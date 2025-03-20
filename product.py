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
    

    
        



    
    
    
    
    
    
    
    
    