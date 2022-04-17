from flask import Response
import json


def create_data_resp(data, status=200):
    return Response(response=json.dumps(data),
                    status=status,
                    mimetype='application/json')


def create_exception_resp(exception):
    data = json.dumps(dict(error=exception.args[0]))
    return Response(response=data,
                    status=400,
                    mimetype='application/json')
