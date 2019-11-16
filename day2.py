from decimal import Decimal

# input meal cost, tip percent and tax percent
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

# tip formula
tip = meal_cost*(tip_percent/100)

# tax formula
tax = meal_cost*(tax_percent/100)

# round .5 up
totalCost = Decimal(meal_cost + tip + tax).quantize(Decimal('1'))

# print total Cost
print(totalCost)
