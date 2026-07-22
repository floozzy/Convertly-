states = {}



def set_state(
    user_id,
    key,
    value
):

    if user_id not in states:

        states[user_id] = {}


    states[user_id][key] = value





def get_state(
    user_id,
    key,
    default=None
):

    return states.get(

        user_id,

        {}

    ).get(

        key,

        default

    )





def clear_state(
    user_id,
    key=None
):

    if user_id not in states:

        return



    # очистить только один режим

    if key:

        states[user_id].pop(

            key,

            None

        )


        return




    # полностью очистить пользователя

    states.pop(

        user_id,

        None

    )
