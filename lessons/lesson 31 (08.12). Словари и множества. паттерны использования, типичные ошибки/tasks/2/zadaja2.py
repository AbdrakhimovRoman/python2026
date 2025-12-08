spots = [('center', 18), ('south', 9), ('center', 7), ('north', 4)]
finished = ['south']
zakaz = {}
for spot, count in spots:
    if spot in zakaz:
        zakaz[spot] += count
    else:
        zakaz[spot] = count
for finish in finished:
    zakaz.pop(finish, ' нет заказов')
print(zakaz)
selected_spot = 'center'
total_zakaz = zakaz.get(selected_spot, 0)
print(f'Итоговая сумма заказов {selected_spot}: {total_zakaz}')
