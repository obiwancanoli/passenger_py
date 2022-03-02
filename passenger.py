# PASSENGER by Daniel Murillo 


# This is a password generator application.
# The user can either create a randomly generated password or enter their own.
# That new password is then COPIED to the user's clipboard using the pyperclip module. 
# The user can then PASTE the new password wherever! 

#IMPORT:--------------------------------------------------------------------------------------
import sys, pyperclip, random, string 
# The string module contains a number of useful constants, classes and a number of functions to process the standard python string.



#DATA STRUCTURES:-----------------------------------------------------------------------------

lower_case = string.ascii_lowercase #All lower case letters
upper_case = string.ascii_uppercase #All upper case letters
num = string.digits #The string ‘0123456789’.
symbols = '+&^%$#@!*' #String of ASCII characters which are considered punctuation characters in the C locale.



#FUNCTIONS:-----------------------------------------------------------------------------------

def password_gen(): # This function takes a users input and replaces certain letters with certain characters
    
    usr_entry = input('''
    Enter your current password that you want to better secure: ''') 
    # Input from the user. 

    new_pass = usr_entry.replace('s' or 'S', '$').replace('e' or 'E', '3').replace('a' or 'A', '@').replace('i' or 'I', '!').replace('o' or 'O', '0').replace('g' or 'G', '&').replace('t' or 'T', '+') 
    # (new_pass) represents the new password with the replaced letters.

    pyperclip.copy(new_pass) 
    #Pyperclip module now copies new password (new_pass) to the user's clipboard.
    
    print('''
    Your newly generated password is: ''' + new_pass + ''' 
    (This password has also been pasted to your clipboard!)
    ''') 
    # The user can now 'PASTE' their newly generated password anywhere!

def random_password(): # This function generates a random password based on the length the user inputs

    while True:
        usr_entry = input('''
    Please enter desired length of password: ''')
        if usr_entry.isdecimal():
            break
        else:
            print('''
            INVALID ENTRY! PLEASE ENTER A VALID NUMBER!''')

    all = lower_case + upper_case + num + symbols #Combine the data structures
    temp = random.sample(all, int(usr_entry)) # temp is used as a placeholder for randomizing all the data structures (all) and using the usr_enry to determine length of password. 
    new_pass = "".join(temp) # .join() combines items in a list into a string. 

    pyperclip.copy(new_pass)

    print('''
    Your newly generated password is: ''' + new_pass + ''' 
    (This password has also been pasted to your clipboard!)
    ''') 
    # The user can now 'PASTE' their newly generated password anywhere!


#--------------------------------------------START-OF-PROGRAM--------------------------------------------------------------------

print('''
 ************ Welcome to Passenger: A Password Generator Program ************''')

while True: # Main loop of the program
    user_input = input('''
    Enter: 'x' to make your current password stronger. 
    Enter: 'y' to generate a random password.
    Enter: 'exit' to leave the program: ''').lower() # The lower() method makes user's input lowercased to ensure argument passing. 

# The options (x, y or exit) and what they execute when called upon. 
    if user_input == 'x': 
        password_gen() # 'x' takes a user's input and replaces certain letters with certain characters 
    elif user_input == 'y': # 'y' generates a random password based on the length the user inputs.
        random_password()
    elif user_input == 'exit': # 'exit' breaks out of the Main loop and ENDS the program.
        break
    else:
        print('''
            INVALID ENTRY! PLEASE ENTER A VALID ENTRY!''') 
        continue #If the user does not enter 'x', 'y' or 'exit' the program goes back to the start until the user enters a valid entry.  
    
    while True:
        user_question = input('''Would you like to generate another password? (y/n): ''').lower() # Asks if user wants to restart Main loop again. 
        if user_question == 'y': # Returns to Main loop.
            break
        elif user_question == 'n': # END Program
            print('''
            Thank you for using the program!
            (To close the window, press: 'COMMAND' + Q)''')
            sys.exit()
        else:
            print('''
            INVALID ENTRY! PLEASE ENTER A VALID ENTRY! 
                ''')
            
            
            # Will contiune to loop until user enters either 'y' or 'n'. 

print('''
Thank you for using the program!
(To close the window, press: 'COMMAND' + Q)
''')

#------------------------------------------------END-OF-PROGRAM-----------------------------------------------------------------------

