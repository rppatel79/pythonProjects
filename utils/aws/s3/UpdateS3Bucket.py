import boto3
import sys

class UpdateS3Bucket:
    def __init__(self, bucketName, profile="default"):
        session = boto3.Session(profile_name=profile)
        self.s3 = session.client('s3')
        self.bucketName = bucketName

    def updateWithConfig(self, config) -> object:
        return self.s3.put_bucket_website(Bucket=self.bucketName,
                                   WebsiteConfiguration=config)

    def updateWithRedirectHostName(self, redirectHostName)-> object:
        config = {
            'RedirectAllRequestsTo': {
                'HostName': redirectHostName
            }
        }
        return self.updateWithConfig(config)


if __name__ == '__main__':
    updateS3Bucket = UpdateS3Bucket(sys.argv[1], sys.argv[2])
    updateS3Bucket.updateWithRedirectHostName("myHostName")
