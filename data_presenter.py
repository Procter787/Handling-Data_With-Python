data_presenter = open('CupcakeInvoices.csv')

#for line in data_presenter:
    #print(line)

#for line in data_presenter:
    #values = line.split(',')
    #print(values[2])


#for line in data_presenter:
    #values = line.split(',')
    #total = int(values[3]) * float(values[4])
    #print(total)

total = 0

for line in data_presenter:
    values = data.strip('\n).split(',')
    total = total + (int(values [3]) * float(values[4]))
print(total)