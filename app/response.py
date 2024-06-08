from flask import jsonify, make_response

def success(values, pesan):
    res = {
        'data': values,
        'pesan': pesan
    }

    return make_response(jsonify(res)), 200

def failure(values, pesan):
    res = {
        'data': values,
        'pesan': pesan
    }

    return make_response(jsonify(res)), 400