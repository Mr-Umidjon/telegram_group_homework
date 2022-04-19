from read_data import read_data


def find_all_users_name(data: dict) -> list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    users = []
    for message in data['messages']:
        user = message.get('actor')
        if user and user not in users:
            users.append(user)

    return users


data = read_data("data/result.json")
print(find_all_users_name(data))
# print(data.keys())
# print(data['messages'][0])
# users = []
# for message in data['messages']:
#     users.append(message.get('actor_id'))
#
# print(users)
