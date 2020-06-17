car_list = ['AB1234', 'CD5678', 'EF981', 'CH234', 'JK567', 'LM8981']
odd_days = ['MO', 'WE', 'FR']
even_days = ['TU', 'TH', 'SA']
Accept_Cars = []
day = input("Please, enter your number: ")
for car in car_list:
    num = int(car[-1])
    if day in odd_days and num%2 != 0:
        Accept_Cars.append(car)
    elif day in even_days and num%2 == 0:
        Accept_Cars.append(car)
    elif day == 'SU':
        Accept_Cars.append(car)
print(*Accept_Cars, sep='\n')
