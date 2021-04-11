name = ""
age = ""
username = ""
password = ""
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
            
            mode = input("""Choose what you would like to do by entering the number:
            1: Add passwords 2: View passwords 3: Exit :""").strip()
            return mode
        
        
print("Welcome to Password Manager")
print("If you are 13 or older, You will be able to use Password Manager")\
    
name = input("What is your name? ")
age = int(input ("How old are you? "))

while True:
    chosen_option = menu(name, age)
    
    if chosen_option == "1":
        username = input("Type in your username here: ")
        password = input("Type in your password here: ")
        
        
        
    if chosen_option == "2":
        print("Please sign in to view existing passwords")
        signin_username = (input("Please enter your username: "))
        if signin_username == username:
            signin_password = (input("Please enter your password: "))
            if signin_password == password:
                print("You are signed in")
                print("Here are your saved passwords and usernames: ", password, username)
            else:
                print("Your login credentials do not match any in our database")
                
    

    if chosen_option == "3":
        print("Goodbye, thanks for using password manager")
        break
    
    
        
