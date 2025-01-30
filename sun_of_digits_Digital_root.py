def digital_root(n):
    if n < 10:
        return n  
    digit_sum = sum(int(char) for char in str(n))  
    return digital_root(digit_sum) 
#recursion solution