stopped = False
car_started = False

while stopped != True:
    choice = input('> ')
    choice = choice.lower();
    if choice == 'start':
        if car_started == True:
            print('The car is already started...')
        else:
            print('Car started... Ready to go!')
            car_started = True
    elif choice == 'stop':
        if car_started == True:
            print('Car Stopped.')
            car_started = False
        else:
            print('The car is not started!')
    elif choice == 'exit': 
        stopped = True
    elif choice == 'help':
        print('''
 Start: Starts the car
 Stop: Stops the car
 Exit: Exits the program
        ''')
    else:
        print('Unknown command. Type help for help.')