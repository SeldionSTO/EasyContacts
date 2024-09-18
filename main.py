from contacts import contacts
from ui import ui
from utilities import * 

running = True

dir_lst = ["1. Main Directory", "2. Emergency Directory"]
opt_lst = ["1. Add a new contact", "2. Search for a contact by name.", "3. update or delete an existing contact.", "4. Display all saved contacts.", "type q to quit"]

print_style(type_I="text_line",msg="Welcome to your contact list")

dict_choice = ui.menu(dir_lst)

sel_dir = None
if dict_choice == "1":
    sel_dir = contacts("Main Directory", "data\contacts.json")
elif dict_choice == "2":
    sel_dir = contacts("Emergency Directory", "data\emer.json")
else:
    print_error("Invalid directory choice. Please restart the program.")
    running = False


menu_action = {"1" : sel_dir.new, "2" : sel_dir.search, "3": sel_dir.update, "4" : sel_dir.display}

while running and sel_dir:
    user_choice = ui.menu(opt_lst)

    if user_choice in menu_action :
        menu_action[user_choice]()
    elif user_choice == "q" :
        running = False
    else :  
        print_error("You didn't enter a valid input")
    
    if running : 
        input("Press any key to go back to the menu\n")
    print_style()

