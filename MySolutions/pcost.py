with open('../Data/portfolio.dat', 'r') as f:
    cost = 0
    for line in f:
        fields = line.split(' ')
        price = float(fields[2])
        number = int(fields[1])
        cost += price * number

print('Total cost:', cost)



    