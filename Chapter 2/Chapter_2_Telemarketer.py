"""In this problem, we’ll assume that phone numbers are four digits. A phone
number belongs to a telemarketer if its four digits satisfy all three of the fol-
lowing properties:
* The first digit is 8 or 9.
* The fourth digit is 8 or 9.
* The second and third digits are the same.
For example, a phone number whose four digits are 8119 belongs to a
telemarketer.
Determine whether a phone number belongs to a telemarketer, and in-
dicate whether we should answer the phone or ignore it.
Input
There are four lines of input. These lines give the first, second, third, and
fourth digits of the phone number, respectively. Each digit is an integer be-
tween 0 and 9.
Making Decisions 37
Output
If the phone number belongs to a telemarketer, output ignore; otherwise,
output answer."""

numeroum = int(input("First number? "))
numerodois = int(input("Second number? "))
numerotres = int(input("Third number? "))
numeroquatro = int(input("Fourth number? "))
if numeroum == 8 or numeroum ==9 :
    if numeroquatro == 8 or numeroquatro ==9 :
        if numerodois ==numerotres :
            print("ignore")
        else :
            print("answer")
    else :
        print("answer")
else :
    print("answer")

numbertelemarketer = input("Choose an option (1-3): ").strip()

numbertelemarketer = [int(c) for c in numbertelemarketer]
print("You entered:", numbertelemarketer[0])
print(numbertelemarketer[1])

for i in range(len(numbertelemarketer)) :
    print(i)
    if numbertelemarketer[i] == 8 or numbertelemarketer[i] == 9:
        if numbertelemarketer[3] == 8 or numbertelemarketer[3] == 9:
            if numbertelemarketer[1] == numbertelemarketer[2]:
                print("ignore")
            else:
                print("answer")
        else:
            print("answer")