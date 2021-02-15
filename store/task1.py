customers = ['brad','jolie','johny','sooronbai','sooronbai','sadyr','sadyr','emma','sooronbai',
         'brad','almazbek','roza','roza','kurmanbek','toby','tony','robert','askar','robert','chris','chris']

# print(len(set(customers)))



def task1(request):
    import random
    list1 = random.sample(range(1,1000000),60000)
    list1_max = list1.index(max(list1))
    list1_min =list1.index(min(list1))

print(list1_max),


