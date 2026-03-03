# Create list for each piece of info from the three camping activities
camp_activitys_list = ["Cultural immersion", "Kayaking and pancakes", "Mountain biking"]
camp_length_list = ["5", "3", "4"]
camp_difficulty_list = ["easy", "moderate", "difficult"]
camp_cost_list = ["$800", "$400", "$900"]

def printcamps():
    print('These are the activitys and their cost:')
    loop_count = 3

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

printcamps()
userinput()
