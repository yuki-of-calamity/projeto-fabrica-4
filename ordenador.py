boi1 = input ("digite o nome do boi 1 ")
peso1 =float(input(f"digie o peso do {boi1}"))
boi2 = input ("digite o nome do boi 2 ")
peso2 =float(input(f"digie o peso do {boi2}"))
boi3 = input ("digite o nome do boi 3 ")
peso3 =float(input(f"digie o peso do {boi3}"))

if peso1 > peso2 and peso1 > peso3:
    if peso2 > peso3:
        print(boi1,boi2,boi3)
    else:
        print(boi1,boi3,boi2)
elif peso3 >peso1 and peso2 > peso3:
    if peso1 > peso3:
        print(boi2,boi1,boi3)
    else:
        print(boi2,boi3,boi1)    