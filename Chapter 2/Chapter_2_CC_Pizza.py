"""One summer evening, while curled up with her beloved Cheese-kun plushie, C.C. begins craving pizza. Although she would really like a large, extra-cheesy pizza, her stomach is willing to settle for anything. Without hesitation, she snatches up Lelouch's credit card and makes a very important phone call…

C.C. will be absolutely satisfied if the pizza she gets has a width of 3 units and an extra-cheesiness of at least 95 % .
C.C. will be fairly satisfied if the pizza she gets has a width of 1 unit and an extra-cheesiness of at most 50 % .
C.C. will be very satisfied with any other pizza she receives.

Input Specification

The first line of input will contain a single integer W ( 1 ≤ W ≤ 3 ) , denoting the width of the pizza C.C. receives.

The second line of input will contain another integer C ( 0 ≤ C ≤ 100 ) , representing the percentage of the pizza covered in extra cheese.
Output Specification

A single line containing C.C.'s satisfaction with her order in the form: C.C. is M satisfied with her pizza.

Make sure your output matches this exactly, including any spacing and punctuation.

Here, M is a string describing her satisfaction, which will be one of: absolutely, fairly or very."""

width = int(input("Width of the pizza"))
cheese = int(input("Cheesiness of the pizza"))

if width == 3 and cheese >= 95 :
    word = "Absolutely"
elif width == 1 and cheese <= 50 :
    word = "fairly"
else :
    word = "very"
print(f"C.C. is {word} satisfied with her pizza.")