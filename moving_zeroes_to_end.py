def move_zeros(lst):
    zeroes = []
    ints = []
    for i in lst:
        if i == 0:
            zeroes.append(i)
        else:
            ints.append(i)
    return ints+zeroes