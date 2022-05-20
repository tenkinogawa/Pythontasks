file = open("c_n_c.txt", "w+") # 'r' - read, 'w' - write, 'w+' - read & write
c_a_c = {"Poland": "Warsaw", "Germany": "Berlin"}

for country, capital in c_a_c.items():
    file.write(country + "-" + capital + "\n")

file.close()

file = open("c_n_c.txt")

for line in file.readlines():
    print(line.strip())

file.close()