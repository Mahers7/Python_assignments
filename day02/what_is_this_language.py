language = ""
while language.capitalize() != "Python":
    language = input("what is this programming language? ")

    if language.capitalize() == "Python":
        print(f"you are right it is {language}")
        print("still here")
    else:
        print("not good")
              