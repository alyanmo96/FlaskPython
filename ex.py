
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

product_list = []
with open ('item.txt', 'rt') as myfile: # Open item.txt for reading text data.
    for myline in myfile:
        index=find_str(myline, "-")
        price=int(myline[index+1:])
        name=myline[:index]
        product_list.append(name)
        product_list.append(price)

index_of_product=0
print("name     price")
for i in product_list:
    print(i,"      ", end = '')
    if index_of_product%2!=0:
        print("")
    index_of_product+=1


def get_product_ptice(product):
    find_it=-1
    for i in product_list:
        if find_it == 1:
            return i
        if product==i:
            find_it=1
    return 0

user_answer=""
user_cart_total_price=0
f = open("people_buy.txt", "a")
while user_answer!="no":
    user_choose_item = str(input("select item you want to buy:\n"))
    f.write(user_choose_item)
    f.write("\n")
    user_cart_total_price+=get_product_ptice(user_choose_item)
    user_answer=str(input("do you want to buy more item {yes/no}:\n"))
f.close()

print("Total price: ",user_cart_total_price)
user_answer = str(input("do you want to submit a review of the supermarket {yes/no}:\n"))
if user_answer=="yes":
    new_product = str(input("Propose new items:\n"))
    Submit_a_comment=str(input("Submit a comment:\n"))
    rate=str(input("Rate the supermarket out of 5:\n"))

f = open("client.txt", "a")
f.write(new_product)
f.write("\n")
f.write(Submit_a_comment)
f.write("\n")
f.write(rate)
f.write("\n")
f.close()

def clients_feedback():
    #open and read the file after the appending:
    f = open("client.txt", "r")
    print(f.read())

clients_feedback()

#/////////////////////////////                  P                 /////////////////////////////
#/////////////////////////////                  A                 /////////////////////////////
#/////////////////////////////                  R                 /////////////////////////////
#/////////////////////////////                  T                 /////////////////////////////

#/////////////////////////////                  T                 /////////////////////////////
#/////////////////////////////                  W                 /////////////////////////////
#/////////////////////////////                  O                 /////////////////////////////

def remove_random_characters(word):
    alphanumeric = ""
    for character in word:
        if character.isalnum():
            alphanumeric += character
    return alphanumeric

def remove_letters(txt):
    count_of_remove_indexes=0
    for i in txt:
        if count_of_remove_indexes>=6:
            break
        if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
            txt = txt.replace(i, '')
            count_of_remove_indexes+=1
    return txt

def f(txt):
    txt = remove_letters(txt)
    txt = txt[::-1]
    txt = remove_letters(txt)
    txt = txt[::-1]
    return txt

file1 = open('items_hacked.txt', 'r')
Lines = file1.readlines()
count = 0
txt=""
tt=""
random_str=""
# Strips the newline character
for line in Lines:
    ff=line.strip()
    tt = ff[::-1]
    tt=remove_random_characters(tt)
    tt=f(tt)
    txt+=remove_random_characters(tt)
print(txt)











