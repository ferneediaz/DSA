def rev_rot(strng, sz):
    if sz <= 0:
        return ''
    elif len(strng) == 0:
        return ''
    if sz > len(strng):
        return ''
    
    chunks = []
    for i in range(0, len(strng), sz):
        chunk = strng[i:i+sz]
        if len(chunk) == sz:
            chunks.append(chunk)
    
    # Process each chunk
    processed_chunks = []
    for chunk in chunks:
        digit_sum = sum(int(digit) for digit in chunk)
        if digit_sum % 2 == 0:
            processed_chunks.append(chunk[::-1])
        else:
            processed_chunks.append(chunk[1:] + chunk[0])
    
    # Combine chunks
    return ''.join(processed_chunks)