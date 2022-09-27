import json

from notes.redis_utils import RedisServices


class RedisNote:
    """
    create a RedisNote
    """
    
    def __init__(self):
        self.redis = RedisServices()


    def set(self, userid, notes):
        noteid = notes.get("id")
        print(noteid)
        note_dict = self.get(userid)
        print(note_dict)
        note_dict.update({noteid : notes})
        self.redis.set(userid, json.dumps(note_dict))
        return self.get(userid)


    def get(self,userid):
        get_val = self.redis.get(userid)
        print(get_val)
        return json.loads(get_val) if get_val else {}


    def put(self, note):
        user_id = note.get("user")
        print(user_id)
        note_id = note.get("id")
        print(note_id)
        note_dictionary = self.get(user_id)

        if note_dictionary:
            note_dictionary.update({note_id: note})
            self.redis.set(user_id, json.dumps(note_dictionary))
        return self.get(user_id)


    def delete(self, note_object):
        user_id = note_object.user_id
        print(user_id)
        note_id = note_object.id
        print(note_id)
        note_dictionary = self.get(user_id)
        print(note_dictionary)
        note_dictionary.pop(str(note_id))
        self.redis.set(user_id, json.dumps(note_dictionary))

