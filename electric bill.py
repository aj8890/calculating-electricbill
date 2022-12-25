consumeunit=float(input("ENTER THE CONSUMER UNIT:"))
if(consumeunit>1000):
    Totalcharge=consumeunit*10.20
    print("Total charge:",Totalcharge)
elif(consumeunit>800):
    Totalcharge=consumeunit*7.10
    print("Total charge:",Totalcharge)
elif(consumeunit>500):
    Totalcharge=consumeunit*5.00
    print("Total charge:",Totalcharge)
elif(consumeunit>350):
    Totalcharge=consumeunit*4.10
    print("Total charge:",Totalcharge)
elif(consumeunit>150):
    Totalcharge=consumeunit*3.20
    print("Total charge:",Totalcharge)
else:
    Totalcharge=200
    

SC=(Totalcharge*10)/100
FC=(Totalcharge*3)/100
Finalbill= Totalcharge+SC+FC
        
    
print("Final bill=",Finalbill)
