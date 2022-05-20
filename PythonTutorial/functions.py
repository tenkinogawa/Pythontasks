from calendar import c


countries_info = {}
countries_info["Polska"] = ("Warszawa", 37.97)
countries_info["Niemcy"] = ("Berlin", 83.02)
countries_info["Słowacja"] = ("Bratysława", 5.45)

print(countries_info)

def show_country_info(country):

    country_info = countries_info.get(country)

    print()
    print(country)
    print("Capital city: " + country_info[0])
    print("Number: " + str(country_info[1]))

def display_sum(a,b):
    print(a+b)

def calculate_sum(a,b):
    return a+b

for country in countries_info.keys():
    print(country)


country = input("What country would you like to display?")
show_country_info(country)
our_sum = display_sum(2,3)
print(our_sum)
print(calculate_sum(3,7))