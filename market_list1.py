print('Это мой список покупок')
market_list = []

# Заполнение списка покупок
print("Добавьте продукты в список. Для завершения введите пустую строку.")
while True:
    item = input('Введите название продукта: ')
    if not item.strip():  # Проверяем, если введена пустая строка
        break
    market_list.append(item)
    print('Ваш список покупок выглядит так:', market_list)

print('Список покупок завершен:', market_list)

# Удаление продуктов из списка
print('Если вы купили какой-либо продукт, введите команду "delete" чтобы удалить его из списка. Для завершения введите "stop".')

while True:
    action = input().lower()
    if action == 'delete':
        item_name = input('Введите продукт, который хотите удалить из списка: ').lower()
        if item_name in market_list:
            market_list.remove(item_name)
            print('Продукт "{}" удален из списка'.format(item_name))
            print('Ваш список имеет следующий вид:', market_list)
        else:
            print('Продукт "{}" не найден в списке.'.format(item_name))
    elif action == 'stop':
        break
    else:
        print('Неверная команда')