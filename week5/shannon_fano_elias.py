import math

input_list = [['a', 0.25], ['b', 0.25], ['c', 0.20], ['d', 0.15], ['e', 0.15]]
code = '0001'

message = ['100', '100', '0001']
delta = 0.00000001
hex2bin = dict('{:x} {:04b}'.format(x, x).split() for x in range(16))


def calculate_cum_fun(input_list):
    working = input_list
    working[0].append(working[0][1])
    last_item = len(working)
    for i in range(1, last_item):
        cum_val = working[i][1] + working[i-1][2]
        working[i].append(cum_val)
    return working


def calculate_modif_cum_fun(d):
    working = input_list
    for item in working:
        modif = item[2] - item[1]/2 + delta
        item.append(modif)
    return working


def transform_to_binary(number, places):

    whole, dec = str(number).split(".")

    whole = int(whole)
    dec = int(dec)

    res = bin(whole).lstrip("0b") + "."

    for x in range(places):

        whole, dec = str((decimal_converter(dec)) * 2).split(".")

        dec = int(dec)

        res += whole

    return res


def decimal_converter(num):
    while num > 1:
        num /= 10
    return num


def transform_to_dec(binary):
    div, mod = binary.split('.')
    whole = 0
    fractional = 0
    for i in range(len(div)):
        whole = whole + (int)(div[i])*(2**i)
    for i in range(len(mod)):
        fractional = fractional + (int)(mod[i])*(2**(-i - 1))
    return whole + fractional


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return (math.ceil(n * multiplier) / multiplier)


def calculate_length(prob):
    return (int)(round_up(math.log(1/prob, 2)) + 1)


def preprocessing(code):
    return '0.' + code


def encoding(input_list):
    working = []
    working = input_list
    print(working)
    working = calculate_cum_fun(working)
    working = calculate_modif_cum_fun(working)
    print(working)

    for item in working:
        length = calculate_length(item[1])
        binary = transform_to_binary(item[3], length)
        print(item[0], ' ', binary)


def decoding(input_list, code):
    pr = input_list
    pr = calculate_cum_fun(pr)
    f = preprocessing(code)
    f = transform_to_dec(f)
    pr = calculate_modif_cum_fun(pr)
    if f < pr[0][3] or f > pr[len(pr)-1][3]:
        if f < pr[0][3]:
            print(pr[0][0])
        else:
            print(pr[len(pr)-1][0])
    else:
        for i in range(len(pr)-1):
            if pr[i][3] < f and pr[i+1][3] > f:
                if abs(pr[i][3] - f) <= abs(pr[i+1][3] - f):
                    print(pr[i][0])
                else:
                    print(pr[i+1][0])


if __name__ == '__main__':
    encoding(input_list)
    for item in message:
        decoding(input_list, item)
