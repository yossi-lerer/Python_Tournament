def user_text_input(msg):
    return input(f"{msg}: ")

def user_num_input(msg):
    try:
        return int(input(f"{msg}: "))
    except:
        return False
