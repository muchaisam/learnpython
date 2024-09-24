#Lists - ordered mutable collections of items
#tuples - ordered immutable collections of items
#dictionaries - unordered collections of key value pairs

#List
fruits = ["apple", "mango", "banana"]
fruits.append("date")
print(fruits)

#tuple
coordinates = (10, 20)
print(coordinates[1])

#dictionary
person = {'name': 'Sammy',
          'age': 50,
          'city': 'Nairobi'
}
print(person["name"])
person["job"] = "Engineer"
print(person)