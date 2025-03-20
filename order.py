from product import car_charger, usb_type_C_charging, fm_transmitter, laptop_work_14_SSD ,bluetooth_modulator 
class Order:
    """Класс, представляющий заказ.
       Атрибуты:
        - order_code код заказа,
        - product_list список товаров в заказе.
         Конструктор __init__:
        инициализирует объект ордер с  атрибутами:
        code - код заказа
        и product_list список товаров заказа, возможно пустой.
       Свойство code для получения и смены кода заказа.
       методы :
        - add_product для поплнения списка товаров заказа -  парметр сисок добавляемых товаров
        - del_product для удаления товаров из списка товаров заказа - парметр сисок удаляемых товаров      
    """ 
    def __init__(self, code: str, products: list):
        self.__code = code
        self.__poducts = products
  
# свойство-геттер code
    @property
    def code(self):
        return self.__code
    
    # свойство-сеттер
    @code.setter
    def code(self, code):
        self.__code = code  
        
    # добавление списка товаров в заказ
    def add_product (self, add_products: list):
        self.__poducts.extend(add_products)   
    
    #Удаление списка товаров из заказа 
    def del_product (self, del_products: list):
        for prd in del_products:
            if prd in self.__poducts:
                self.__poducts.remove(prd)     
    
    # Получение списка товаров заказа
    def get_products(self):
        return self.__poducts    
    
    def __str__(self):
        return f'Заказ:\n - код заказа: -  {self.__code},\n - Количество товаров: {len(self.__poducts)}'
    
    #Список заказов
print('СОздание заказов ------------')
#Заказ №1
order_1 = Order ('a+106z', [car_charger, usb_type_C_charging])
print('Создание первого заказа ---------------------------------------')
print(order_1)
#Товары заказа
print('Первый товар заказа')
print(order_1.get_products()[0])
#Добавление товаров в заказ
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
    