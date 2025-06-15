week_days = ['Sunday' , 'Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday', 'Saturday']

first_day_of_year = input("Enter the first day of the year:- ").capitalize()

day_number = int(input("Enter the day number in the year:- "))

if first_day_of_year not in week_days:
    print("Entered day name is not valid please enter the valid day name")
    
if day_number<2 or day_number>365:
    print("Entered day number not lies in the year please enter the valid day number.")

# this will calculated the index of the first day among the week days.
first_day_index = week_days.index(first_day_of_year)
# print(first_day_index)

# this will find the index of the entered day according to the indexing of week days.
day_index_entered_number =(first_day_index + (day_number-1)) % 7
# print(day_index_entered_number)

day_name_on_entered_number = week_days[day_index_entered_number]

print("The day on the number ",day_number,"is ",day_name_on_entered_number)
