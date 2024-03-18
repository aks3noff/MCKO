import csv

with open('products.csv', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    answer = list(reader)[1::]

total_summ = 0

with open('products_new.csv', 'w', newline='', encoding='utf8') as file:
    w = csv.writer(file)
    w.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    for i in range(len(answer)):
        summ = float(answer[i][3]) * float(answer[i][4])
        if answer[i][0] == 'Закуски':
            total_summ += summ
        w.writerow([answer[i][0], answer[i][1], answer[i][2], answer[i][3], answer[i][4], total_summ])
print(total_summ)

