def find_it(seq):
    count = 0
    for i in seq:
        if seq.count(i) % 2 != 0:
            count = i
    return count
