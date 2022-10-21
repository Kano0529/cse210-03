class Parachute:
    def __init__(self):
        
        self.para1 = '  ___'
        self.para2 = " /___\\"
        self.para3 = " \\   /"
        self.para4 = "  \\ /"
        self.parachute = f"{self.para1}\n{self.para2}\n{self.para3}\n{self.para4}"
    

        self.man1 = "   o"
        self.man2 = "  /|\ "
        self.man3 = "  / \ "
        self.man4 = ' '
        self.man5 = "^^^^^^^"
        self.man = f"{self.man1}\n{self.man2}\n{self.man3}\n{self.man4}\n{self.man5}"
        self.lastman = "   x"

        self.parachute_exist = True
        self.size = 4
        

    def get_size(self):   
        self.size = self.size - 1   


    def set_parachute(self):
        if self.size == 4:
            self.parachute = f"{self.para1}\n{self.para2}\n{self.para3}\n{self.para4}"
        elif self.size == 3:
            self.parachute = f"{self.para2}\n{self.para3}\n{self.para4}" 
        elif self.size == 2:
            self.parachute = f"{self.para3}\n{self.para4}" 
        elif self.size == 1:
            self.parachute = f"{self.para4}" 
        elif self.size == 0:
            self.parachute = ''

        return self.parachute    

    def set_man(self):
        if self.size == 0:
            self.man = f"{self.lastman}\n{self.man2}\n{self.man3}\n{self.man4}\n{self.man5}" 
        else:
            self.man = f"{self.man1}\n{self.man2}\n{self.man3}\n{self.man4}\n{self.man5}"

        return self.man  


    def has_parachute(self):
        if self.parachute != '':
            return True       
