#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print((a), '+', (b), '= ', f'{add(a, b)}')
    print((a), '-', (b), '= ', f'{sub(a, b)}')
    print((a), '*', (b), '= ', f'{mul(a, b)}')
    print((a), '/', (b), '= ', f'{div(a, b)}')
    