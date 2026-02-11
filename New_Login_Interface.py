
import pwinput
import Program

incorrectt = 0
print("New Command Interface.")
while True: 
    qusername = input("Username: ")
    qpassword = pwinput.pwinput(("Password: ")) 
    
    if qusername == "bob":
        if qpassword == "bob":
            print("Access Granted...") 
            Program.program()
            break
        else: 
            incorrectt += 1
            if incorrectt != 3:
                print("Password incorrect try again") 
            
        
    else: 
        incorrectt += 1
        if incorrectt != 3:
            print("Password incorrect try again") 
          
    if incorrectt == 3: 
        print("Oi Emma you little bum get out")
        print("Your Are Banned") 
        break


