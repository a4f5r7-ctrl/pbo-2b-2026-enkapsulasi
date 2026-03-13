class Member:
    # constructor
    def __init__(self, id, nama, email):
        
        if not isinstance(id, str):
            raise TypeError("id harus string")
        
        if not isinstance(nama, str):
            raise TypeError("nama harus string")
        
        if not isinstance(email, str):
            raise TypeError("email harus string")
        
        if len(id) < 1:
            raise ValueError("id minimal karakter")
        
        
        self.__id = id
        self.__nama = nama
        self.__email = email
        self.__last_visited = None
    # setter
    def set_nama(self,nama):
        if not isinstance(nama, str):
            raise TypeError("nama harus string")

        if len(nama) < 1:
            raise ValueError("id minimal karakter")
        
        self.__nama= nama

    # getter  
    def get_id(self):
        return self.__id


    # getter  
    def get_nama(self):
        return self.__nama