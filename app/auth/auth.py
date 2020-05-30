import os
import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen

# AUTH0 CONFIGARATIONS
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = os.environ.get('API_AUDIENCE')


# AUTHERROR EXCEPTION
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# AUTH HEADER
def get_token_auth_header():

    auth_header = request.headers.get("Authorization", None)

    if not auth_header:
        raise AuthError({
            "code": "authorization_header_missing",
            "description": "Authorization header is expected"}, 401)

    header_parts = auth_header.split(' ')

    if len(header_parts) != 2 or not header_parts:
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must be in the format"
            " Bearer token"}, 401)

    elif header_parts[0].lower() != 'bearer':
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must be in the format"}, 401)

    return header_parts[1]


# FUNCTION TO CHECK PERMISSION OF REQUEST
def check_permissions(permission, payload):
    if 'permissions' not in payload:
        abort(400)

    if permission not in payload['permissions']:
        raise AuthError({
            "code": "unauthorized",
            "description": "Permission Not Found",
        }, 401)

    return True


# FUNCTION FOR VERIFYING AUTH0 TOKEN
def verify_decode_jwt(token):
    # GET A PUBLIC KEY FORM AUTH 0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN HEADER
    unverified_header = jwt.get_unverified_header(token)

    # AUTH0 TOKEN SHOULD HAVE A ID KEY
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed'
        }, 401)

    rsa_key = {}

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
            break

    # VERIFY THE TOKEN
    if rsa_key:
        try:
            # VALIDATE THE TOKEN USING RSA KEY
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f'https://{AUTH0_DOMAIN}/'
            )
            return payload

        except jwt.ExpiredSignatureError:

            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:

            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, '
                'check the audience and issuer.'
            }, 401)

        except Exception:

            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)

    raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to find the appropriate key.'
    }, 400)


# REQUIRE FUCNTIONS WITH AUTH0 DECORATOR
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
