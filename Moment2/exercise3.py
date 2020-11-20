# Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
userList = []
finalize = False
while(not finalize):
    numbers = int(input("Enter the numbers you want to count, use '0' to number from '<' to '>': "))
    if(numbers == 0):
        finalize=True
    else:
        userList.append(numbers)
userList.sort()
 
print("These are the numbers from lowest to highest",userList)