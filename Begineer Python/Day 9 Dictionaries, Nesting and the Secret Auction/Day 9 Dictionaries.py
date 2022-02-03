programming_dictionaries ={
    "Bug" : "An error in a program that prevents the program from running as expected",
    "Function" : "A piece of code that you can easily call over and over again"
}

#Retrieving items from dictionary
#print(programming_dictionaries["Bug"])

#Adding new items to dictionary
programming_dictionaries["Loop"] = "The action of doing something over and over again"


#Creating an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionaries = {}
# print(programming_dictionaries)

#Edit an item in a dictionary
programming_dictionaries["Bug"] = "A moth in your computer"
#print(programming_dictionaries)

#Loop through a dictionary
for key in programming_dictionaries:
    print(key)
    print(programming_dictionaries[key])

#############################
#Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

#Nesting a list in a Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting Dictionary in a Dictionary

travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany" : {"cities_vistited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5}
}

#Nesting Dictionary in a List

travel_log = [
    {
        "country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    {
        "country" : "Germany",
        "cities_vistited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5}
]



