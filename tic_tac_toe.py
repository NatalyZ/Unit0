def new_field():
    return [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def print_field(p_field):
    print(' ', '0', '1', '2')
    for i in range(3):
        print(i, end=' ')
        print(p_field[i][0], end=' ')
        print(p_field[i][1], end=' ')
        print(p_field[i][2])

def end_game(g_field):
    if g_field[0][0] + g_field[1][1] + g_field[2][2] == 'XXX' or g_field[0][2] + g_field[1][1] + g_field[2][0] == 'XXX':
        return 'X'
    if g_field[0][0] + g_field[1][1] + g_field[2][2] == '000' or g_field[0][2] + g_field[1][1] + g_field[2][0] == '000':
        return '0'
    for i in range(3):
        if g_field[i][0] + g_field[i][1] + g_field[i][2] == 'XXX':
            return 'X'
        if g_field[i][0] + g_field[i][1] + g_field[i][2] == '000':
            return '0'
        if g_field[0][i] + g_field[1][i] + g_field[2][i] == 'XXX':
            return 'X'
        if g_field[0][i] + g_field[1][i] + g_field[2][i] == '000':
            return '0'
        if g_field[i][0] == '-' or  g_field[i][1] == '-' or g_field[i][2] == '-':
            return ''
    return 'nobody'

def next_move(m_field, n):
    if n:
        arr_xy =input('Ход крестика. Введите номер позиции. Номер строки и номер столбца через пробел: ').split()
    else:
        arr_xy = input('Ход нолика. Введите номер позиции. Номер строки и номер столбца через пробел: ').split()
    if arr_xy[0].isdigit() == arr_xy[1].isdigit() == True:
       x = int(arr_xy[0])
       y = int(arr_xy[1])
       if x in {0, 1, 2} and y in {0, 1, 2}:
           if m_field[x][y] == '-':
               if n:
                   return x, y, 'X'
               else:
                   return x, y, '0'
           else:
               print('Ошибка. Эта позиция занята!')
       else:
           print('Ошибка. Номер позиции должен быть от 0 до 2.')
    else:
        print('Ошибка. Введите два целых числа.')
    return False, False, False


field = new_field()
print_field(field)
n_step = True
while end_game(field) == '':
    a, b, step = next_move(field, n_step)
    if step:
        field[a][b] = step
        n_step = not(n_step)
    print_field(field)
print('Игра окончена! Победил:', end_game(field))