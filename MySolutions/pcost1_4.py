def portfolio_cost(filename:str):
    with open(filename, 'r') as f:
        cost = 0
        for line in f:
            fields = line.split(' ')
            try:
                price = float(fields[2])
                number = int(fields[1])
            except ValueError as e:
                print(f'Error: couldnt parse line: {line}')
                print(f'Reason: {e}')
                continue
            cost += price * number

    return cost

if __name__ == '__main__':
    print(portfolio_cost('../Data/portfolio3.dat'))
