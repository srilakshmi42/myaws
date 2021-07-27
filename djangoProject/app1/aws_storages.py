from storages.backends.s3boto3 import s3Boto3Storage

class DynamicFiles(S3Boto3Storage):
    location = "media"
    file_overwrite = False