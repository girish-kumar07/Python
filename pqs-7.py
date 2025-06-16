def display_date(date_int):
    date = str(date_int)

    month = int(date[:2])
    day = int(date[2:4])
    year = int(date[4:])

    month_name = ['','January','February','March','April','May','June','July','August','September','October','November','December']

    month_name = month_name[month]
    print(month_name,day,",",year)

date_int = input("Enter the date in MMDDYYYY formate:- ")
display_date(date_int)