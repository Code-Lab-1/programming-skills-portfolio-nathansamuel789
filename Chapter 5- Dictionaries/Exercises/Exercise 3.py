glossary =  {
    'string': 'A series of characters.',
    'if..else': 'Python supports the usual logical conditions from mathematics',
    'list': 'A collection of items in a particular order.',
    'dictionary': "A collection of key-value pairs.",
    'operators':'Operators are used to perform operations on variables and values.',
    'arrays':'Arrays are used to store multiple values in one single variable:' ,  
    'function':'A function is a block of code which only runs when it is called.',
    'lambda':'A lambda function can take any number of arguments, but can only have one expression.',
    'sets':'Sets are used to store multiple items in a single variable.',
    'bolleans':'Booleans represent one of two values True or False.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)