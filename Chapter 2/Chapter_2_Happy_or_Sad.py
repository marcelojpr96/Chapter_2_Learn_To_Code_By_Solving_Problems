happyorsad = input("how are you feeling today")
happy = happyorsad.count(":-)")
sad = happyorsad.count(":-(")

if sad == happy :
    print("unsure")
elif sad > happy :
    print("sad")
elif sad<happy :
    print("happy")
else :
    print("none")