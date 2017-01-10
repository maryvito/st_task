import re

def checked_bus_numbers():
    d = open('INPUT', 'r')
    number_of_lines = int(d.readline())
    bus_number = []
    for line in range(number_of_lines):
        bus_number.append(d.readline().strip())
    print(bus_number)
    d.close()

    f = open('OUTPUT', 'w')

    for n in range(len(bus_number)):
        if re.match('^[ABCEHKMOPTXY]\d{3}[ABCEHKMOPTXY]{2}$', bus_number[n]):
            f.writelines('Yes\n')
        else : f.write('No\n')
