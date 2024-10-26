money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0 # Количество месяцев, которое можно протянуть без долгов
while money_capital > 0:
    money_capital = money_capital - (spend - salary)
    if money_capital < 0:
        break
    spend *= 1 + increase
    months += 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print(f"Количество месяцев, которое можно протянуть без долгов: {months}")
