from .audition import Audition

class Actor:
    all = []

    def __init__(self, name):
        self.name = name
        Actor.all.append

    @property
    def auditions(self):
        return [a for a in Audition.all if a.actor == self]
    
    @property
    def roles(self):
        return [a.role for a in self.auditions]
    
    @property
    def characters(self):
        pass
   
    @property
    def paychecks(self):
        hired_list = ""
        for role in self.auditions:
            if role.hired == True:
                hired_list = role
            return hired_list


# - `Actor#paychecks` returns a list of strings with all the 
# different character names that this actor has been **hired** for.


