import requests
import json


def get_user_by_username(username: str):
    url = f'https://api.twitter.com/2/users/by/username/{username}'
    headers = {'authorization': 'Bearer '}
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    return response_json


resp = get_user_by_username('coolfunnytshirt')
print(resp['data']['name'])
