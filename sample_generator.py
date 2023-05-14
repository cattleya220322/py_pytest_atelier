# -*- coding: utf-8 -*-

def func_generator():
    """ ジェネレータ関数 """
    print('---START---')    # next()[0]
    print('next()[0]')
    yield ('return[0]')
    print('next()[1]')
    yield ('return[1]')
    print('next()[2]')
    yield ('return[2]')
    print('next()[3]')
    print('---END---')      # next()[3]
    # StopIteration


print()
print('---from func_generator---')

iter_generator = func_generator()
for n, elem in enumerate(iter_generator):
    print('--- loop', n, '---')
    print(elem)
    print('--- LOOP', n, '---')

print()
print('---from expr_generator---')

# expr that returns iter_generator
for x, y in enumerate(n*n for n in range(10)):
    print(x, ': ', y)
