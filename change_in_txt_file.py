with open("my_file.txt","r") as f:
    info = f.read()

new_info = info.__add__("\nCurrently I am  in my first year of Graduation")
print(new_info)

with open("my_file.txt","w") as f:
    f.write(new_info)