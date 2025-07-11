"""
Here are the three burger choices:
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger
    Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink
Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order	
Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert
"""

opcao1 = int(input("""here are the three burguer choices
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger"""))
if opcao1 == 1 : 
    totalcalories = 461
elif opcao1 == 2:
    totalcalories= 431
elif opcao1==3:
    totalcalories =420
else :
    totalcalories =0

opcao2 = int(input("""Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink"""))
if opcao2 == 1 : 
    totalcalories = totalcalories + 130
elif opcao2 == 2:
    totalcalories= totalcalories +160
elif opcao2==3:
    totalcalories = totalcalories +118
else :
    totalcalories = totalcalories + 0

opcao3 = int(input("""Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order"""))
if opcao3 == 1 : 
    totalcalories = totalcalories + 100
elif opcao3 == 2:
    totalcalories= totalcalories +57
elif opcao3==3:
    totalcalories = totalcalories +70
else :
    totalcalories = totalcalories + 0

opcao4 = int(input("""Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert"""))
if opcao4== 1 : 
    totalcalories = totalcalories + 167
elif opcao4 == 2:
    totalcalories= totalcalories +266
elif opcao4==3:
    totalcalories = totalcalories +75
else :
    totalcalories = totalcalories + 0

print(totalcalories)
