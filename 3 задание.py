import csv

with open('products.csv', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    answer = list(reader)[1::]
    s = ''
    while s != 'молоко':
        s = input()
        d = set()
        minn = 100000000
        if s == 'молоко':
            break
        for i in range(len(answer)):
            if answer[i][0] == s:
                d.add(answer[i][1])
        if len(d) == 0:
            print('Такой категории не существует в нашей БД')
        else:
            for j in d:
                count = 0
                for t in range(len(answer)):
                    if answer[t][1] == j:
                        count += float(answer[t][4])
                if count < minn:
                    product = j
                    minn = count
            print('В категории:', s, 'товар:', product, 'был куплен', minn, 'раз')

