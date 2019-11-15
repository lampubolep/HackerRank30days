from decimal import Decimal

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
#solve(meal_cost, tip_percent, tax_percent)

tip = meal_cost*(tip_percent/100)

tax = meal_cost*(tax_percent/100)

totalCost = Decimal(meal_cost + tip + tax).quantize(Decimal('1'))

print(totalCost)
