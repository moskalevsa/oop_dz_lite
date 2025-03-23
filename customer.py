class Customer:
    """Класс, представляющий клиента.
       Атрибуты:
        - name (имя клиента)
        - orders (список заказов клиента).
        Конструктор __init__:
        инициализирует объект Customer с двумя атрибутами: name (полное имя клиента)
        и orders (список заказов клиента, возможно пустой).
       Свойство client_name для смены полного имени клиента.
       Методы:
        - add_order для пополнения списка заказов клиента параметр - список добавляемых заказов
        - del_order для удаления заказов из списка заказов клиента параметр - список удаляемых заказов

    """
    def __init__(self, name: str, orders: list):
        self.__name = name
        self.__orders = orders
        
    #свойство-геттер name
    @property
    def name(self):
        return self.__name
    
    # свойство-сеттер
    @name.setter
    def name(self, name):
        self.__code = name  
        
    # добавление списка товаров в заказ
    def add_order (self, add_orders: list):
        self.__orders.extend(add_orders)   
    
    #Удаление списка товаров из заказа 
    def del_order (self, del_orders: list):
        for order in del_orders:
            if order in self.__orders:
                self.__orders.remove(order)     
    
    # Получение списка товаров заказа
    def get_orders(self):
        return self.__orders    
    
    def __str__(self):
        return f'Клиент:\n - полное имя клиента: -  {self.__name},\n - Количество заказов: {len(self.__orders)}'
    
    