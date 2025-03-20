class Product:
    """
    Класс, представляющий товар.
    Атрибуты:
     - name (название товара),
     - price (цена товара).
     
     Конструктор инициализирует объект Product с двумя атрибутами:
      -  name (название товара),
      -  price (цена товара).
      
      Свойства:
      - name для получения и смены наименования товара,
      - price для получения и смены цены товара 
        
     Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(product1) выведет Product(name=Laptop, price=1000).
    """
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price
        
    # свойство-геттер name
    @property
    def name(self):
        return self.__name
    
    # свойство-сеттер
    @name.setter
    def name(self, name):
        self.__name = name
        
 # свойство-геттер price
    @property
    def price(self):
        return self.__price
    
    # свойство-сеттер
    @price.setter
    def price(self, price):
        self.__price = price      
        
    def __str__(self):
        return f'Товар:\n - Название товара: -  {self.__name},\n - цена: {self.__price} руб.'
    
    # Создание товаров
print('Создание товаров для заказов -----------------------------')
car_charger = Product('Car Charger 100W', 1228.0)
print(car_charger)
usb_type_C_charging = Product('Зарядка USB + Type-C', 769.0)
print(usb_type_C_charging)
fm_transmitter  = Product('FM модулятор с Bluetooth в машину', 1194.0)
print(fm_transmitter)
bluetooth_modulator = Product('модулятор блютуз в машину', 1439.0)
print(bluetooth_modulator)
laptop_work_14_SSD = Product('Ноутбук для работы SD-256GB', 15400.0)   
print(laptop_work_14_SSD)
    
        



    
    
    
    
    
    
    
    
    