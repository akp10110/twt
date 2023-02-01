from services.lib.utlis import twt_api

auth_token = ''

# Get user id
response = twt_api.get_user_by_username('', auth_token)
user_id = response['data']['id']

# Get followers
response = twt_api.get_followers_of_user_id(user_id, auth_token)
print(response['data'])
