from flask import Blueprint, jsonify
from src.controllers.controller import get_form_data, get_db_data
routes = Blueprint('routes', __name__)

ROUTE_POST = '/'
ROUTE_GET = '/'

@routes.route(ROUTE_POST, methods=['POST'])
def post_response():
    status, data = get_form_data()
    if status == 200:
        return f"Form data received successfully: {data}", 200
    else:
        return "Failed to receive form data", 400
    
@routes.route(ROUTE_GET, methods=['GET'])
def get_response():
    status, data = get_db_data()
    if status != 200:
        return "Failed to retrieve data from the database", 500
    return jsonify(data), 200