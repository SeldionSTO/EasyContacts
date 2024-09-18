class ui :
    def menu(lst) : 
        for i in range(len(lst)) :
            print(lst[i])
        
        c_input = input("-> ")
        return c_input
    
    def form_person() :
        name_inpt = input("Enter Name: ")
        phone_inpt = input("Enter Phone Number: ")
        email_inpt = input("Enter Email Address: ")

        output_data = {"name":name_inpt, "phone":phone_inpt, "email" : email_inpt}
        return output_data