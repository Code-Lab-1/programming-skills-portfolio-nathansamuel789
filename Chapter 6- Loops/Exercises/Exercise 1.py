prompt = "\nWhat toppings would you like to add on your pizza?"
prompt += "\nEnter 'quit' when you are done:"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break