import json
from ui import ui
from utilities import * 

class contacts :
    def __init__(self, name,  dir_input) :
        self.savedir = dir_input
        self.name = name

    def save_data(self, data_file: list, print_msg = False, msg = None) :
        with open(self.savedir, "w") as file :
            file.write(json.dumps(data_file, indent=4))

        if print_msg == True :
            print(msg)

    def load_data(self) : 
        try :
            js_str = open(self.savedir, "r").read()
            JSdata = json.loads(js_str)
        except FileNotFoundError:
            self.save_data(data_file=[])
            js_str = open(self.savedir, "r").read()
            JSdata = json.loads(js_str)
            
        return JSdata  

    def new(self) : 
        JSdata = self.load_data()
        print_style()
        
        user_input  = ui.form_person() 

        if is_phone(user_input["phone"]) :
            if is_email(user_input["email"]) :
                saved_data = list()
                id_lst = list()

                for i in range(len(JSdata)) :
                    saved_data.append(JSdata[i])
                    if JSdata[i]["id"] :
                        id_lst.append(JSdata[i]["id"])

                if len(id_lst) >= 1 : id = max(id_lst) + 1 
                else : id = 1
                
                contact = [{"id" : id,"name": user_input["name"], "phone": user_input["phone"],"email": user_input["email"]}]
                saved_data.append(contact[0])
                self.save_data(saved_data)
            else :
                print_error("You didn't enter a valid email")
        else :
            print_error("You didn't enter a valid phone nr")
        

    def search(self) :  
        JSdata = self.load_data()
        
        print_style()
        name_inpt = input("Enter a name: ")
        found = False

        for item in JSdata :
        
            if item["name"].lower() == name_inpt.lower() :
                print_style(2, "text_line", "Contact Found:")
                print("id: ", item["id"], "\nName: ", item["name"], "\nPhone Number: ", item["phone"], "\nEmail: ", item["email"])
                found = True
            else : 
                continue

        if not found :
            print(name_inpt, "not found!")

    def update(self) : 
        JSdata = self.load_data()
        
        print_style()
        name_inpt = input("Enter an ID: ")
        found = False
        for i in range(len(JSdata)) :
            try :   
                if JSdata[i]["id"] == int(name_inpt):
                    id_lc = i
                    found = True
            except :
                print("Invalid ID")
                break
        if not found :  
            print("Id: ", name_inpt, "not found!")
        else :
            print(f"You selected {JSdata[id_lc]['name']}")
            update_method = ui.menu(["1. delete", "2. update"])
            if update_method == "1" :
                    JSdata.pop(id_lc)
                    self.save_data(JSdata)
                    
            elif update_method == "2" :
                    print("Type in the new value of what you want to change")
                    name = input("Name: ")
                    phone = input("Phone Number: ")
                    email = input("Email: ")

                    if is_phone(phone) :
                        if is_email(email) :
                            JSdata[i]["name"] = name
                            JSdata[i]["phone"] = phone
                            JSdata[i]["email"] = email

                            self.save_data(JSdata)
                        else :
                            print("\033[91mYou didn't enter a valid email\033[0m")
                    else :
                        print("\033[91mYou didn't enter a valid phone nr\033[0m")

    def display(self) : 
        JSdata = self.load_data()
        print_style(type_I="text_line", msg="Your contact list")

        for item in JSdata : 
            print("id:", item["id"], "\nName:", item["name"], "\nPhone Number:", item["phone"], "\nEmail:", item["email"], "\n")
