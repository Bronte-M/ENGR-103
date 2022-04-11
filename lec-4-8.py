# class example on user input

mpge_car = input('Enter the MPGe for your car: ')

cost_driving_OR_peryear = (0.18 * 33.7) * 14000 // int(mpge_car)  # $

print('You probably spend $', cost_driving_OR_peryear, ' per year on electricity.')