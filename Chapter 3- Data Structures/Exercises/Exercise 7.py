people = ['JP Falcon', 'Jose', 'Raven']

name = people[0].title()
print(name + ", please come to my dinner.")

name = people[1].title()
print(name + ", please come to my dinner.")

name = people[2].title()
print(name + ", please come to my dinner.")

name = people[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(people[1])
people.insert(1, 'Adhenz')


name = people[0].title()
print("\n" + name + ", please come to dinner.")

name = people[1].title()
print(name + ", please come to dinner.")

name = people[2].title()
print(name + ", please come to dinner.")

print("\nWe got a bigger table!")
people.insert(0, 'Ron Man')
people.insert(2, 'Gerald Frien')
people.append('John')

name =  people[0].title()
print(name + ", please come to dinner.")

name = people[1].title()
print(name + ", please come to dinner.")

name = people[2].title()
print(name + ", please come to dinner.")

name = people[3].title()
print(name + ", please come to dinner.")

name =  people[4].title()
print(name + ", please come to dinner.")

name =  people[5].title()
print(name + ", please come to dinner.")

print("\nSorry, we can only invite two people to dinner.")

name = people.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = people.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = people.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = people.pop()
print("Sorry, " + name.title() + " there's no room at the table.")


name = people[0].title()
print(name + ", please come to dinner.")

name = people[1].title()
print(name + ", please come to dinner.")


del(people[0])
del(people[0])


print(people)