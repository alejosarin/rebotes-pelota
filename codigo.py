h = int(input("\nDame la altura de la pelota: "))
j=h/5
rebotes=0

while h>j:

    h=(-h*0.10)+h
    rebotes=rebotes+1

    
print("los revotes necesarios son "+str(rebotes))   
