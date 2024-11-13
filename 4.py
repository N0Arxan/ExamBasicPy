inici = input("DNA inici: ")
fin = input("DNA fin: ")
minim = int(input("enter numero minim de subseq: "))
cont = 0
contable = 0
char = ""
while char != "+":
    char=input("enter DNA(0): ")
    primer_char = char
    contA = 0
    contT = 0
    sub_cont = 0
    while char != "*" and char != "+":
        sub_cont+=1
        if char == "A":
            contA+=1
        if char == "T":
            contT+=1
        char_ant = char
        char = input("enter DNA(1): ")
    
    print(f"{char_ant} = ultima DNA ; {primer_char} = primer DNA ; {sub_cont} = numero de subseq ")
    
    cont+=1
    
    if (primer_char == inici) and (char_ant == fin) and (sub_cont >= minim):
        contable += 1
        if contA < contT :
            print(f"despres la subseq {cont} te mas T")
        elif contA > contT :
            print(f"despres la subseq {cont} te mas A")
        else:
            print(f"despres la subseq {cont} te tant A com T")

print(f"{contable/(cont-1)*100} % is analitzables")