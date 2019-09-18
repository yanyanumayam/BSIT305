import random
import time
from datetime import date
price1 = 1000
price2 = 1000
price3 = 1000
price4 = 800
##main menu lotto
def main_lotto():
    price1 = 1000
    price2 = 1000
    price3 = 1000
    price4 = 800
    
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    SixFourtyTwo_lot = random.sample(range(1,42),6)
    SixFourtyFive_lot = random.sample(range(1,45),6)
    SixFourtyNine_lot = random.sample(range(1,49),6)
    Lucky3_lot = random.sample(range(1,10),3)
    print("*** Welcome to IT-Lotto ***")
    print("---------------------------")
    print("Yesterday's Winning numbers")
    print("In 6/42: ",SixFourtyTwo_lot,"Price:",price1)
    print("In 6/45: ",SixFourtyFive_lot,"Price:",price2)
    print("In 6/49: ",SixFourtyNine_lot,"Price:",price3)
    print("Lucky Number: ",Lucky3_lot,"Price:",price4)
    print("---------------------------")
    print("Today's Date:" ,d2)
    print("---------------------------")
    print("SELECT PLAYING MODE:")
    print("1 - 6/42 Lotto")
    print("2 - 6/45 Lotto")
    print("3 - 6/49 Lotto")
    print("4 - Lucky 3 Number!")

def second_lotto():
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    SixFourtyTwo_lot = random.sample(range(1,42),6)
    SixFourtyFive_lot = random.sample(range(1,45),6)
    SixFourtyNine_lot = random.sample(range(1,49),6)
    Lucky3_lot = random.sample(range(1,10),3)
    print("*** Welcome to IT-Lotto ***")
    print("---------------------------")
    print("Yesterday's Winning numbers")
    print("In 6/42: ",SixFourtyTwo_lot,"Price:",price1)
    print("In 6/45: ",SixFourtyFive_lot,"Price:",price2)
    print("In 6/49: ",SixFourtyNine_lot,"Price:",price3)
    print("Lucky Number: ",Lucky3_lot,"Price:",price4)
    print("---------------------------")
    print("Today's Date:" ,d2)
    print("---------------------------")
    print("SELECT PLAYING MODE:")
    print("1 - 6/42 Lotto")
    print("2 - 6/45 Lotto")
    print("3 - 6/49 Lotto")
    print("4 - Lucky 3 Number!")
    
    
    
##generator lotto number
    
def two_lotto():
    integer = []
    for number in range(1,7):
        integer.append(random.randint(1,42))
    return integer

def five_lotto():
    integer = []
    for number in range(1,7):
        integer.append(random.randint(1,45))
    return integer

def nine_lotto():
    integer = []
    for number in range(1,7):
        integer.append(random.randint(1,49))
    return integer

def ten_lotto():
    integer = []
    for number in range(1,4):
        integer.append(random.randint(1,10))
    return integer

##Answering lotto ticket

def two_lotto_ans ():
    lottolist =  []
    numadd = 1
    print("------------6/42 Lotto-------------")
    while(len(lottolist) <6):
          picknum = int(input("Enter number " +str(numadd)+" of 6: "))
          numadd += 1
          if(picknum not in lottolist):
              lottolist.append(picknum)
              
              if (picknum >= 43):
                lottolist.pop()
                print("the number is above 42, try again ")
                numadd -= 1
                
              elif (picknum < 1):
                numadd -= 1
                lottolist.pop()
                print("the number is negative, try again ")
                
          else:
              print(" the number is duplicated, tr again ")
              numadd -=1
    
    ##checking lotto                
    rightnumber = 0
    for number in two_lotto():
        for mynumber in lottolist:
            number = 1
            mynumber = 1
            rightnumber = 0
            if(number == mynumber):
               rightnumber += 1
             
             
    print ("You have " + str(rightnumber)+ " right number")
    print("Youre lotto number list: ", lottolist )
    print("The lottory numbers: ",two_lotto())


