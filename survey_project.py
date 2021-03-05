# at least 10 questions that are interactive and the responses vary depending on user input
# bonus points for and or !not operators
# multiple datatypes (int, float, string, boolean)

def getSum(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum

print("Welcome to Fortune of the Future Survey! Please answer the following questions to unlock the secrets of your fate!!")
print()

# Please enter your First name. string. 
while True:
            fname = str(input('Please enter your first name: '))
            if fname.isalpha():
                break
            


while True: 
        lname = str(input('Pleae enter your last name: '))
        if lname.isalpha():
            break
    
print()

# Please enter your Last name. string. 

len_lname = len(lname)
len_fname = len(fname)

if len_fname > len_lname:
        print("Your first name is longer than your last name!")

elif len_lname > len_fname:
        print("Your last name is longer than your first name!")

else: 
        print("Your first and last name have the same number of letters!")


# Please enter your date of birth using number only. int. 
print()

while True:
    try:
        name_num = int(input('Please enter your date of birth:  '))
        break
    except:
        print('Numbers only please.')



print()  

magic_num1 = getSum(name_num)

print(f"Your magic number is {magic_num1} {fname} {lname}")

print()

while True: 
        yes_no = str(input('Would you like to know more... type Yes or No: '))
        if yes_no.lower() == 'yes':
            break
        print("Wrong Answer!! Bahahahaha!!")

print()

# asks for current date
while True:
    try:
        date_num = int(input('Please enter current date:  '))
        break
    except:
        print('Numbers only please.')

magic_num2 = getSum(date_num)

super_magic_num = magic_num1 + magic_num2

# asks how many siblings do you have


while True:
    try:
        sibling_num = int(input('How many siblings do you have?:  '))
        break
    except:
        print('Numbers only please.')
# asks how many slices of pizza do you eat on average

while True:
    try:
        pizza_num = int(input('How many slices of pizza do you typically eat?:  '))
        break
    except:
        print('Whole Numbers only please.')

# Asks how many hours of sleep do you get each day. 
while True:
    try:
        sleep_num = int(input('How many hours do you normally sleep?:  '))
        break
    except:
        print('Whole Numbers only please.')

# Asks how many hours of python do you study each day. 
while True:
    try:
        python_num = int(input('How many hours do you study python each day?:  '))
        break
    except:
        print('Whole Numbers only please.')

print()

#final question 

while True: 
        yes_no = str(input(f"Are you ready to know your fortune {fname}??... type Yes or No: "))
        if yes_no.lower() == 'yes':
            break
        print()
        print(f'Seriously {fname}...I thought we went over this already. Try again.')
            


print()

#The variables below are a combination of the answers to the questions above
p_s_py_num = python_num + pizza_num + sleep_num
magic_num3 = super_magic_num % (sibling_num + 1)
magic_num4 = magic_num1 % (sibling_num + 1)
life = magic_num1 + magic_num2 + magic_num3 + magic_num4 + sibling_num + pizza_num + python_num + sleep_num

print(f"Your remaining life is {life}. This could be minutes, hours, days, years...who knows!")
print()
print(f"These are your lotto numbers {magic_num4}, {magic_num3}, {magic_num2}, {magic_num1}, {p_s_py_num}, ")
print()
print(f"Thank you for your time {fname}, it was nice getting to know a bit about you. Have a nice day!")