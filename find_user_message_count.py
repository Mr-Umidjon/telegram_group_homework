from read_data import read_data
from find_all_users_id import find_all_users_id


def find_user_message_count(data: dict, users_id: str) -> dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    message_count = dict(zip(users_id, [0]*len(users_id)))
    # print(message_count)
    for message in data['messages']:
        user_id = message.get('from_id', False)
        if user_id and user_id in users_id:
            message_count[user_id] += 1




    return message_count


data = read_data('data/result.json')
users_id = find_all_users_id(data)

# print(users_id)
# print(data['messages'])

print(find_user_message_count(data, users_id))