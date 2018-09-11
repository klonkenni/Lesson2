
def ask_user():
    try:
        # Часть №1 Будет спрашивать "Как дела?", пока не ответит хорошо.
        while True:
                print("Как дела?")
                reply = input("")
                if reply == "Хорошо":
                    break

        print("Хочешь что-нибудь спросить?")

        # Часть №2 Бесконечный диалог с ботом :)
        while True:
                user_question = input("")
                answers = {"Как дела?": "Хорошо", "Что делаешь?": "Танцую", "Хочешь есть?": "Очень"}
                print(answers.get(user_question, "Мне нечего ответить") + ". Может еще что-нибудь спросишь?")

    except KeyboardInterrupt:
        print("Пока!")


ask_user()

