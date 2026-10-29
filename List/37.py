lst = [16, 13, 16]
new_lst = lst[::-1]
print(new_lst)
if lst == new_lst:
    print("List is palindrome...")
else:
    print("List is not palindrome...")