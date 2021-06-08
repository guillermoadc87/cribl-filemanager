from flask import Blueprint, jsonify
from flask_restx import Api

from .resources.main import main_ns


v1_blueprint = Blueprint('v1_blueprint', __name__, url_prefix='/api/v1')

api_v1 = Api(v1_blueprint,
             title='FileUploader',
             version='1.0',
             description='')

api_v1.add_namespace(main_ns)


