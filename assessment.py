# Creating constants for the max and min age to join and the price of the bus.
MIN_AGE = 5
MAX_AGE = 17
CAMP_LEADER_AGE = 15
SHUTTLE_COST = 80

# Creates empty variables for users info.
user_first_name = ""
user_age = ""
meal_choice = ""
camp_choice = ""
camp_total_cost = ""
camp_confirmation = ""
camp_leader = ""

# Creates empty lists for the camp info.
camp_activitys_list = []
camp_length_list = []
camp_difficulty_list = []
camp_cost_list = []

# Add items to the list for each piece of info from the three camping activities.
camp_activitys_list = ["Cultural immersion", "Kayaking and pancakes", "Mountain biking"]
camp_length_list = ["5", "3", "4"]
camp_difficulty_list = ["easy", "moderate", "difficult"]
camp_cost_list = [800, 400, 900]

# Creates empty lists for other info.
meal_choice_list = []
camp_leader_answers = []
transport_answer = []
confirmation_answer = []

# Adds items to the list for acceptable answers.
meal_choice_list = ['standard', 'vegan', 'vegeterian']
camp_leader_answers = ['yes', 'no']
transport_answer = ['yes', 'no']
confirmation_answer = ['yes', 'no']

# Prints the three different camp options and info about them.
def printcamps():
    print('These are the activitys and their cost:')
    print('Number')
    loop_count = 3
    for i in range(loop_count):
        print(f'{i}      {camp_activitys_list[i]} lasts {camp_length_list[i]} days, it is cosidered {camp_difficulty_list[i]}. The cost is ${camp_cost_list[i]}.')

# Asks for users name and making sure it is letters not numbers or left blank.
def userinput():
    global user_first_name, user_age, camp_choice, meal_choice, camp_total_cost, camp_leader
    user_first_name = input('What is your name? ')
    while user_first_name == "" or user_first_name.isalpha() == False:
        user_first_name = input('Name can not be blank or number. Please re-enter your name in letters: ')

# Asks for users age and makes sure they are between the min and max age. Asks if user wants to be a camp leader if eligable.
    while True:
        try:
            user_age = int(input('What is your age? '))
            break
        except ValueError:
            print('Age must be number, not letter or blankspace. Please re-enter.')
    if user_age < MIN_AGE:
        print('You are to young to join camp.')
    elif user_age > MAX_AGE:
        print('You are to old to join camp')
    elif user_age >= CAMP_LEADER_AGE:
        camp_leader = input('Since you are fifteen or older, you are eligable to become a camp leader. Would you like to be one? (yes/no): ').lower()
        while camp_leader not in camp_leader_answers:
            camp_leader = input('Please enter yes or no: ').lower()
        if camp_leader == 'yes':
            camp_leader = ' as a camp leader,'
        elif camp_leader == 'no':
            camp_leader = ''

# Asks user which camp they would like to attend and the meal they want, while checking they are entering a correct camp number and avalible meal choice.
        while True:
            try:
                camp_choice = int(input('Enter the number for the camp you want to attend: '))
                if camp_choice in range(3):
                    break
            except ValueError:
                print('Camp number must be 0, 1, or 2. Please re-enter.')
        meal_choice = input('What meal do you want (standard/vegeterian/vegan)? ').lower()
        while meal_choice not in meal_choice_list:
            meal_choice = input('We dont offer that meal. Please select from the avalible options (standard/vegeterian/vegan): ').lower()

# Asks user if they would like transport and making sure it is a yes or no answer.
        transport_choice = input('Would you like to take the shuttle bus (extra $80, yes/no)? ').lower()
        while transport_choice not in transport_answer:
            transport_choice = input('Please enter a yes or no answer: ').lower()
        if transport_choice == 'yes':
            camp_total_cost = SHUTTLE_COST + (camp_cost_list[camp_choice])
        elif transport_choice == 'no':
                camp_total_cost = (camp_cost_list[camp_choice])

# Asks user same information if they said no to being a camp leader or are to young to be a camp leader.

# Asks user which camp they would like to attend and the meal they want, while checking they are entering a correct camp number and avalible meal choice.
    else:
        while True:
            try:
                camp_choice = int(input('Enter the number for the camp you want to attend: '))
                if camp_choice in range(3):
                    break
                else:
                    print('Please enter one of the correct numbers (0/1/2)')
            except ValueError:
                print('Camp number must be 0, 1, or 2. Please re-enter.')
        meal_choice = input('What meal do you want (standard/vegeterian/vegan)? ').lower()
        while meal_choice not in meal_choice_list:
            meal_choice = input('We dont offer that meal. Please select from the avalible options (standard/vegeterian/vegan): ').lower()

# Asks user if they would like transport and making sure it is a yes or no answer.
        transport_choice = input('Would you like to take the shuttle bus (extra $80, yes/no)? ').lower()
        while transport_choice not in transport_answer:
            transport_choice = input('Answer can not be blank or number, please enter a yes or no answer: ').lower()
        if transport_choice == 'yes':
            camp_total_cost = SHUTTLE_COST + (camp_cost_list[camp_choice])
        elif transport_choice == 'no':
                camp_total_cost = (camp_cost_list[camp_choice]) 


def campconfirmation():

# Prints users info and info about the camp the selected/meal choice. Asks them if they want to confirm their camp application with the total cost of it.
    print(f'Hello {user_first_name}, you are {user_age}. You have chosen to attend {camp_activitys_list[camp_choice]}{camp_leader} which lasts {camp_length_list[camp_choice]} days and is {camp_difficulty_list[camp_choice]}. Your meal choice is {meal_choice}.')
    camp_confirmation = input(f"Please confirm you'd like to attend the camp with the cost of ${camp_total_cost} (yes/no): ").lower()

# Prints different message depending on if the user confirmed or denied the camp application.
    while camp_confirmation not in confirmation_answer:
        camp_confirmation = input('Please confirm your application by entering yes or no: ').lower()
    if camp_confirmation == 'yes':
            print('Enjoy the camp!')
    elif camp_confirmation == 'no':
            print('Camp application cancelled.')
    else:
            camp_confirmation = input('Please enter yes or no for your comfirmation: ').lower()

# Runs the subroutines.
printcamps()
userinput()
campconfirmation()