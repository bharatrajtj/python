#### List is represented with []
countries_name=["Canada", "India", "ScotLand"]
print(countries_name)

### Length of List
countries_name=["Canada", "India", "ScotLand"]
print(len(countries_name))

### List can be appended. Lists are mutable
countries_name=["Canada", "India", "ScotLand"]
countries_name.append("France")
print(countries_name)


### Remove keyword can be used on List but not on Tuples

countries_name=["Canada", "India", "ScotLand"]
countries_name.remove("India")
print(countries_name)

#### Slicing: creation of list from existing list (upper bound is not counted)
countries_name=["Canada", "India", "ScotLand"]
shortlist = countries_name[0:2]
print(shortlist)

#### String Concatination
countries_name=["Canada", "India", "ScotLand"]
print(countries_name[0] +" "+ countries_name[2])

#### Tuples are represented by () and cannot be appended. Tuples are immutable
countries_name=("Canada", "India", "ScotLand")
print(countries_name)
