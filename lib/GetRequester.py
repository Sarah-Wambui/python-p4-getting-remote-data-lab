import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
    

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
data = get_requester.load_json()
print(data)

# execute the file as a script
# python lib/GetRequester.py
