import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    

    def load_json(self):
        response_body = self.get_response_body()
        json_data = response_body.decode('utf-8')
        return json.loads(json_data)
    

requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').get_response_body()
data = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').load_json()
print(data)

# execute the file as a script
# python lib/GetRequester.py
