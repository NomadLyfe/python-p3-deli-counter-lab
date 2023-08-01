def line(line):
    if line == []:
        print("The line is currently empty.")
    else:
        print('The line is currently:', end='')
        for index, person in enumerate(line, 1):
            print(f' {index}. {person}', end='')
        print('\n', end='')

def take_a_number(line, name):
    line.append(name)
    print(f'Welcome, {name}. You are number {len(line)} in line.')

def now_serving(line):
    if line == []:
        print('There is nobody waiting to be served!')
    else:
        print(f'Currently serving {line[0]}.')
        del line[0]