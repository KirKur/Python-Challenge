my_list_ctrl = {1, 11, 21, 1211, 111221}
my_list = ['1']

for i in range(30):
    next_element = ''
    symbol_last = ''
    for n, symbol in enumerate(my_list[i] + '_'):
        if symbol_last == symbol:
            symbol_cnt += 1
        else:
            if n != 0:
                next_element += str(symbol_cnt) + symbol_last
            symbol_last = symbol
            symbol_cnt = 1

    my_list.append(next_element)
print (my_list)
print (len(my_list[30]))
