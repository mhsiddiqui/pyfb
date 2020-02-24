from collections import namedtuple
import json

d = {
  "data": [
    {
      "access_token": "EAACrRQJvMygBAICBn2uVRUW25teO2CIBM8h4CjzJTZBZCGOVxGq45ljfnKYyGIxdvZCtRC00uskpddZA6DRGNWF9hkcVSiGZC9lkY8OyRbXLZCwEvXSUezMA7pwu7E9eGCyNjbL2N4sYwxJqR9m7aCZAM19P0ZCE9BZAocL1FZAMgIjLVExSBebezzsy46R4ZCoBb6jcQ5mi9yGQwZDZD",
      "category": "Video Game",
      "category_list": [
        {
          "id": "211579738882707",
          "name": "Video Game"
        }
      ],
      "name": "Xinon Games",
      "id": "372707443159301",
      "tasks": [
        "ANALYZE",
        "ADVERTISE",
        "MODERATE",
        "CREATE_CONTENT",
        "MANAGE"
      ]
    },
    {
      "access_token": "EAACrRQJvMygBAM5vOk9DpYZAbqMgmZCEXGK6ihGip6RwMYO18aLZCKcHP2E8zPOwTuzkp3Slc1zre5N8aSUZAZAkLxPLGbniB4ZCMhpTqM1bKW6YuaVcAynjFQZBrunViQDJ7qMzWZCoeRsExW3197LeoPQuDvTNodJJpNZBPbsOnemLBzVoMXoZC58ULTK5OwjgT5EO60mibZALQZDZD",
      "category": "Jewelry/Watches",
      "category_list": [
        {
          "id": "2226",
          "name": "Jewelry/Watches"
        }
      ],
      "name": "WeMart.Pk",
      "id": "538291146570689",
      "tasks": [
        "ANALYZE",
        "ADVERTISE",
        "MODERATE",
        "CREATE_CONTENT",
        "MANAGE"
      ]
    }
  ],
  "paging": {
    "cursors": {
      "before": "MzcyNzA3NDQzMTU5MzAx",
      "after": "NTM4MjkxMTQ2NTcwNjg5"
    }
  }
}
print(d)

class Objectify:

  def __init__(self, id='Object'):
    super().__init__()
    self.id = id
  
  def foo(self):
    json.loads(json.dumps(d), object_hook=lambda d: namedtuple(self.id, d.keys())(*d.values()))