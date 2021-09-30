# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr.Rajeev
# Date: September 23rd, 2021
# Lab Number: 2
# Program Inputs: User inputs; Births per second, Death per second, Migrations per second, current population, and Amount of years into the future
# Program Outputs: Estimates future population size for a country

# Necessary User Inputs (Births, Deaths, Migrations per second, Current Population, and Years into the future)
current_population = float(input("Enter current population: "))
amount_years = float(input("Enter how many years into future: "))
births_per_second = float(input("Enter births per second: "))
deaths_per_second = float(input("Enter deaths per second: "))
migrations_per_second = float(input("Enter migrations per second (for emigration please use negative sign) : "))
1
# Declaring amount of seconds in desired years
seconds_per_desired_year = (86400 * 365) * amount_years

# Converting Inputs from seconds to year
total_births = births_per_second * seconds_per_desired_year
total_deaths = deaths_per_second * seconds_per_desired_year
total_migrations = migrations_per_second * seconds_per_desired_year

# Final population after inputted years
future_population = current_population + total_births - total_deaths + total_migrations
future_population = int(future_population)

# Closing statement with output data
if future_population > 0:
    print("\nYour Population in " + str(amount_years) + " years will be, " + str(future_population))
else:
    print("\nYour population has died out! :( , current population is " + str(future_population))

print("\nThanks for using our code!")



