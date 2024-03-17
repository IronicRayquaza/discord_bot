from random import choice, randint

def get_response(user_input:str)->str:
    lowered:str=user_input.lower()

    if lowered=='':
        return  'Are you for real a Kanye Fan?'
    elif 'hello' in lowered:
        return 'Yo!! Ye just dropped Vultures!!!!'
    elif 'how are you' in lowered:
        return 'I miss the old Kanye!'
    elif 'fact' in lowered:
        return 'Ye made that bitch famous'
    else:
        return choice(['You seem like a Taylor fan....','Wanna hear some Ye music??','Praise the God'])
