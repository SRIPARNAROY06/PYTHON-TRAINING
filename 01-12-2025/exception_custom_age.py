class InvalidAgeError(Exception):
    pass

def age_check(age):
    if age <18:
        raise InvalidAgeError
    return "Age is valid"

print(age_check(11))