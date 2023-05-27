
variable = 123


print(variable) #print variable

my_list = [1,2,3]   #define list 

for i in my_list:
    print(i)        #print list

def calculation(x):
    x += x
    return x        #function

print(calculation(15))  #call function and print

i = 0

while i<4:
    print(i)    #while loop
    i += 1

dictionary = {
            "my_json_element_1": "321", #define json 
            "my_json_element_2": "2",
            "my_json_element_3": "2"
            }
print(dictionary["my_json_element_1"]) #print json value

print(lambda x: x*x) #lambda usage




