weight_list = [45,55]
total = 0
for weight in weight_list:
    total = total + weight
number_of_weights = len(weight_list)
average = total / number_of_weights
print(f'平均体重は{average}㎏です。')
