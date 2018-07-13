def total(a=5, *numbers, **phonebook):
    print('a', a)
    
    #przechodzi przez wszystkie elementy w krotce
    for single_item in numbers:
        print('single_item', single_item)
        
    #przechodzi przez wszystkie elementy w słowniku   
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
