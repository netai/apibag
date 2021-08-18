from flask import request
from app.api.errors import bad_request, unknown_error
from app.helpers import ValidationHelper


def api_test():
    try:
        resp_obj = {}
        if request.method == 'GET':
            data = request.args or {}
            validation = ValidationHelper(
                data,
                {
                    'value': {
                        'required': True
                    }
                }
            ).valid()

            if validation['is_valid']:
                resp_obj = {
                        'status': 'success',
                        'data': {
                            'value': data.get('value')
                        }
                    }

                return resp_obj
            else:
                return bad_request(validation['messages'])

    except Exception as e:
        print(e)
        return unknown_error(e)