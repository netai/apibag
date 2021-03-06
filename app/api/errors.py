from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code=200, message=None):
    payload = {'status': 'failed'}
    if status_code!=200:
        payload['error'] = HTTP_STATUS_CODES.get(status_code, 'Unknown error')
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def bad_request(message):
    return error_response(400, message)

def resource_exist(resource):
    return error_response(200, f'Requested <{resource}> already exists.')

def resource_not_exist(resource):
    return error_response(200, f'Requested <{resource}> not exists.')

def unknown_error(message):
    return error_response(500, f'Unknown error has occurred, ({message})')

def invalid_token():
    return error_response(200, f'Provide a valid auth token.')