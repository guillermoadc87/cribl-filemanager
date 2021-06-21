
from datetime import datetime
from ..parser import file_upload
from .mixin import HelperMixIn, S3MixIn
from flask import send_file, current_app
from flask_restx import Resource, Namespace

main_ns = Namespace('Main', path="/")

@main_ns.route('/upload/<customer>/')
class UploadFile(HelperMixIn, S3MixIn, Resource):

    @main_ns.expect(file_upload)
    def post(self, customer):
        """
        Uploads customer's bundle tgz to and S3 bucket
        """
        current_app.logger.info(f"{self.__class__.__name__}")

        # Get payload
        payload = file_upload.parse_args()
        tgz_file = payload['tgz_file']

        # Validate the file extension os allowed
        if not self.allowed_file(tgz_file.filename):
            return {'success': False, 'error': 'Bundle extention needs to be tgz'}, 404

        # Generate bucket key
        filename = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        key = f'{customer}/{filename}.tgz'

        # Upload file
        self.upload_file(key, tgz_file)

        return {'success': True}, 200

@main_ns.route('/list/<customer>/')
class GetFiles(S3MixIn, Resource):

    def get(self, customer):
        """
        Return a list of files for the customer
        """

        # Get files for customer
        file_list = self.list_files(customer)

        return {'success': True, 'files': file_list, 'totals': len(file_list)}, 200

@main_ns.route('/download/<customer>/<filename>/')
class DownloadFiles(S3MixIn, Resource):

    def get(self, customer, filename):
        """
        Return a the contents of a file the customer wants to download
        """

        file = self.download_file(customer, filename)

        print(file)

        return send_file(file, as_attachment=True)
