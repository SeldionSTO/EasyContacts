import re

def print_style(size=4, type_I=None , msg = None) :
    block = "--------"
    line = ""
    
    if size >= 1 :
        for i in range(size) : 
            line = line + block
    
    if type_I != None :
        if type_I.lower() == "text_line" :
            print(f"\n{line}\n", f" {msg} ", f"\n{line}\n")
    else :
        print(line)

def print_error(error_msg) :
    print(f"\033[91m{error_msg}\033[0m")

#simple email validator
def is_email(email) :
    if "@" in email and email.count("@") <= 1 :
        valid = True
    else :
        valid = False
    return valid

#simple phone validator
def is_phone(phone_inpt) :
    phone = phone_inpt.strip().replace(" ", "")
    if re.fullmatch("^[0-9]+", phone) and len(phone) >= 7 and len(phone) <= 12 : 
        valid = True  
    else :
        valid = False      
    return valid

def run_menu(obj) : 
    while obj.active:
        choice = obj.display()
        action = obj.process(choice)
    return action