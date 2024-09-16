class ui :
    @classmethod
    def menu(cls, lst) : 
        for i in range(len(lst)) :
            print(str(i + 1) + ".", lst[i])
        print("type q to quit")

        user_choice = input("-> ")
        return user_choice

    @classmethod
    def print_style(cls, size=4, type_I=None , msg = None, ) :
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