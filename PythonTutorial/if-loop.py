light = input("What color is the light [red/green/yellow] ")


## LONG WAY
# if light == "red":
#     print('Wait')
# elif light == "yellow":
#     print("Be ready!")
# elif light == "green":
#     print("Go!")
# else:
#     print("Wrong value")

print("Go!") if light == 'green' else print("Wait")