def log_it(*args):
    path = r'/home/siwy/python/section3/labs/hw_14.txt'
    with open(path, 'a') as file:
        for i in args:
            file.write(i)
            file.write(' ')
        file.write('\n')


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')