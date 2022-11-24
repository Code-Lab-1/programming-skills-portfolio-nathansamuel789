sand_wich = ['beef', 'tuna', 'sausage', 'chicken']
finished_sandwiches = []

while sand_wich:
    current_sandwich = sand_wich.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")