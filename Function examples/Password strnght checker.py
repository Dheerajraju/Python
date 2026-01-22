def is_strong_password(password):
    """This function checks if the password is strong or not"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password): #isdigit() function is used to check any digit is present in the password
        return False
    if not any(char.islower() for char in password): #islower() function is used to check lower case character in the password
        return False
    if not any(char.isupper() for char in password): #isupper() function is used ti=o check upper case character in the password
        return False
    if not any(char in '!@#$%^&*()_+' for char in password): #to check any special character present in the password
        return False
    return True

## calling the function
print(is_strong_password("WeakPwd"))
print(is_strong_password("Str0ngPwd!"))
    
