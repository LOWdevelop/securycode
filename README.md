# Welcom To SecuryCode

    1. How to use Lib

First Config your FireBase --> https://github.com/LOWdevelop/securycode/blob/main/FirebaseSettings.md

Clone your Lib to your project https://github.com/LOWdevelop/securycode

# Using Lib in your code
    
    1. import secury_code   #Import lib
    
# Instance Class
    2. secury = secury_code.secury_key('https://securycode-code-default-rtdb.firebaseio.com/')  # paste you firebase url ( YES USE "/" IN FINAL LIN)

# Using Commands 1
   
    1. Commmad --> response = secury.check_key(key="key for check") # This command check and return state of key (in dictionary format)
 
    Example :  
        response['registered'] is state of the key
        response['userid'] is id associate from key  ( USERNAME )
        
        response['registered'] return this values ->
            if key exist and not used : "not_registered"
            if key exist and key used : "registered"
            if key not exist : "Key Not Exist"
    
       
# Using Commands 2
    2. Command --> secury.register_key(response['userid'])
this command associate key to user HWID.
So that only his pc can open the application with that key

# Using Commands 3
    3. Command --> seucry.auth_key(response['userid'])
This command will verify, if the key is already registered, if it is associated with the same HWID that is making the request.
returning true or false, so you can access the program

this function returns a bool

