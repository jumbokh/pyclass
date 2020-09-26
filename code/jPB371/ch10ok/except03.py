def show(data, index):
    try:
        data[index]
    except IndexError as err:
        print(err)
        raise IndexError('索引超出界值')
    else:
        print(data[index])
number = [15, 20, 60, 100] #List
show(number, 0)
show(number, 1)
show(number, 2)
show(number, 3)
show(number, 4)
