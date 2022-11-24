prompt = "\nWhat toppings would you want to add on your pizza?"
prompt += "\nEnter 'finshed' when you are done:"

while True:
    topping = input(prompt)
    if topping != 'finished':
        print("  I will add " + topping + " to your pizza.")
    else:
        break