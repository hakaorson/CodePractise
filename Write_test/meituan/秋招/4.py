n = 5
a = 2
b = 2
cars = [[2, 4], [3, 3], [10, 8], [12, 1000], [11, 5], [1, 1]]
cars = sorted(cars, key=lambda x: x[0], reverse=True)

cur_a = cars[:a]
cur_b = cars[a:a+b]

for new_car in cars[a+b:]:
    if new_car == 0:
        
    pass
