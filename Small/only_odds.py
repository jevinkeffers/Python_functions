def only_odds(lst):
    numbers_list = []
    for i in lst:
        if i % 2 != 0:
            numbers_list.append(i)
    return numbers_list

print(only_odds([4, 8 , 15, 16, 23, 42]))

#solved