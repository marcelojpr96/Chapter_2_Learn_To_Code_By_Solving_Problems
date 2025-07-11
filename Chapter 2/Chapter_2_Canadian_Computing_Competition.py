
"""
    Canadian Computing Competition: 2015 Stage 1, Junior #1

    February 18 is a special date for the CCC this year.	

    mês 2 dia 18

    Write a program that asks the user for a numerical month and numerical day of the month and then determines whether that date occurs before, after, or on February 18.

    If the date occurs before February 18, output the word Before.
    If the date occurs after February 18, output the word After.
    If the date is February 18, output the word Special.

    Input Specification

    The input consists of two integers each on a separate line. These integers represent a date in 2015 .

    The first line will contain the month, which will be an integer in the range from 1 (indicating January) to 12 (indicating December).

    The second line will contain the day of the month, which will be an integer in the range from 1 to 31 . You can assume that the day of the month will be valid for the given month.
    Output Specification

    Exactly one of Before, After, or Special will be printed on one line.
"""
mes = int(input("Insira o mês : "))
dia = int(input("Insira o dia :"))

if mes > 2 or mes == 2 and dia >18 :
    print("After")
elif mes < 2 or mes == 2 and dia <18 :
    print ("Before")
elif mes == 2 and dia == 18 :
    print("Special")