def max_101(number1,number2):
    if (number1>number2):
        return number1
    else:
        return number2

def max_of_three(n1, n2, n3):
    if (float(n1)>float(n2) and float(n1)>float(n3)):
        return n1
    elif (float(n2)>float(n1) and float(n2)>float(n3)):
        return n2  
    elif (float(n3)>float(n1) and float(n3)>float(n2)):
        return n3 

def rental_late_fee(number_of_days):
    if int(number_of_days)<=0:
        return 0
    elif int(number_of_days)<=9:
        return 5
    elif int(number_of_days)<=15:
        return 7
    elif int(number_of_days)<=24:
        return 19
    elif int(number_of_days)>24:
        return 100
