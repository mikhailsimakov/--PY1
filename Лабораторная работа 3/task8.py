money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0

while money_capital + salary >= spend:
    month += 1
    money_capital = money_capital - spend + salary
    spend *= 1 + increase


print(month)
