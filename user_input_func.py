from validation import validate_positive_number, validate_str_empty

def user_text_input(msg):
    user_input = ""
    while not validate_str_empty(user_input):
        user_input = input(f"{msg}: ")
    return user_input


def user_num_input(msg):
    user_input = ""
    while not validate_positive_number(user_input):
        user_input = input(f"{msg}: ")
    return int(user_input)

if __name__ == "__main__":
    user_num_input("please")