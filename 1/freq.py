total_freq = 0

with open('input') as file:
    for item in file.readlines():
        try:
            num = int(item[1:])
            if item[0] == '-':
                total_freq = total_freq - num
            else:
                total_freq = total_freq + num
        except ValueError as ex:
            print('{} {}'.format(item, ex))

print(total_freq)

