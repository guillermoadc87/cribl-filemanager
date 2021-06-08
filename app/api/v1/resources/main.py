
import os
from datetime import datetime
from flask import request, send_file, current_app
from flask_restx import Resource, Namespace
from .mixin import HelperMixIn
from ..parser import file_upload, file_name

main_ns = Namespace('Main', path="/")

@main_ns.route('/upload/<customername>/')
class UploadFile(HelperMixIn, Resource):

    @main_ns.expect(file_upload)
    def post(self, customername):
        """
        Uploads customer's bundle tgz to and S3 bucket

        :return:
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
        key      = f'{customername}/{filename}.tgz'

        # Upload file
        self.upload_file(key, tgz_file)
        
        return {'success': True}, 200

@main_ns.route('/list/<customername>/')
class GetFiles(HelperMixIn, Resource):

    def get(self, customername):
        """
        Return a list of files for the customer

        :return:
        """

        # Get files for customer
        file_list = self.list_files(customername)

        return {'success': True, 'files': file_list, 'totals': len(file_list)}, 200

@main_ns.route('/download/<customername>/<filename>/')
class GetFiles(HelperMixIn, Resource):

    def get(self, customername, filename):
        """
        Return a the contents of a file the customer wants to download

        :return:
        """

        file = self.download_file(customername, filename)
        
        print(file)

        return send_file(file, as_attachment=True)