# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr.Rajeev
# Date: September 23rd, 2021
# Lab Number: 2
# Program Inputs: User inputs; Births per second, Death per second, Migrations per second, current population, and Amount of years into the future
# Program Outputs: Estimates future population size for a country

# Necessary User Inputs (Births, Deaths, Migrations per second, Current Population, and Years into the future)
current_population = float(input("Enter current population: "))
amount_years = int(input("Enter how many years into future: "))
births_per_second = float(input("Enter births per second: "))
deaths_per_second = float(input("Enter deaths per second: "))
migrations_per_second = float(input("Enter migrations (-) per second: "))

# Declaring amount of seconds in a day
seconds_per_year = 86400 * 365

# Converting Inputs from seconds to year
births_per_year = births_per_second * seconds_per_year
deaths_per_year = deaths_per_second * seconds_per_year
migrations_per_year = migrations_per_second * seconds_per_year

# Total outcome of Subtracting deaths and migrations per year from births per year)
total_difference = births_per_year - deaths_per_year - migrations_per_year

# Amount to be added onto the current population based on amount of years into future wished to be calculated
difference_in_future = total_difference * amount_years

# Final population after inputted years
total_population = int(current_population + difference_in_future)

# Closing statement with output data
print("\nYour Population in " + str(amount_years) + " years will be, " + str(total_population))
print("\nThanks for using our code!")



