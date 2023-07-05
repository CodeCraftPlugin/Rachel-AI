my_str = 'bobby'

my_list = ['bobby', 'hadz', 'com']

result = my_str in my_list
print(result)  # 👉️ True

if my_str in my_list:
    # 👇️ this runs
    print('The string is in the list')
else:
    print('The string is NOT in the list')