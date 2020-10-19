
#1  Ask the user for his name, and then print a greeting message
NAME=str(input("enter you name: "))
print("hello",NAME)



#2Ask two users for their names, and then tell them who got the longest name.
name_one=str(input("enter name of the first user: "))
name_two=str(input("enter name of the second user: "))

counter__length_of_user_one = 0
counter__length_of_user_two = 0

for o in name_one: # traverse the string “educative”
    counter__length_of_user_one+=1 #increment the counter
for t in name_two: # traverse the string “educative”
    counter__length_of_user_two+=1 #increment the counter    

if  counter__length_of_user_one > counter__length_of_user_two:
    print(name_one)
elif  counter__length_of_user_one  < counter__length_of_user_two:
    print(name_two)    
else:
        print("both names are equal by the length")
    
    
    
#3Ask a user for his name, and if it starts with a vowel, greet him    
NAME=str(input("enter you name: "))
if NAME[0] in ['a','e','i','o','u']:
            print("hello",NAME)
            
#4Ask the user for his name, and tell him if the last letter is a vowel or a consonant            
NAME=str(input("enter you name: "))
last_char = NAME[-1]
if last_char[0] in ['a','e','i','o','u']:
            print("it's a vowel letter")
else:
        print("it's a consonant letter")
        

#5Ask the user for two numbers (one after the other) and then print their sum
a = int(input("enter the first number:  "))
b = int(input("enter the second number:  ") )      
result = a + b
print(result)


#6Challenge the user to print the longest sentence without any “A”, if he achieves it, tell him how many letters he wrote, else, print a fail message.
get_user_string_input = str(input("enter your string:  "))

for i in get_user_string_input:
       if i =='A':
         print("fail")
       
#7Ask the user for his full name (example: “John Doe”), and check the validity of his answer:
#The name should contain only letters.
#The name should contain only one space.
#The first letter of each name should be upper cased.       
one_space=0
NAME=input("enter you name : ")
check = NAME.isalpha()
if check == False:
    print("name contain leeters with other chars")
if NAME[0].isupper():
     print("first letter name is not an upper")

next_digit=0
for i in NAME:
    if one_space>1:
        print("there is more than one space")
    if one_space == 1 and next_digit==1:
        if i.isupper():
            print("first letter of second name is not an upper")
       
    if i.isspace() == True:    
        one_space+=1
        next_digit=1
    
    
#8Ask the user for a sentence, and then tell him how many words are in it.    
get_user_string_input = str(input("enter your string:  "))
count_of_spaces=0
for i in get_user_string_input:
       if i.isspace() == True: 
            count_of_spaces+=1
count_of_spaces+=1       
print("you enter {} words",count_of_spaces)       


#9
"""
Write a python program to get a string made of the first 2 and the last 2 chars from a given string, if the string length is less than 2, return instead the empty string.
For example: "Helloworld" output "Held", while "Sik" returns ""
"""

str_form_user=str(input("enter a word:  "))
return_str=""

counter_length_of_str= 0

for o in str_form_user: 
    counter_length_of_str+=1

print(counter_length_of_str)
if counter_length_of_str<=2:
    print("")
else:
    return_str+=str_form_user[0]
    return_str+=str_form_user[1]
    return_str+=str_form_user[-2]
    return_str+=str_form_user[-1]
print(return_str)


#10 Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then tell him how old he turnt/will turn this year.





#11




#12
""""
For Loops
Exercise (Easy)
Write a program that counts the number of element for a list, without the len function.

"""
name=['Alex','Mike','Dylan','Yossi']
count_of_element=0
for i in  name:
        count_of_element+=1
print(count_of_element)


#13        Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.

for i in range(11):
    if i !=3 and i!=6:
        print(i)
        

#14
"""
You have a list of users, and you want to remove every user that is below 16 years old.

Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.

At the end, print the final list.

Example list:
"""        
names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
index_to_remove=0
for i in names:
    below_or_not = str(input(" are you below 16 years old yes/no"))
    if below_or_not =="yes":
        names.pop(index_to_remove)
    index_to_remove+=1
print(names)        


#15Use a for loop to print the numbers from 1 to 20, inclusive.
for i in range(1,21):
     print(i)
     
     
#16
"""
Make a list of the numbers from one to one million, and then use a for loop to print the numbers.

(If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
"""     
list1 = list(range(1000001))
list1.pop(0)
print(list1)

#17 Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers .
list1 = list(range(11))
list1.pop(0)
print(min(list1))
print(max(list1))
print("Sum of elements in  list of million is :", sum(list1))


#18Write a program that returns the index of the first occurrence of an item in a list.
def return_index():
    index_of_word=0
    list = ["car", "boolean" , "chair","apple","chair","lion"]
    search_word="chair"
    
    for i in list:
        if  i == search_word:
            return index_of_word
        index_of_word+=1    
    return -1        
print(return_index())       
   

#19Write a little program that concatenate two lists together without using the + sign.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
list2.clear()
print(list1)


#20
"""
Create a board as following by using for loops:

    X
    XX
    XXX
    XXXX
    XXXXX
    XXXXXX
    XXXXX
    XXXX
    XXX
    XX
    X
"""
rows = 6
for num in range(rows):
    for i in range(num):
        print("*", end=" ")  
    print(" ")
    
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\r')


