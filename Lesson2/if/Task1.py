#Практика: Возраст
age = float(input("Enter your age: "))


def who_is_user(user_age):
    float(user_age)

    if user_age < 5:
        resp = "Your age is " + str(user_age) + ". You must be pupil of a kindergarten!"
    elif user_age < 16:
        resp = "Your age is " + str(user_age) + ". You must be a schoolboy!"
    elif user_age < 22:
        resp = "Your age is " + str(user_age) + ". You must be a student!"
    else:
        resp = "Your age is " + str(user_age) + ". It is time to start working!"
    return resp


val = who_is_user(age)
print(val)


