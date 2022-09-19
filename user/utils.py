import jwt
import logging
from django.conf import settings
from rest_framework.response import Response


logging.basicConfig(filename='fundoo_note.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class JWTService:
    """
    Create Generic Class JWTService
    """
    
    def encode_token(self, payload):
        """
        create encode function
        """
        try:
            if not isinstance(payload, dict):
                return Response({"message": "payload"})
                

            encode_tokenn = jwt.encode(payload, key='settings.SECRET_KEY', algorithm='HS256')
            return encode_tokenn
        except Exception as e:
            logger.exception(e)
            
            return Response({"message": str(e)})

    
    def decode_token(self, token):
        """
        create decode function
        """
        try:
            decode_tokenn = jwt.decode(token, key='settings.SECRET_KEY', algorithms=["HS256"])
            
            return decode_tokenn
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e)})
