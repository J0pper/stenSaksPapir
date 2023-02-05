key = int(input("Skriv et tal\t"))
list = ["Bruger", "pIzza"]

def myFunction(key):
    print("Eat my", list[key-1])


if key > len(list):
    print("WRITE SMALLER NUMER BIGGUS")

else:
    myFunction(key)



