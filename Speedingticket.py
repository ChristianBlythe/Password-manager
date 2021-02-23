name = ""
age = ""
# empty list for storing new passwords and usernames
password_list = []
# list with existing usernames and passwords
member_list = ["student", "password123"]


def menu(name, age):
    
    print("Hello!", name)
    
    if age < 13:
        print("Sorry, but you do not meet the minimum age requirement for this program. ")
        exit()
        
        
    else:
            
            mode = input("""Choose a mode by entering the number:
            1: Add passwords 2: View passwords 3: Exit :""").strip()
            return mode
        
        
print("Welcome to Password Manager")
print("If you are 13 or older, You can store access details to websites or mobile apps")\
    
name = input("What is your name? ")
age = int(input ("How old are you? "))

while True:
    chosen_option = menu(name, age)
    
    if chosen_option == "1":
        print("Successful")
        
        
        
    elif chosen_option == "2":
        print("Successful")
        
    

    elif chosen_option == "3":
        break
    
    else: 
        print("Sorry, that was not a valid option. Please try again later")
        
print("Goodbye, thanks for using password manager")