# Program to check the list contains elements of another list

# List1
List1 = [1, 2, 3]

# List2
List2 = [4, 5, 6, 3, 2, 1]

check = all(item in List1 for item in List2)

if check is True:
    print("The list {} contains all elements of the list {}".format(List1, List2))
else:
    print("No, List1 doesn't have all elements of the List2.")
