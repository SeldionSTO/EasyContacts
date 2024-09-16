from contacts import contacts
from ui import ui

running = True
main_dir = contacts("Main Directory", "contacts.json")
emer_dir = contacts("Emergency Directory", "emer.json")

opt_lst = ["Add a new contact", "Search for a contact by name.", "update or delete an existing contact.", "Display all saved contacts."]

ui.print_style(type_I="text_line",msg="Welcome to your contact list")

dict_choice = None

while running :

    user_choice = ui.menu(opt_lst)

    if user_choice == "1" :
        main_dir.new()
    
    elif user_choice == "2": 
        main_dir.search()
    elif user_choice == "3" : 
        main_dir.update()
    
    elif user_choice == "4" :
        main_dir.display()
    
    elif user_choice == "q" :
        running = False

    else :
        print("You didn't enter a valid input")
    
    if running : 
        input("Press any key to go back to the menu")
    ui.print_style()