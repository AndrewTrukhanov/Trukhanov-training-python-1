per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада:'))
deposit_list = [money /100 * per_bank for per_bank in per_cent.values()]
print(deposit_list)
print('Максимальная сумма, которую вы можете заработать —', max(deposit_list))