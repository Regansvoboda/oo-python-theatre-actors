from .audition import Audition

class Role:
    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append

    @property
    def auditions(self):
        return [a for a in Audition.all if a.auditions == self]
    
    @property
    def actors(self):
        return [a for a in self.auditions]
    
    @property
    def locations(self):
        return [l.location for l in self.auditions]
    
    # @classmethod
    # def silver_screen(cls):
    #     hired_li = list({h for h in })

    #     for hired in Audition.all:
    #         if hired == hired.role.character_name:
    #             hired_li = hired
    #     return hired_li


                


#    @classmethod
#     def oldest_company( cls ):
#         earliest_year = 3000
#         found_instance = 'We tried to search nothing?'

#         for company in cls.all:
#             if company.founding_year < earliest_year:
#                 earliest_year = company.founding_year
#                 found_instance = company
#         return found_instance