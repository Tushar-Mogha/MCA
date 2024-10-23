# Write a program to create a list of squares of numbers from 0 to n using list comprehension

n=50
res=[ x**2 for x in range(0,n) if x%2==0 ]
print(res)

# WAP that use dictionary comprehension to create a dictionary where keys are numbers and 
# values are square numbers


res2={x: x**2 for x in range(0,n) if x&2==0}
# Write a program that takes a arguement that is dictionary and returns where keys are values 
# and values are keys

def flip_dictionary(d1):
    assert isinstance(d1,dict),"Input is not a dictionary"
    flipped={ val:key for key,val in d1.items() }
    return flipped
print(f"flipped dictionary is \n { flip_dictionary(res2)}")
flip_dictionary({"1":"Tushar"})