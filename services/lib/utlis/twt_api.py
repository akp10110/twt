import requests
import json


def get_user_by_username(username: str, auth_token: str):
    url = f'https://api.twitter.com/2/users/by/username/{username}'
    headers = {'authorization': f'Bearer {auth_token}'}
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    return response_json


def get_followers_of_user_id(user_id: str, auth_token: str):
    url = f'https://api.twitter.com/2/users/{user_id}/followers'
    headers = {'authorization': f'Bearer {auth_token}'}
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    return response_json


def get_user_tweet_timeline_by_id(user_id: str, auth_token: str):
    url = f'https://api.twitter.com/2/users/{user_id}/tweets'
    headers = {'authorization': f'Bearer {auth_token}'}
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    return response_json
