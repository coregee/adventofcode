def part1(digits):
    """Takes a list of digits, alternating between len(file) and len(empty-space).
    Moves the last values of stored memory into the first available values.
    Returns the checksum, which is sum(value of each memory block * its index).
    """
    disk = []
    for i in range(len(digits)):
        if i % 2 == 0:  # file
            disk.extend([i // 2] * digits[i])
        else:  # empty-space
            disk.extend([None] * digits[i])
    empty_index = 0
    fill_index = len(disk) - 1
    while empty_index < fill_index:
        while disk[empty_index] != None:
            empty_index += 1
        while disk[fill_index] == None:
            fill_index -= 1
        if empty_index < fill_index:
            disk[empty_index] = disk[fill_index]
            disk[fill_index] = None
            fill_index -= 1
    return sum(i * disk[i] for i in range(len(disk)) if disk[i] is not None)


def part2(digits):
    disk = []
    for i in range(len(digits)):
        if i % 2 == 0:  # file (id, length)
            disk.append((i//2, digits[i]))
        else:  # empty-space (None, length)
            disk.append((None, digits[i]))
    fill_index = len(disk) - 1
    while fill_index >= 0:
        if disk[fill_index][0] == None:
            fill_index -= 1
        length = disk[fill_index][1]
        # Find first gap from left
        for i in range(fill_index):
            if disk[i][0] == None and disk[i][1] >= length:
                space = disk[i][1]
                disk[i] = disk[fill_index]
                disk[fill_index] = (None, length) # we don't need to worry about joining these
                # If space is left over, add it in and adjust our pointer
                if space > length:
                    disk.insert(i + 1, (None, space - length))
                    fill_index += 1
                break
        fill_index -= 1
    i = 0
    checksum = 0
    for data in disk:
        id = data[0]
        length = data[1]
        if id:
            checksum += sum([(i + j) * id for j in range(length)])
        i += length
    return checksum


if __name__ == '__main__':
    with open('09-input.txt', 'r') as input:
        digits = [int(x) for row in input for x in row.strip()]
    print(part1(digits))
    print(part2(digits))