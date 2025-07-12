# Good question on Dictionary.
dict = {'January':'31','February':'28','March':'31','April':'30','May':'31','June':'30','July':'31','August':'31','September':'30','October':'31','November':'30','December':'31'}
keys = input("Enter the month name:-").capitalize()
month_31 = []
days = input("Enter the no of days of the month:-")
sorted_by_values = sorted(dict.items(), key=lambda x : x[1])
for key in dict:
    if dict[key] == days:
        month_31.append(key)
print("There are",dict[keys],"days in the month of",keys)
print()
print("All the keys in the dictionary are:-",dict.keys())
print()
print("All the months having",days,"days are:-",month_31)
print()
print("Sorted key value pairs by values:-",sorted_by_values)