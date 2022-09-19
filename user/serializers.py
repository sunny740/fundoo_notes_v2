import logging
from asyncio.log import logger
from rest_framework import serializers
from .models import User


logging.basicConfig(filename='fundoo_note.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()                    


class RegisterSerializer(serializers.ModelSerializer):
    """
    serializer class
    """

    def create(self, validated_data):
        """
        Create and return a new instance, given the validated data.
        """
        try:
            return User.objects.create_user(**validated_data)
        except Exception as e:
            logger.exception(str(e))


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'location', 'is_verified']