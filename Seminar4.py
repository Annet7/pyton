my_string = 'A *  x**2 + B *x - C = 0'
new_string = my_string.replace(' ', '').replace('=0', '').replace('*x**2', ' ').replace('*x', ' ').replace('+', '').replace('- ', ' -').split(' ')
print(f'{new_string}')