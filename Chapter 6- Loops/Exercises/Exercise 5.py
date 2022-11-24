sand_wich = ['beef', 'tuna','pastrami', 'sausage','pastrami', 'chicken','pastrami']
finished_sandwiches = []


print("I'm sorry, we dont have pastrami today.")
while 'pastrami' in sand_wich:
    sand_wich.remove('pastrami')
    
while sand_wich:
    current_sandwich = sand_wich.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)


print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")