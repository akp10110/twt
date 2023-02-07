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


def get_user_tweet_timeline_by_id(user_id: str, auth_token: str, until_id: str = None):
    url = f'https://api.twitter.com/2/users/{user_id}/tweets'
    headers = {'authorization': f'Bearer {auth_token}'}
    params = None
    if until_id is not None:
        params = {'until_id': until_id}

    response = requests.get(url, headers=headers, params=params)
    response_json = json.loads(response.text)
    return response_json


def get_user_tweet_timeline_by_id_2(user_id: str, auth_token: str):
    response_json = get_user_tweet_timeline_by_id(user_id, auth_token)
    response_data = response_json['data']
    response_meta = response_json['meta']
    oldest_id = response_meta['oldest_id']
    response_data_merged = response_data

    counter =range(5)
    for i in counter:
        response_json = get_user_tweet_timeline_by_id(user_id, auth_token, until_id=oldest_id)
        response_data = response_json['data']
        response_meta = response_json['meta']
        oldest_id = response_meta['oldest_id']
        response_data_merged = response_data_merged + response_data
        print(response_data_merged)

