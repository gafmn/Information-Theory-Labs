input_list = [['a', 0.6], ['b', 0.2], ['c', 0.1], ['d', 0.1]]

# We want to encode: abcd


def calculate_ranks(prob):
    prob[0].append(0)
    prob[0].append(prob[0][1])
    if len(prob) > 1:
        for i in range(1, len(prob)):
            prob[i].append(prob[i-1][3])
            prob[i].append(prob[i-1][3] + prob[i][1])
    return prob


def recalculate_ranks(part, ranks):
    start = part[2]
    end = part[3]

    ranks[0][2] = start
    ranks[0][3] = start + ranks[0][1]*(end-start)

    for i in range(1, len(ranks)):
        ranks[i][2] = ranks[i-1][3]
        ranks[i][3] = ranks[i-1][3] + ranks[i][1]*(end-start)
    return ranks


def encoding(input_list, code):
    temp = calculate_ranks(input_list)
    for ch in code:
        for item in temp:
            if ch in item:
                temp = recalculate_ranks(item, temp)
    last_ch = code[len(code) - 1]
    print(last_ch)
    for item in temp:
        if last_ch in item:
            print("The range: (", item[2], ", ", item[3], ")")


if __name__ == '__main__':
    code = 'acd'
    encoding(input_list, code)
