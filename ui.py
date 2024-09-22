from utilities import *
class ui :
    def __init__(self):
        self

class Menu(ui) :
    def __init__(self, active=False):
        super().__init__()
        self.active = active
        self.lst = []

    def display(self) :
        for option in self.lst['options'] :
            print(option)

        return input("-> ")
    
    def process(self, choice) :
            if choice in self.lst['actions'] :
                if callable(self.lst['actions'][choice]) :
                    return self.lst['actions'][choice]()
                else :
                    self.active = False
                    return self.lst['actions'][choice]
            elif choice == "q" : 
                self.active = False
            else:
                print_error("Invalid input.")

class Form(ui) :
    def __init__(self):
        super().__init__()

    def form_person() :
        name_inpt = input("Enter Name: ")
        phone_inpt = input("Enter Phone Number: ")
        email_inpt = input("Enter Email Address: ")

        output_data = {"name":name_inpt, "phone":phone_inpt, "email" : email_inpt}
        return output_data