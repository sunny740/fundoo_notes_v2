import redis
import logging

logging.basicConfig(filename='user_logs.log', encoding='utf-8', level=logging.DEBUG)


class RedisServices:
    """
    create new class RedisServces
    """     
    def __init__(self):
        """
        create a constructor
        """

        self.redis_client = redis.Redis(host='localhost',port=6379)


    def get(self, key):
        """
        create get method
        """
        try:
            return self.redis_client.get(key)
        except Exception as e:
            logging.exception(e)
            raise Exception("Data is unable in redis server")
            

    def set(self, key, value):
        """
        create set method
        """
        try:
            return self.redis_client.set(key, value)
        except Exception as e:
            logging.exception(e)
            raise Exception("Data is unable in redis server")        

