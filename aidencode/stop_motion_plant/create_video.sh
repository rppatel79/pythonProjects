#!/bin/bash

TMP_LOC=/home/pi/tmp/

file_name=animation
current_time=$(date "+%Y.%m.%d-%H.%M.%S")
new_fileName=$file_name.$current_time.mp4
echo "New FileName: " "$new_fileName"

#AWS CLI
#sudo pip install awscli

mkdir -p $TMP_LOC
cd $TMP_LOC

echo "Downloading files"
aws s3 sync s3://plant.photo.bucket $TMP_LOC

echo "Creating video in $TMP_LOC $new_fileName"
ffmpeg -framerate 25 -pattern_type glob -i '*.jpg' -vf "transpose=3"  -c:v libx264 -pix_fmt yuv420p $new_fileName

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error"
else
    echo "Successfully created video $TMP_LOC $new_fileName"

    echo "Removing jpgs"
    rm *.jpg

    echo "Done"
fi
