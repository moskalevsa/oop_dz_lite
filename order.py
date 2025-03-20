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
    
