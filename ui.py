class ui :
    @classmethod
    def menu(cls, lst) : 
        for i in range(len(lst)) :
            print(lst[i])
        
        user_choice = input("-> ")
        return user_choice