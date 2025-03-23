from product import Product
from order import Order
from customer import Customer
from discount import Discount
from pprint import pprint

"""
1.	Создаются товары, заказы и клиенты.
2.	Демонстрируется функциональность добавления заказов к клиенту.
3.	Демонстрируется применение различных видов скидок к заказам.
4.	Проводится подсчёт общего количество заказов и общей сумму всех заказов для всех клиентов.
5.	Выводится информация о клиентах, заказах и продуктах с использованием дандер методов.   
6.  Проверяются статический метод (Discount)и методы класса (Order)
"""
# Товары
print('Товары: создание и вывод информации -----------------------------')
car_charger = Product('Car Charger 100W', 1228.0)
print(car_charger)
usb_type_C_charging = Product('Зарядка USB + Type-C', 769.0)
print(usb_type_C_charging)
print('Цены равны: ',car_charger == usb_type_C_charging)
print('цена USB < car_charger :', usb_type_C_charging < car_charger)
fm_transmitter  = Product('FM модулятор с Bluetooth в машину', 1194.0)
print(fm_transmitter)
bluetooth_modulator = Product('модулятор блютуз в машину', 1439.0)
print(bluetooth_modulator)
laptop_work_14_SSD = Product('Ноутбук для работы SD-256GB', 15400.0)   
print(laptop_work_14_SSD)

#Заказы
print('Заказы: создание, проверка функциональности и вывод информации')
#Заказ №1
order_1 = Order ('a+106z', [car_charger, usb_type_C_charging])
print('Создание первого заказа ---------------------------------------')
print(order_1)
#Товары заказа
print('Первый товар заказа')
print(order_1.get_products()[0])
#Добавление товаров в заказ
print('Проверка функциональности')
print('Добавление товаров в заказ -----------------------------')
order_1.add_product([fm_transmitter, laptop_work_14_SSD ])
print(order_1)
#Товары заказа
print('Первый товар заказа')
print(order_1.get_products()[0])
#Удаление товаров из заказа
print('Удаление товаров из заказа -----------------------------')
order_1.del_product([car_charger])
print(order_1)
#Товары заказа
print('Первый товар заказа')
print(order_1.get_products()[0])

#Заказ №2
order_2 =Order ('a+116z', [laptop_work_14_SSD, bluetooth_modulator])
print('Создание второго заказа ---------------------------------------')
print(order_2)
#Товары заказа
print('Последний товар заказа')
print(order_2.get_products()[-1])

#Заказ №3
order_3 =Order ('a+116z', [laptop_work_14_SSD, fm_transmitter, bluetooth_modulator])
print('Создание третьего заказа ---------------------------------------')
print(order_3)
#Товары заказа
print('Последний товар заказа')
print(order_3.get_products()[-1])

# Клиенты
print('Клиенты: создание, проверка функциональности и вывод информации')
#Клиент №1
customer_1 = Customer('Иванов Иван Иванович', [order_1])
print('Создание первого клиента ---------------------------------------')
print(customer_1)
#Добавление заказов клиенту
print('Проверка функциональности')
print('Добавление заказов в список заказов клиента -----------------------------')
customer_1.add_order([order_2])
print(customer_1)
#Заказы клиента
print('Последний заказ клиента')
print(customer_1.get_orders()[-1])
#Удаление товаров из заказа
print('Удаление заказов из списка заказов клиента -----------------------------')
customer_1.del_order([order_2])
print(customer_1)

#Клиент №2
customer_2 = Customer('Мишулина Ольга Александровна', [order_2, order_3])
print('Создание второго клиента ---------------------------------------')
print(customer_2)
#Товары заказа
print('Последний заказ клиента')
print(customer_2.get_orders()[-1])

# Скидки
print('Скидки: создание, проверка функциональности и вывод информации')
discount_list = {
    'сезонная скидка' : 40.0,
    'скидка по промокоду' : 30.0,
    'пенсионная скидка' : 20.0    
    }
print('Создание скидок -----------------------------------------------------')
discount = Discount(discount_list)
print(discount)
#Добавление скидок
print('Добавление скидок---------------------------------------')
add_discouns = {
     'скидка в Яузу' :  10.5,
     'скидка в Лопасню' : 20.0
     }
discount.add_discounts (add_discouns)
print(discount)
#Удаление скидок
print('Удавление скидок---------------------------------------')
key_discounts = ['пенсионная скидка', 'скидка в Лопасню']
discount.del_discounts(key_discounts)
print(discount)
# Стоимость товаров первого заказа со скидкой 'сезонная скидка'
print('Стоимость товаров первого заказа со скидкой "сезонная скидка"')
order_discont_cost_1 = discount.get_order_discounted_cost(order_1,'сезонная скидка')
print(order_1)
print(f'Стоимость товаров заказа со скидкой : {round(order_discont_cost_1,2)}')
# Стоимость товаров первого клиента со скидкой 'скидка в Яузу'
print('Стоимость товаров первого заказа со скидкой "скидка в Яузу"')
customer_discont_cost_1 = discount.get_customer_discounted_cost (customer_1, 'скидка в Яузу')
print(customer_1)
print(f'Стоимость товаров клиента со скидкой : {round(customer_discont_cost_1,2)}')
#Проверка метода класса Order для подсчета общего количества заказов для всех клиентов
print('Проверка метода класса Order для подсчета общего количества заказов для всех клиентов')
customer_list = [customer_1, customer_2]
total_number_orders = Order.get_total_number_orders(customer_list)
print (f'Общее количество заказов по клиентам = {total_number_orders}')
#Проверка метода класса Order для подсчета общей стоимости заказов для всех клиентов
print('Проверка метода класса Order для подсчета общей стоимости заказов для всех клиентов')
total_cost_order = Order.get_total_cost_orders(customer_list, discount, 'сезонная скидка')
print(f'Общая стоимость заказов всех клиентов сщ скидкой "сезонная скидка": {round(total_cost_order,2 )}')
# Проверка статического метода класса Discount для расчета цены с указанной скидкой
print('Проверка статического метода класса Discount для расчета цены с указанной скидкой')
discont_price = Discount.get_discount_price(1450.0, discount_list,'скидка по промокоду') 
print (f'цена: {1450.0} \n Скидка по промокоду: {discount_list.get('скидка по промокоду')}\n цена со скидкой: {discont_price}' )





