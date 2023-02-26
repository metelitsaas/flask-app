from flask import make_response, jsonify


def bad_request(message):
    response = jsonify({"error": "bad_request", "message": message})
    status_code = 400

    return make_response(response, status_code)


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    status_code = 401

    return make_response(response, status_code)


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    status_code = 403

    return make_response(response, status_code)
