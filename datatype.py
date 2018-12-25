'''
Datatype
    immutable
        Numbers
        Strings
        Tuples

    Mutable
        Lists
        Dictionaries
        Sets
'''

'''
string1 = 'Python'
string2 = "Tutorial"

#Concatenation
print(string1 + string2)

#Repetition
print(string2 * 3)

#Slicing
print(string2[3:6])

print(string2[2:-3] )

'''
#Type Specific Method
'''
string1 = 'Python'
string2 = "Tutorial"

print(string1.count('P',0,5))
print(string1.find('on'))
print(string1.isalpha())
print(string1.upper())
print(max(string1))
print(min(string1))
'''

'''
#TUPLES
my_tup = ('Manoj','Manish','Sarita','Dilli')

#Concatination
print(my_tup+('Sonu','Sane'))

#Repetition
print(my_tup * 3)

#Slicing
print(my_tup[1:4])

#Indexing
print(my_tup[0])
'''

'''
#LISTs
my_list=['Green','Red','Blue','Yellow','Pink']
my_list.append('grey')
print(my_list)

my_list.extend(['white','black'])
print(my_list)
'''

'''
#Dictionaries
my_dict={1:'Green', 2:'Blue', 3:'Red'}

#accessing Dictionary
print(my_dict[3])
#len()
print(len(my_dict))
#key()
print(my_dict.keys())
#values()
print(my_dict.values())
#items()
print(my_dict.items())
#get()
print(my_dict.get(1))
#update()
A = {'a', 'b'}
B = {1, 2, 3}
result = A.update(B)
print('A =',A)
print('B =',B)
print('result =',result)
#pop()
print(my_dict.pop(1))
'''

#SETs
#creating sets
my_set={1,2,3,4,5,'a'}
your_set={6,7,8,9,10,'a'}
print(my_set)
print(your_set)
#union
print("Union=",my_set|your_set)
#intersection
print("Intersection=",my_set&your_set)
#difference
print("Difference=",my_set-your_set)

















