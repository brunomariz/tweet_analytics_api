import requests
from credentials.api import BEARER_TOKEN

def get_user_data_by_username(username):
    headers = {'Authorization': 'Bearer ' + BEARER_TOKEN}
    url = f'https://api.twitter.com/2/users/by/username/{username}?user.fields=created_at'

    r = requests.get(url, headers=headers)
    data = r.json()['data']
    return {'id': data['id'], 'name': data['name'], 'username': data['username'], 'createdAt': data['created_at']}