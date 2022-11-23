question= "How old are you?"
question += "\nEnter 'done' when you are finished. "

while True:
    age = input(question)
    if age == 'done':
        break
    age = int(age)

    if age < 3:
        print("You get a free ticket")
    elif age < 13:
        print("  Your ticket will be 36 dhs.")
    else:
        print("  Your ticket will be 45 dhs.")