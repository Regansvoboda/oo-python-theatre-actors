import ipdb
from lib import *

# Test your code below...

a1 = Actor('Zendaya')
a2 = Actor('Tom Holland')

r1 = Role('MJ')
r2 = Role('Spiderman')

au1 = Audition('loc', 'hired', r1, a1)
au2 = Audition('loc2', 'hired2', r2, a2)


print("working")

# the below line allows us to stop & try stuff!
ipdb.set_trace()