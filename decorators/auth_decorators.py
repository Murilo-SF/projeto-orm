# ================================================================DECORATOR/role_required================================================================
from flask_jwt_extended import (verify_jwt_in_request, get_jwt)

from flask import (jsonify)

from functools import wraps

def role_required(role):
	def decorator(fn):
		
		@wraps(fn)

		def wrapper (*args, **kwargs):

			verify_jwt_in_request()

			claims = get_jwt()

			if claims['role'] != role:
				return jsonify ( { "error" : "ACESSO NEGADO!" } ), 403

			return fn (*args, **kwargs)

		return wrapper

	return decorator