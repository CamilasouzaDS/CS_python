user_name = input("User name: ")
password = input("Password: ")

name_db = "camila"
password_db = '12345'

if user_name == name_db and password == password_db:
    print('Welcome')
else:
    print('User name of password incorrect')

print(f'the total amount is {len(user_name) + len(password)}')

