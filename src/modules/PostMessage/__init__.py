import requests

class PostService:
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def post_message(self, message):
        requests.post(self.url, data={
            "api_key": self.key,
            "status": message
        })
