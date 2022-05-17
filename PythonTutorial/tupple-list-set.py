# ## LIST

# names_list = []
# names_list.append("Marek")
# names_list.append("Julek")
# print(names_list)

# names_list = ["Kamil", "Marek1", "Adam", "Kamil"]
# print(names_list)

# names_list.reverse()
# print(names_list)

# names_list.sort()

# for name in names_list:
#     print(name)

# print(names_list[0])

# print(names_list.count("Kamil"))
# print(len(names_list))

# # print(names_list.pop(0))
# # print(names_list)

# # print(names_list.remove("Kamil"))
# # print(names_list)

# # print(names_list.clear())

# names_list2 = ["Iza", "Ewa", "Ela"]

# names_list3 = names_list + names_list2
# print(names_list3)
# nl = sorted(names_list3, reverse=True)
# print(nl)

## -----------------------------------------------------
## SET
# names_set = {"Kamil", "Mariusz", "Kamil", "Iza"}
# print(names_set)

# empty_set = set()
# empty_set.add("Tytus")
# empty_set.add("John")
# print(empty_set)

# # empty_set.remove("Kamil")
# empty_set.discard("John")
# print(empty_set)

# set3 = names_set.union(empty_set) #connect elements from both sets - do not modify
# print(set3)

# names_set.update(empty_set)

# for name in names_set:
#     print(name)
# print()
# set3 = names_set.difference(empty_set)
# for name in names_set:
#     print(name)

# set3 = names_set.intersection(empty_set)
# print(set3)
# set3 = names_set.symmetric_difference(empty_set)
# print(set3)

# names_list = ["Artur", "Rafał"]
# names_list.extend(set3)
# print(names_list)

## -----------------------------------------------------
##TUPLE

person = ("Kamil", "Nowak", "33")
#names_tuple = ()  #pusta krotka
print(person)
print(len(person))
print(person.count("Kamil"))