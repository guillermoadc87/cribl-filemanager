import boto3
from flask import current_app

class HelperMixIn:

    def allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in current_app.config.get('ALLOWED_EXTENSIONS')

class S3MixIn:

    def __init__(self, *args, **kwargs):
        super(S3MixIn, self).__init__(*args, **kwargs)
        self.s3_client()

    def s3_client(self):
        session = boto3.session.Session()
        self.client = session.client('s3')

        return self.client
    
    def upload_file(self, key, tgz_file):
        """
        Function to upload a file to an S3 bucket
        """
        response = self.client.put_object(
            Bucket=current_app.config.get('S3_BUCKET'), 
            Key=key,
            Body=tgz_file
        )

        return response
        
    def list_files(self, customername):
        """
        Function to list files in a given S3 bucket
        """
        response = self.client.list_objects(
            Bucket=current_app.config.get('S3_BUCKET'),
            Prefix=customername
        )

        file_list = []

        # Parser key to get filename and add to list
        for data in response['Contents']:
            filename = data['Key'].split(f'{customername}/')[-1]
            file_list.append(filename)

        return file_list

    def download_file(self, customername, filename):
        """
        Function to list files in a given S3 bucket
        """
        f = f"/tmp/{filename}"

        self.client.download_file(
            Bucket=current_app.config.get('S3_BUCKET'),
            Key=f'{customername}/{filename}',
            Filename=f
        )

        return f