# Create list for each piece of info from the three camping activities
camp_activitys_list = ["Cultural immersion", "Kayaking and pancakes", "Mountain biking"]
camp_length_list = ["5", "3", "4"]
camp_difficulty_list = ["easy", "moderate", "difficult"]
camp_cost_list = ["$800", "$400", "$900"]

# Prints the three different camp options and info about them
def printcamps():
    print('These are the activitys and their cost:')
    loop_count = 3
    for i in range(loop_count):
        print(f'{camp_activitys_list[i]} which lasts {camp_length_list[i]}.The difficulty is {camp_difficulty_list[i]} and the cost is {camp_cost_list[1]}')

# Asks for users info and choices for camp, meal, and transport
def userinput():
    user_first_name = input('What is your name? ')
    while user_first_name == "" or user_first_name.isdigit() == True:
        user_first_name = input('Name can not be blank or number. Please re-enter your name: ') 
    user_age = int(input('What is your age? '))
    if user_age < 5:
        print('You are to young to join camp.')
    elif user_age > 17:
        print('You are to old to join camp')
    else:
        camp_choice = input('Enter the number for the camp you want to attend: ')
        meal_choice = input('What meal do you want (standard/vegeterian/vegan)? ')
        transport_choice = input('Would you like to take the shuttle bus (extra $80)')

        print(f'Hello {user_first_name}, you are {user_age}. You have chosen to attend {camp_activitys_list} which lasts {camp_length_list} and is {camp_difficulty_list} difficulty. Your meal choice is {meal_choice}')
        camp_confirmation = input("Please confirm you'd like to attend the camp with the cost of ... (yes/no):")

        if camp_confirmation == 'yes':
            print('Enjoy the camp!')
        elif camp_confirmation == 'no':
            print('Camp application cancelled.')
        else:
            camp_confirmation = input('Please enter yes or no for you comfirmation: ')

printcamps()
userinput()
