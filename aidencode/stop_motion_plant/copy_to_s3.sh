#!/bin/bash

PYTHON3=/usr/bin/python3
UPLOAD_SCRIPT=/home/pi/myCode/pythonProjects/scripts/pipeline/upload_file_to_s3.py
IMAGE_PATH=/home/pi/plant_images/*
BUCKET_NAME=plant.photo.bucket

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
echo "Starting copy at $current_time"


if [ "$#" == "2" ]; then
	aws_key=$1
	aws_secret=$2
	local_source=$IMAGE_PATH
	remote_destination=$BUCKET_NAME
elif [ "$#" == "4" ]; then
	aws_key=$1
	aws_secret=$2
	local_source=$3
	remote_destination=$4
else
	echo "Illegal number of parameters"
	exit -1
fi

aws_key=$1
aws_secret=$2



for filepath in $local_source; do
	echo $filepath
	filename=$(basename $filepath)
	echo $filename
	$PYTHON3 $UPLOAD_SCRIPT $remote_destination $filepath $aws_key $aws_secret $filename
	retVal=$?
	if [ $retVal -ne 0 ]; then
    		echo "Unable to upload file"
	else
		echo "Deleting file $filename"
		rm $filepath
	fi
done
