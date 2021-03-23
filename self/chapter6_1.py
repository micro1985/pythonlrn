def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


#answer = ask_yes_no("\nPlease, enter 'y' or 'n': ")
#print("Thnx for ypur answer ",answer)


def birthday(name, age):
    print("Happy birthday", name, ". Now you are",age, "old")

birthday(name1 = "Dasha", age1 = 22)
