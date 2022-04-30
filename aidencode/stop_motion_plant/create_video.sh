#!/bin/bash

TMP_LOC=/home/pi/tmp/
DEFAULT_FILENAME=plant_video_420
DEFAULT_BUCKETNAME=plant.photo.bucket

if [ "$#" = "0" ]
then
	file_name=$DEFAULT_FILENAME
	bucket_name=$DEFAULT_BUCKETNAME
elif [ "$#" = "2" ]
then
	file_name=$1
	bucket_name=$2
else
	echo "Illegal number of parameters"
	exit -1
fi

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
echo "Starting video at $current_time"

#new_fileName=$file_name.$current_time.mp4
new_fileName=$file_name.mp4
echo "New FileName: " "$new_fileName"
echo "Bucket name: " "$bucket_name"

#AWS CLI
#sudo pip install awscli

mkdir -p $TMP_LOC
cd $TMP_LOC

echo "Downloading files"
/usr/local/bin/aws s3 sync s3://$bucket_name $TMP_LOC

echo "Creating video in $TMP_LOC $new_fileName"
ffmpeg -framerate 12 -pattern_type glob -i '*.jpg' -vf "transpose=2"  -c:v libx264 -pix_fmt yuv420p $new_fileName

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error"
else
    echo "Successfully created video $TMP_LOC $new_fileName"

    echo "Removing jpgs"
    rm *.jpg

    echo "Done"
fi
