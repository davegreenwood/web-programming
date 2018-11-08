"""Solutions to Lab week 5"""
import csv

pi = 3.14159265358979323846264338327950288419716939937510


def default():
    print('This is the default output... did you enter the correct input?')


def hello():
    print('hello world')


def hello_name():
    name = input('Enter your name: ')
    print('hello', name)


def sum_two():
    a = input('Enter first number: ')
    b = input('Enter second number: ')
    s = float(a) + float(b)
    print('The sum of two numbers is:', s)


def loop_vert():
    for i in range(4, 13, 2):
        print(i)


def loop_hor():
    for i in range(4, 13, 2):
        print(i, end='')
        print(' ', end='')
    print()


def radii():
    s = 'The area of a circle with radius of {:>2d} is {:>6.2f}'
    for radius in range(1, 11):
        area = pi * radius**2
        print(s.format(radius, area))


def rad_input():
    s = 'The area of a circle with radius of {:>2d} is {:>6.2f}'
    while True:
        radius = int(input('Enter a radius value: '))
        if radius <= 0:
            break
        area = pi * radius**2
        print(s.format(radius, area))
    print('Finished')


def bmi():
    w = float(input('Enter weight in kg: '))
    h = float(input('Enter height in m: '))
    bmi = w/h**2
    s = f'{bmi:0.2f}'
    if bmi <= 20:
        print('You are underweight', s)
    elif bmi >= 30:
        print('You are obese', s)
    elif 25 < bmi < 30:
        print('You are overweight', s)
    else:
        print('You are normal', s)


def months():
    mnths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
             'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    idx = int(input('Enter month index (1-12): ')) - 1
    print(mnths[idx])


def _input_name_iter():
    print('Enter names, or type "stop" to stop:')
    return [name for name in iter(input, 'stop')]


def _input_names():
    print('Enter names, or type "stop" to stop:')
    names = []
    while True:
        name = input()
        if name == 'stop':
            break
        names.append(name)
    return names


def _read_csv(fname):
    with open(fname, 'r') as fid:
        reader = csv.reader(fid)
        a_list = next(reader)
    return a_list


def _write_csv(fname, a_list):
    """write a list of strings with comma seperation to a file """
    with open(fname, 'w') as fid:
        fid.write(','.join(a_list))
        fid.write('\n')


def input_names():
    names = _input_name_iter()
    print(','.join(sorted(names)))


def read_csv():
    fname = 'namelist.csv'
    names = _read_csv(fname)
    print(names)
    print(len(names))
    name = input('Enter name: ')
    print(names.count(name))


def write_csv():
    fname = 'out.csv'
    names = _input_names()
    _write_csv(fname, names)


def thirteen():
    fname = 'out.csv'
    names = _read_csv(fname)
    names += _input_names()
    _write_csv(fname, sorted(names))


functions = {
    0: default,
    1: hello,
    2: hello_name,
    3: sum_two,
    4: loop_vert,
    5: loop_hor,
    6: radii,
    7: rad_input,
    8: bmi,
    9: months,
    10: input_names,
    11: read_csv,
    12: write_csv,
    13: thirteen,
}


def main():
    s = input('Enter Question number (1 - 13): ')
    f = functions.get(int(s), default)
    f()


if __name__ == '__main__':
    main()
