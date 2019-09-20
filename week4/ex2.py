input_seq = [['A', 3, ""], ['B', 12, ""], ['C', 10, ""], ['D', 8, ""],
         ['E', 8, ""]]


def shannon(items):
    size = len(items)
    if size > 1:
        total = 0
        for item in items:
            total = total + item[1]
        sorted_items = sorted(items, key=get_fr, reverse=True)
        # Split
        left_part = []
        right_part = []
        delim = 0
        for item in sorted_items:
            x = item[1] + delim
            if x > delim and delim < total - x:
                delim = x + delim
                left_part.append(item)
            else:
                right_part.append(item)

        # Decoding
        for item in left_part:
            item[2]  = item[2] + '0'

        for item in right_part:
            item[2]  = item[2] + '1'

        shannon(left_part)
        shannon(right_part)

        print(left_part)
        print(right_part)


def get_fr(item):
    return item[1]


if __name__ == '__main__':
    shannon(input_seq)
