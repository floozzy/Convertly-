user_states = {}



def set_state(
    user_id,
    key,
    value
):

    if user_id not in user_states:

        user_states[user_id] = {}


    user_states[user_id][key] = value





def get_state(
    user_id,
    key,
    default=None
):

    if user_id not in user_states:

        return default


    return user_states[user_id].get(
        key,
        default
    )





def clear_state(
    user_id
):

    if user_id in user_states:

        del user_states[user_id]
