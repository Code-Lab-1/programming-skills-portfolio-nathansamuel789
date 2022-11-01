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