def five_lotto_ans ():
    lottolist =  []
    numadd = 1
    print("------------6/45 Lotto-------------")
    while(len(lottolist) <6):
          picknum = int(input("Enter number " +str(numadd)+" of 6: "))
          numadd += 1
          if(picknum not in lottolist):
              lottolist.append(picknum)
              
              if (picknum >= 46):
                lottolist.pop()
                print("the number is above 45, try again ")
                numadd -= 1
                
              elif (picknum < 1):
                numadd -= 1
                lottolist.pop()
                print("the number is negative, try again ")
                
          else:
              print(" the number is duplicated, tr again ")
              numadd -=1
    
    ##checking lotto                
    rightnumber = 0
    for number in five_lotto():
        for mynumber in lottolist:
            number = 1
            mynumber = 1
            rightnumber = 0
            if(number == mynumber):
               rightnumber += 1
             
    print ("You have " + str(rightnumber)+ " right number")
    print("Youre lotto number list: ", lottolist )
    print("The lottory numbers: ",five_lotto())


def nine_lotto_ans ():
    lottolist =  []
    numadd = 1
    print("------------6/49 Lotto-------------")
    while(len(lottolist) <6):
          picknum = int(input("Enter number " +str(numadd)+" of 6: "))
          numadd += 1
          if(picknum not in lottolist):
              lottolist.append(picknum)
              
              if (picknum >= 50):
                lottolist.pop()
                print("the number is above 45, try again ")
                numadd -= 1
                
              elif (picknum < 1):
                numadd -= 1
                lottolist.pop()
                print("the number is negative, try again ")
                
          else:
              print(" the number is duplicated, try again ")
              numadd -=1
    
    ##checking lotto                
    for number in nine_lotto():
        for mynumber in lottolist:
            number = 1
            mynumber = 1
            rightnumber = 0
            if(number == mynumber):
               rightnumber += 1
             
    print ("You have " + str(rightnumber)+ " right number")
    print("Youre lotto number list: ", lottolist )
    print("The lottory numbers: ",nine_lotto())

def ten_lotto_ans ():
    lottolist =  []
    numadd = 1
    print("------------Lucky 3 Number-------------")
    while(len(lottolist) <3):
          picknum = int(input("Enter number " +str(numadd)+" of 3: "))
          numadd += 1
          if(picknum not in lottolist):
              lottolist.append(picknum)
              
              if (picknum >= 11):
                lottolist.pop()
                print("the number is above 10, try again ")
                numadd -= 1
                
              elif (picknum < 1):
                numadd -= 1
                lottolist.pop()
                print("the number is negative or zero, try again ")
                
            
                
          else:
              print(" the number is duplicated, try again ")
              numadd -=1
    
    ##checking lotto                
    for number in ten_lotto():
        for mynumber in lottolist:
            number = 1
            mynumber = 1
            rightnumber = 0
            if(number == mynumber):
                rightnumber += 1
             
    print ("You have " + str(rightnumber)+ " right number")
    print("Youre lotto number list: ", lottolist )
    print("The lottory numbers: ",ten_lotto())
    
## Main class 
main_lotto()
choose = input("Choose: ")
lottolist =  []
numadd = 1

while True:
    if choose == "1":
        two_lotto_ans ()

    elif choose == "2":
        five_lotto_ans ()
        
    elif choose == "3":
        nine_lotto_ans ()

    elif choose == "4":
        ten_lotto_ans ()
    else:
        print("invalid input")
        choose = input("Choose: ")
        continue
       
##decision
    decision = str(input("DO YOU WANT TO PLAY AGAIN ? [y,yes] or [no]"))
    if decision == "yes" or decision == "y":
        price1 = price1 + 1000
        price2 = price2 + 2000
        price3 = price3 + 3000
        price4 = price4 + 4000
        
        second_lotto()
        choose = input("Choose: ")
        lottolist =  []
        numadd = 1
        
        
        continue
    elif decision == "no" or decision =="n":
        break
    else:
        print("Invalid letter")
        decision = str(input("DO YOU WANT TO PLAY AGAIN ? [yes] or [no]"))
        continue 
