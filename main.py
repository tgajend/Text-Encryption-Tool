#Encryption tool
print('Welcome to encryption tool!')
while True:
    inp = str(input('enter text:'))
    linp = inp.lower()
    specs = '!@#$%^&*()~`/?><,.-'"{[}]|1234567890"
    if linp == '!exit':
        print('Goodbye!')
        break
    for s in specs:
        inp = inp.replace(s, '_')
    inp = inp.replace('a', '@')
    inp = inp.replace('b', '%')
    inp = inp.replace('c', '<')
    inp = inp.replace('d', ')')
    inp = inp.replace('e', '3')
    inp = inp.replace('f', '4')
    inp = inp.replace('g', '6')
    inp = inp.replace('h', '#')
    inp = inp.replace('i', '`')
    inp = inp.replace('j', '/')
    inp = inp.replace('k', '8')
    inp = inp.replace('l', '|')
    inp = inp.replace('m', '{')
    inp = inp.replace('n', '}')
    inp = inp.replace('o', '0')
    inp = inp.replace('p', '?')
    inp = inp.replace('q', '[')
    inp = inp.replace('r', ']')
    inp = inp.replace('s', '5')
    inp = inp.replace('t', '7')
    inp = inp.replace('u', '(')
    inp = inp.replace('v', '^')
    inp = inp.replace('w', '~')
    inp = inp.replace('x', '*')
    inp = inp.replace('y', '1')
    inp = inp.replace('z', '2')
#NUMBER REPLACEMENTS
#inp = inp.replace('1', 'I')
#inp = inp.replace('2', 'Z')
#inp = inp.replace('3', 'E')
#inp = inp.replace('4', 'F')
#inp = inp.replace('5', 'S')
#inp = inp.replace('6', 'G')
#inp = inp.replace('7', 'T')
#inp = inp.replace('8', 'B')
#inp = inp.replace('9', 'P')
#inp = inp.replace('0', 'O')
    print(inp)
    continue


