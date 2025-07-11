print("Game between bananas and apples :")

threepointa = int(input("3 pointers apples :"))
twopointa = int(input("2 pointers apples : "))
onepointa = int(input("1 pointers apples : "))

threepointa = threepointa * 3
twopointa = twopointa * 2

threepointb = int(input("3 pointers bananas :"))
twopointb = int(input("2 pointers bananas : "))
onepointb = int(input("1 pointers bananas : "))

threepointb = threepointb * 3
twopointb = twopointb * 2

totalapples = threepointa + twopointa + onepointa
totalbananas = threepointb+ twopointb + onepointb

if totalapples > totalbananas :
    print(f"Apples points: {totalapples}, Bananas points: {totalbananas}")
    print("Apples wins")
elif totalapples < totalbananas :
    print(f"Apples points: {totalapples}, Bananas points: {totalbananas}")
    print("Bananas wins")
else :
    print(f"Apples points: {totalapples}, Bananas points: {totalbananas}")
    print("Tie")
