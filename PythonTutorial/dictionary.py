countries_n_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_n_capitals["Czechia"] = "Prague"
print(countries_n_capitals)

for key in countries_n_capitals.keys():
    print(key)

for value in countries_n_capitals.values():
    print(value)

for country, capital in countries_n_capitals.items():
    print(country + "-" + capital)

# print(countries_n_capitals["France"]) #error
print(countries_n_capitals.get("France")) #none

print(countries_n_capitals.setdefault("USA", "Washington DC"))

for country, capital in countries_n_capitals.items():
  print(country + "-" + capital)

# print(countries_n_capitals.pop("Poland"))

for country, capital in countries_n_capitals.items():
  print(country + "-" + capital)
print(countries_n_capitals.popitem())

for country, capital in countries_n_capitals.items():
  print(country + "-" + capital)

if "Poland" in countries_n_capitals.keys():
  print("Found")
else:
  print("Not found")

print("Poland" in countries_n_capitals)
countries_n_capitals.clear()
print(countries_n_capitals)