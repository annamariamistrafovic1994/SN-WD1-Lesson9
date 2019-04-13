gorivo = int(input("Unjeti količinu goriva: "))

if (gorivo == 0):
    print("Zovi vučnu službu.")
elif (gorivo >= 1 and gorivo <= 5 ):
    print("Pronađi prvu benzinsku.")
elif (gorivo > 5 and gorivo <= 40):
    print("Još ne trebaš brinuti.")
elif (gorivo > 40):
   print("Neispravna vrijednost.")

