#Практика: Возраст
age = input("Enter your age: ")


def who_is_user(user_age):
    if user_age < 5:
        print("Your age is " + str(user_age) + ". You must be pupil of a kindergarten!")
    elif user_age < 16:
        print("Your age is " + str(user_age) + ". You must be a schoolboy!")
    elif user_age < 22:
        print("Your age is " + str(user_age) + ". You must be a student!")
    else:
        print("Your age is " + str(user_age) + ". It is time to start working!")


who_is_user(int(age))


