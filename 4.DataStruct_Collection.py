#collection = single "variable" used to store multiple values

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#LIST
my_list = [2, 4, 13, 17, 89]

#Tuple 
my_tuple = (2, 4, 6, 7, 8)

#Set
my_set = {1, 4, 6, 8,}

#Dict
my_dict = {"a": 1, "b": 2, "c": 3}



for index, list in enumerate(my_list):
    print(f"{index} {list}")