#21Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
lst = list(range(3,31,3))    

for i in lst:
    print(i)

#22Write a program that insert an item at a defined index.
list1 = [ 1, 2, 3, 4, 5, 6, 7 ]  
list1.insert(4, 10)  
print(list1) 


#23
"""

Exercise (Medium)
Here is a list of popular car manufacturers: https://pastebin.com/bkBRuvAZ
Paste it into your code, and store it in a variable.
Convert it into a list using Python (don’t do it by hand!)
Print out a message saying how many manufacturers/companies are in the list
Print the list of manufacturers in reverse/descending order (Z-A)
Using loops or list comprehension:
Find out how many manufacturers’ names have the letter ‘o’ in them.
Find out how many manufacturers’ names do not have the letter ‘i’ in them
Print the above information out with meaningful output messages.
(Bonus: There are a few duplicates in the list:
Remove these programmatically. (Hint: you can use sets to help you)
Print out the companies without duplicates, in a comma-separated list with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), and also print out a message saying how many companies are now in the list).
(Bonus: print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name)
"""

car_manufactures=[ "Abarth",
  "Alfa Romeo",
  "Aston Martin",
  "Audi",
  "Bentley",
  "BMW",
  "Bugatti",
  "Cadillac",
  "Chevrolet",
  "Chrysler",
  "Citroën",
  "Dacia",
  "Daewoo",
  "Daihatsu",
  "Dodge",
  "Donkervoort",
  "DS",
  "Ferrari",
  "Fiat",
  "Fisker",
  "Ford",
  "Honda",
  "Hummer",
  "Hyundai",
  "Infiniti",
  "Iveco",
  "Jaguar",
  "Jeep",
  "Kia",
  "KTM",
  "Lada",
  "Lamborghini",
  "Lancia",
  "Land Rover",
  "Landwind",
  "Lexus",
  "Lotus",
  "Maserati",
  "Maybach",
  "Mazda",
  "McLaren",
  "Mercedes-Benz",
  "MG",
  "Mini",
  "Mitsubishi",
  "Morgan",
  "Nissan",
  "Opel",
  "Peugeot",
  "Porsche",
  "Renault",
  "Rolls-Royce",
  "Rover",
  "Saab",
  "Seat",
  "Skoda",
  "Smart",
  "SsangYong",
  "Subaru",
  "Suzuki",
  "Tesla",
  "Toyota",
  "Volkswagen",
  "Volvo"
]

def  is_manufacture_include_the_letter_o(word):
     for i in word:
         if i=='o':
                return 1
    
def  is_manufacture_include_the_letter_i(word):
     for i in word:
         if i=='o':
                return 1   

count_of_cars_manufactures=0
for i in car_manufactures:
        count_of_cars_manufactures+=1
print("numbers of manufacturers {} ",count_of_cars_manufactures)

car_manufactures.sort()        
car_manufactures

car_manufactures.sort(reverse = True)        
car_manufactures

count_of_cars_manufactures_include_the_letter_o=0
count_of_cars_manufactures_include_the_letter_i=0
for i in car_manufactures:
     if is_manufacture_include_the_letter_o(i) == 1:
        count_of_cars_manufactures_include_the_letter_o+=1
     if is_manufacture_include_the_letter_i(i) == 1:
        count_of_cars_manufactures_include_the_letter_i+=1
        
print("numbers of manufacturers include_the_letter_o {} ",count_of_cars_manufactures_include_the_letter_o)       
print("numbers of manufacturers include_the_letter_i{} ",count_of_cars_manufactures_include_the_letter_i)       
for i in car_manufactures:
    print(i)
    
#24You have two lists, current_players and new_players, use a while loop to transfer every player from new_players to current_players.
current_players = ['Mario', 'Luigi', 'Peach']
new_players = ['Blue Toad', 'Red Toad', 'Green Toad']

length = len(new_players)
i = 0
while i < length: 
    current_players.append(i)
    i += 1     
new_players.clear()     
print(current_players)    


#25
"""
Draw the following pattern using for loops:

    *
   **
  ***
 ****
*****
"""
rows = 6
for row in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print("*", end=' ')
            num += 1
    print("")
    
#26
"""
What is the output of the following?¶
    x = ['ab', 'cd']
    for i in x:
        i.upper()
    print(x)
"""    
#nothing changes



#27
""""
What is the output of the following?¶

    x = ['ab', 'cd']
    for i in x:
        x.append(i.upper())
    print(x)
"""
#Output : run: line 1:     3 Killed                  /usr/bin/python3 script.py



#28Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
integers_list= [] 
strings_list= []  
given_list = ["apple", 444,666,"banana", "cherry",22]

for i in given_list:
     if type(i) is int:
        integers_list.append(i)
     else:
        strings_list.append(i)
 
print(integers_list)
print(strings_list)


#29
""""
Draw the following pattern using for loops:

*
**
***
****
*****
"""
rows = 6
for num in range(rows):
    for i in range(num):
        print("*", end=" ") 
    print(" ")
    
    
   




    




















