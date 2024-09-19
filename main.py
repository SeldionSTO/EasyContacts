from contacts import contacts
from ui import ui, Menu, Form
from utilities import * 

running = True

dir_lst = []
opt_lst = []

print_style(type_I="text_line",msg="Welcome to your contact list")
#main_ui = Ui()
dict_menu = Menu(True)
dict_menu.lst = {"options" : ["1. Main Directory", "2. Emergency Directory"], "actions" : {"1" : contacts("Main Directory", "data\contacts.json"), "2" : contacts("Emergency Directory", "data\emer.json")}}

while dict_menu.active == True :
    choice = dict_menu.display()
    selected_dir = dict_menu.process(choice)

contact_menu = Menu(True)
contact_menu.lst = {"options" : ["1. Add a new contact", "2. Search for a contact by name.", "3. update or delete an existing contact.", "4. Display all saved contacts.", "type q to quit"], "actions" : {"1" : selected_dir.new, "2" : selected_dir.search, "3": selected_dir.update, "4" : selected_dir.display}}

while contact_menu.active == True :
    choice = contact_menu.display()
    action = contact_menu.process(choice)
    action()