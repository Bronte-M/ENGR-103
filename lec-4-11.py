# ask for showers per week and typical shower length
showers_per_week = int(input('How many showers do you take per week? '))
shower_length = float(input('How long do your showers take? (minutes) '))

# find how many gallons per week
gal_per_week = shower_length * 2 * showers_per_week

print('You use approximately', gal_per_week, 'gallons of water showering per week.')