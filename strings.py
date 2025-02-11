#write a python program to create string and display oth character, display 3rd to 6th character, display 6th character onwards, display last character, print the string twice and concatenate two strings.


str_1 = str(input("Enter the first string:"))
print("First String:",str_1)
print("0th character:",str_1[0])
print("3rd to 6th character:",str_1[3:6])
print("6th onwards:",str_1[6::])
print("Last character:",str_1[-1])
print("String Twice:",str_1*2)
str_2 = str(input("Enter the another string:"))
str_3 = str_1 + str_2
print("Concatenated String:",str_3)
