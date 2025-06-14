total = 0
s = int(input('Enter a number or "done":'))
while s != 'done':
    num = int(s)
    total = total + num
    s = input('Enter a number or "done":')
print('The sum of entered number is',total)