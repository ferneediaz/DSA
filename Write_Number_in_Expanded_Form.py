def expanded_form(num):
    result = []

    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))

    return ' + '.join(result[::-1])

# Test the function with specific examples
print(expanded_form(12))    # Should print '10 + 2'
print(expanded_form(42))    # Should print '40 + 2'
print(expanded_form(70304)) # Should print '70000 + 300 + 4'
