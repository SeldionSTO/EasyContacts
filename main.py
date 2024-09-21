from contacts import contacts
from ui import ui, Menu, Form
from utilities import * 

print_style(type_I="text_line",msg="Welcome to your contact list")

dict_menu = Menu(True)
dict_menu.lst = {"options" : ["1. Main Directory", "2. Emergency Directory"], "actions" : {"1" : contacts("Main Directory", "data\contacts.json"), "2" : contacts("Emergency Directory", "data\emer.json")}}
selected_dir = run_menu(dict_menu)

contact_menu = Menu(True)
contact_menu.lst = {"options" : ["1. Add a new contact", "2. Search for a contact by name.", "3. update or delete an existing contact.", "4. Display all saved contacts.", "type q to quit"], "actions" : {"1" : selected_dir.new, "2" : selected_dir.search, "3": selected_dir.update, "4" : selected_dir.display}}

if selected_dir :
    run_menu(contact_menu)()
