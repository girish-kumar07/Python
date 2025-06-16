def time_difference(first_time,second_time):
    first_time_hours = int(first_time[:2])
    first_time_minutes = int(first_time[2:])

    second_time_hours = int(second_time[:2])
    second_time_minutes = int(second_time[2:])

    first_time_total_minutes = first_time_hours * 60 + first_time_minutes
    second_time_total_minutes = second_time_hours * 60 + second_time_minutes

    difference_of_time = second_time_total_minutes - first_time_total_minutes

    if difference_of_time <0:
        difference_of_time = difference_of_time + (24*60) 

    hours_in_time_difference = int(difference_of_time/60)
    minutes_in_time_difference = difference_of_time%60

    return hours_in_time_difference,minutes_in_time_difference

first_time = input("Enter the first time:- ")
second_time = input("Enter the second time:- ")

hours,minutes = time_difference(first_time,second_time)

print(hours,"hours",minutes,"minutes")