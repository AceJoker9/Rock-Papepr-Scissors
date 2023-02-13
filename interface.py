
def validate_to_int(str_input):
    while True:
        try:
            user_input = input(str_input)
            return int(user_input)
        except:
            print("Invalid choice. Try again.")
            pass
                

validate_to_int()

red = validate_to_int

