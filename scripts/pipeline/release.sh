bucket_name=$1
local_resource=$2
aws_access_key=$3
aws_access_secret=$4
local_path=$5

# Install required dependencies for Python script.
pip3 install boto3

ls -ltr

# Run upload script
python3 scripts/pipeline/upload_file_to_s3.py $bucket_name $local_resource $aws_access_key $aws_access_secret $local_path