Qualitat = ""
Conta_R = 0
Conta_ABC = 0
trobat = False
while Qualitat != "*" and (not trobat):
    Qualitat = input("enter qualitat : ")
    if Qualitat != "R":
        Conta_ABC+=1
    else:
        Conta_R+=1
        Qualitat = input("enter qualitat : ")
        if Qualitat == "R":
            Conta_R+=1
            Qualitat = input("enter qualitat : ")
            if Qualitat == "R":
                Conta_R+=1
                trobat = True
    
    
if trobat:
    print("Si,3Rs")
elif Conta_ABC == 1 and Conta_R == 0:
    print("seq buida")     
elif Conta_R <= Conta_ABC :
    print(f"No , {Conta_R} <= {Conta_ABC}")
elif Conta_R > Conta_ABC :
    print(f"Si , {Conta_R} > {Conta_ABC}")  
