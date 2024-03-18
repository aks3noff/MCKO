import csv

with open('products.csv', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    answer = list(reader)[1::]
    for i in range(len(answer)):
        promo = (answer[i][1][0] + answer[i][1][1]).upper() + (answer[i][2][0] + answer[i][2][1]) + (answer[i][1][-1] + answer[i][1][-2]).upper() + (answer[i][2][4] + answer[i][2][3])
        answer[i].append(promo)

with open('product_promo.csv', 'w', newline='', encoding='utf8') as file:
    w = csv.writer(file)
    w.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    w.writerows(answer)