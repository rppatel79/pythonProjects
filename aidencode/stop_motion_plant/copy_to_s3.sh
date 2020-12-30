#!/bin/bash

PYTHON3=/usr/bin/python3
UPLOAD_SCRIPT=/home/pi/myCode/pythonProjects/scripts/pipeline/upload_file_to_s3.py
IMAGE_PATH=/home/pi/plant_images/*
BUCKET_NAME=plant.photo.bucket

if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
fi

aws_key=$1
aws_secret=$2

for filepath in $IMAGE_PATH; do
	echo $filepath
	filename=$(basename $filepath)
	echo $filename
	$PYTHON3 $UPLOAD_SCRIPT $BUCKET_NAME $filepath $aws_key $aws_secret $filename
	retVal=$?
	if [ $retVal -ne 0 ]; then
    		echo "Unable to upload file"
	else
		echo "Deleting file $filename"
		rm $filepath
	fi
done
