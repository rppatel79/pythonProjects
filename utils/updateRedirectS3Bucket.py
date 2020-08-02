from utils.aws.s3.UpdateS3Bucket import UpdateS3Bucket
from utils.myComputer.MyComputer import MyComputer

import sys, getopt


def main(awsProfile,bucketName, port):
    print("bucketName:"+bucketName)
    print("port"+port)

    try:
        myComputer = MyComputer()
        updateS3Bucket = UpdateS3Bucket(bucketName,awsProfile)
        hostname=myComputer.getExternalIp()+port
        print()
        response = updateS3Bucket.updateWithRedirectHostName(hostname)
        print(response)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage:")
        print("\t<awsProfile> <bucketName> <port>")
        sys.exit()
    main(sys.argv[1], sys.argv[2], sys.argv[3])