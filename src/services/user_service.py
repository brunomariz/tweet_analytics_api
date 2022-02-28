from src.twitter_handler import user_id


def user_data_by_username_service(username):
    return user_id.get_user_data_by_username(username)
