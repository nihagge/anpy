


from __future__ import print_function


class Dog(object):
    def __init__(self,breed,name,fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur


sam = Dog(breed = 'huskie',name='sam',fur=False)

print(sam.breed + ' ' + sam.name)
