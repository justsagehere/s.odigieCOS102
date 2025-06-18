#python program program to sway two cities

#To take input from the user
city_1 = input('Enter name of city 1: ')
city_2 = input('Enter name of city 2: ')

#create  temporary variable and swap the cities
temp = city_1
city_1 = city_2
city_2 = temp

print (f"The name of City 1 after swapping is {city_1}")
print(f"the name of City 2 after swapping is {city_2}")