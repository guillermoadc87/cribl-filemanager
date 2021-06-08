from werkzeug.datastructures import FileStorage
from flask_restx import reqparse

file_upload = reqparse.RequestParser()
file_upload.add_argument('tgz_file',  
                         type=FileStorage, 
                         location='files', 
                         required=True, 
                         help='TGZ file')

file_name = reqparse.RequestParser()
file_name.add_argument('filename',  
                         type=str, 
                         location='args', 
                         help='TGZ filename')