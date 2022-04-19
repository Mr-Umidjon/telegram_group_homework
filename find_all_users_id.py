from read_data import read_data


def find_all_users_id(data: dict) -> list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users_ids = []
    for message in data['messages']:
        if message['type'] == 'message':
            users_ids.append(message['from_id'])
        else:
            users_ids.append(message['actor_id'])

    return users_ids


data = read_data("data/result.json")
print(find_all_users_id(data))
# print(data['messages'])
