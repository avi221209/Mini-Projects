
while True:
    # Take password input from user
    password = input("Enter a password: ").strip()
    specialchar = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    # Check minimum length
    if len(password) < 8:
        print(" Invalid")
        print("Password must be at least 8 characters")

    # Check if at least one number exists
    elif not any(c.isdigit() for c in password):
        print(" Invalid")
        print("Include at least one number")

    # Check if at least one special character exists
    elif not any(c in specialchar for c in password): 
        print(" Invalid")
        print("Include at least one special character")

    # If all conditions are satisfied
    else:
        print("Password Accepted")
        break  # Exit loop after successful validation



'''
Another methods to do seperate for loop and if else condition
for c in password:
    if c in specialchar:
        print("Special character found")
    
elif not any(c in specialchar for c in password): 
    print(" Invalid")
    print("Include at least one special character")

'''

'''
elif not any(c.isdigit() for c in password):
    print(" Invalid")
    print("Include at least one number")

for c in password:
    if c.isdigit():
        found_digit = True
        break
'''