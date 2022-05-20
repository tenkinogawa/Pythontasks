coutries_n_capitals = {"Poland":"Warsaw", "Germany":"Berlin", 
                       "Czechia":"Praga"}

try:
    print(2 / 0)
    print(coutries_n_capitals["USA"])
except KeyError:
    print("Key not found")
except ZeroDivisionError:
  print("Cannot divide by 0")
finally:
    print("Always here")
print("Here")