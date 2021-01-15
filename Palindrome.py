check_for_palindrome_list = ['KAYAK', 'DAD', 'LEVEL', 'king are you glad you are king', 'father', 'america']
print("This is the list we're gonna check: ", check_for_palindrome_list)
print("---------------------------------------------------------------------------------------------------------------------")
i = 0
for i in range (len(check_for_palindrome_list)):
    normal_string = check_for_palindrome_list[i]
    reversed_string = reversed(normal_string)
    if list(normal_string) == list(reversed_string):
        print(check_for_palindrome_list[i], "...is a palindrome")
    else:
        print(check_for_palindrome_list[i], "...is NOT a palindrome")
    i = + 1

# variant 2
print("--------------------------------------------------------------------------")
check_for_palindrome_list_2 = ['KAYAK', 'RADAR', 'LEVEL', 'father', 'america']
def is_palidrome(X):
    for word in X:
        if word == word[::-1]:
            print(word, "is  palidrome")
        else:
            print(word, "is NOT palidrome")
print(is_palidrome(check_for_palindrome_list_2))