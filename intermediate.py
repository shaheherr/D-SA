#map function:
#In this example we are going to multiply each element in the lilst by 3 and add 4

def equation(n):
    return (3*n+4)

my_list = [1,2,4,5,6]
ans = map(equation,my_list)
print(list((ans)))

#lambda funtion/anonymous function
#doing the same thing by usimng lambda function
my_list1 = [3,5,3,6,5,10,13]
ans1 = map(lambda x:x+3**2,my_list1)
print(list(ans1))

#filter function:works for functions which return boolean datatype
ans3 = list(filter(lambda n:n<10,my_list1))
print(ans3)
            
#using filter and map functions together
#ans4 = map(lambda o:o+3**2,list(filter(lambda n:n<10,my_list1))) or
ans4 = map(lambda o:o+3**2,ans3)
print(list(ans4))

#list comprehension:
ans5 = [i+3**2 for i in my_list1 
        if i<10]
ans6 = [i+3**2 for c in range(2) 
        for i in my_list1 ]

print(ans5)
print(ans6)
