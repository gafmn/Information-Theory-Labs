from copy import deepcopy

input_list = [['a', 0.6], ['b', 0.2], ['c', 0.1], ['d', 0.1]]

# We want to encode: abcd


def calculate_ranks(input_list):
    prob = []
    prob = input_list.copy()
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


def convert_to_bin(start, end):
    number = ''
    i = 1
    counter = 2**(-i)
    while True:
        i += 1
        if counter < start:
            number += '1'
            counter += 2**(-i)
        elif counter > end:
            number += '0'
            counter -= 2**(-i)
        elif counter >= start and counter <= end:
            number += '1'
            return number


def convert_to_dec(binary):
    div, mod = binary.split('.')
    whole = 0
    fractional = 0
    for i in range(len(div)):
        whole = whole + (int)(div[i])*(2**i)
    for i in range(len(mod)):
        fractional = fractional + (int)(mod[i])*(2**(-i - 1))
    return whole + fractional


def preprocessing(code):
    return '0.' + code


def encoding(input_list, code):
    temp = []
    temp = deepcopy(input_list)
    temp = calculate_ranks(temp)
    for ch in code:
        for item in temp:
            if ch in item:
                temp = recalculate_ranks(item, temp)
    last_ch = code[len(code) - 1]
    for item in temp:
        if last_ch in item:
            number = convert_to_bin(item[2], item[3])
            print(number)
            print("The range: (", item[2], ", ", item[3], ")")
            return number


def decoding(input_list, code, n):
    temp = []
    temp = deepcopy(input_list)
    temp = calculate_ranks(temp)
    code = preprocessing(code)
    dec = convert_to_dec(code)
    for item in temp:
        if dec < item[3] and dec > item[2] and n > 0:
            temp = recalculate_ranks(item, temp)
            n = n - 1
            print(item[0])


if __name__ == '__main__':
    ch = 'acd'
    code = encoding(input_list, ch)
    decoding(input_list, code, 3)
