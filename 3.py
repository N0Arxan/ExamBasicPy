maxim = int(input("enter a max: "))
minim = int(input("enter a min: ")) 
maxim_dins_rango = minim
num = int(input("enter a num: ")) 
while num != -1 :
     
     if minim<num<maxim:
         
         if num>=maxim_dins_rango:
            maxim_dins_rango = num
        
     num = int(input("enter a num"))

print(maxim_dins_rango)