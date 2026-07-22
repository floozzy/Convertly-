states = {}



def set_state(
    user_id,
    key,
    value=True
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







def has_state(
    user_id,
    key
):

    return key in states.get(

        user_id,

        {}

    )







def clear_state(
    user_id,
    key=None
):

    if user_id not in states:

        return



    # удалить конкретное состояние

    if key:


        states[user_id].pop(

            key,

            None

        )


        return





    # удалить все состояния пользователя

    states.pop(

        user_id,

        None

    )
