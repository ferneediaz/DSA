def rev_rot(strng, sz):
    if sz <= 0 or len(strng) == 0 or sz > len(strng):
        return ''

    # Split into chunks and process each chunk
    processed_chunks = [
        chunk[::-1] if sum(int(digit) for digit in chunk) % 2 == 0 else chunk[1:] + chunk[0]
        for i in range(0, len(strng), sz) if len(chunk := strng[i:i+sz]) == sz
    ]

    # Combine processed chunks into a single string
    return ''.join(processed_chunks)
