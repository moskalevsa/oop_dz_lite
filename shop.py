import product
import order


#Список заказов
print('Сщздание заказов')
#Заказ №1
order_1 =order.Order ('a+106z', [product.car_charger, product.usb_type_C_charging])
print('Создание первого заказа ---------------------------------------')
print(order_1)
#Товары заказа
print('Первый товар заказа')
print(order_1.get_products()[0])
#Добавление товаров в заказ
print('Добавление товаров в заказ -----------------------------')
order_1.add_product([product.fm_transmitter, product.laptop_work_14_SSD ])
print(order_1)
#Товары заказа
print('Первый товар заказа')
print(order_1.get_products()[0])
#Удаление товаров из заказа
print('Удаление товаров из заказа -----------------------------')
order_1.del_product([product.car_charger])
print(order_1)
#Товары заказа
print('Первый товар заказа')
print(order_1.get_products()[0])

#Заказ №2
order_2 =order.Order ('a+116z', [product.laptop_work_14_SSD, product.bluetooth_modulator])
print('Создание второго заказа ---------------------------------------')
print(order_2)
#Товары заказа
print('Последний товар заказа')
print(order_2.get_products()[-1])
