# Create list for each piece of info from the three camping activitys
camp_activitys_list = ["Cultural immersion", "Kayaking & pancakes", "Mountain biking"]
camp_length_list = ["5", "3", "4"]
camp_difficulty_list = ["easy", "moderate", "difficult"]
camp_cost_list = ["$800", "$400", "$900"]

def printcamps():
    print('These are the activitys and their cost:')
    camp_count = 0
    while camp_count < 4:
        print(f'{camp_activitys_list[camp_count]} lasts {camp_length_list[camp_count]} days. The difficulty is {camp_difficulty_list[camp_count]}, it costs {camp_cost_list[camp_count]}')
        camp_count = camp_count +1 
                                                                                                                                                                                                          