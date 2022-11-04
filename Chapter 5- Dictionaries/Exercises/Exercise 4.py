rivers = {
    'amazon': 'brazil',
    'mekong': 'china',
    'ganges': 'india',
    'danube': 'germany',
    'volga': 'europe',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this dictionary:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this dictionary:")
for country in rivers.values():
    print("- " + country.title())