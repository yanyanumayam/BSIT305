Tomodachi = []
T = 0
for count in range (0,4):
    x = input ("Enter the nickname of 4 people  ")
    Tomodachi.append(x)
print ("Press H to say Hi to each of them.")
while True:
    y = input ("")
    if y == 'H' or y == 'h':
        print("Hi" , Tomodachi[T])
        T = T + 1
        if T == 4:
            print ("Done saying Hi")
            exit()

    else:
        print ("You can only say hi")
            
    
    

    
