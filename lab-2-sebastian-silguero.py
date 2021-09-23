# Prgrammers: Jonathan, Sebastian, Alex
# Course: CS151, Dr. Rajeev
# Date: September 23rd, 2021
# Lab Number: 2
# Program Inputs: Births per second, deaths per second, immigration per second, and current population
# Program Outputs: Estimate of the population in the future of a country

print("Let's estimate the future population of your country")

# User inputs births per second, deaths per second, and immigration per second
birthSecond = float(input("Please input births per second: "))
deathSecond = float(input("Please input deaths per second: "))
immigrationSecond = float(input("Please input immigrations per second: "))
currentPopulation = float(input("Please input the current population: "))
futureYear = float(input("Please input how many years in the future you want to see: "))

# Seconds in a day
secondsDay = 864000

# Converting seconds in to one day
birthDay = birthSecond * secondsDay
deathDay = deathSecond * secondsDay
immigrationDay = immigrationSecond * secondsDay

# Converting days into one year

birthYear = birthDay * 365
deathYear = deathDay * 365
immigrationYear = immigrationDay * 365

# Calculate the output

futurePopulation = futureYear * (birthYear + deathYear + immigrationYear)

print("Your country will have a population of " + str(futurePopulation))







