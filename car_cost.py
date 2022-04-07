#######################################################################
# Program Filename: driving_cost
# Author:  Bronte McKinnis
# Date:4/7/2022
# Description: Takes MPG or MPGe and calculates the cost of either gas or electricity for 1 person and 1 year
# Output: cost of gas in OR and CA or cost of electricity in Corvallis and at a charging station
#######################################################################

# get MPG and type of car
print('Please print the MPG or MPGe for your car.')
miles_per_gallon = input()
miles_per_gallon = float(miles_per_gallon)

print('Input 0 for a gas or hybrid car and 1 for an electric car.')
car_type = input()  # 0 is a gas/hybrid car and 1 is electric

# convert to gallons per year and print
years_per_gallon = miles_per_gallon / 14032
gallons_per_year = 1 / years_per_gallon
print('Gallons used per year: ' + str(gallons_per_year))

# gas and hybrid car costs
if car_type == '0':

    # calculate cost in OR
    cost_OR = gallons_per_year * 4.72
    print('The cost of gas in OR per year is ' + str(cost_OR))

    # calculate cost in CA
    cost_CA = gallons_per_year * 5.
    print('The cost of gas in CA per year is ' + str(cost_CA))

# electric car cost
elif car_type == '1':

    # convert gallons to kWh
    kWh_per_year = gallons_per_year * 33.7

    # calculate price of electricity in Corvallis
    cost_Corvallis = kWh_per_year * 0.1116
    print('The cost of electricity in Corvallis per year is ' + str(cost_Corvallis))

    # calculate the price of electricity at charging stations
    cost_station = kWh_per_year * 0.30
    print('The cost of electricity at charging stations per year is ' + str(cost_station))
