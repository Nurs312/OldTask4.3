message = 'Hello! '
while True:
    name = input(f"Please, enter your name. ")
    msg = f"{message} {name.title()}"
    print(msg)
    with open('guest_book.txt', 'a') as file:
        file.write(msg + "\n")

