from product import Product
from order import Order
from customer import Customer

class Discount:
    """
    Класс, для хранения и применения скидок.
       Атрибуты:
        - discounts (скидки). Скидки хранятся в виде словаря где key описание скидки, values процент скидки
        Конструктор __init__:
        инициализирует объект Discount с атрибутом discounts (словарь скидок)

       методы :
        - add_discounts для поплнения словаря скидок парметр - словарь добавляемых скидок
        - del_discounts для удаления элемнтов из словаря скидок клиента парметр - сисок ключей удаляемых элементов словоря
        - get_discounts для получения словаря скидок
        - get_product_discounted_price получить цену товара по указанной скидке
        - get_order_discounted_price получить цену товаров заказа по указанной скидке
        - get_customer_discounted_price получить цену товаров заказов клиента  по указанной скидке
     
    """
   
    def __init__(self, discounts : dict):
        self.__discounts = {}
        self.__discounts.update(discounts)
        
    def add_discounts(self, add_discounts: dict):
        self.__discounts.update(add_discounts)
    
    def del_discounts(self, key_discounts: list):
        for key in key_discounts:
            if key in self.__discounts:
                self.__discounts.pop(key)
                
    def get_discounts(self):
        return self.__discounts       
    
    def get_product_discounted_price (self, product: Product, key: str):
        if key in self.__discounts:
            return product.price * self.__discounts.get(key)/100  
        
    def get_order_discounted_price(self, order: Order, key: str ):
        ord_products = order.get_products()
        ord_discount_price = 0
        if key in self.__discounts:
            discount = self.__discounts.get(key)/100
        else:
            discount = 1       
        for product in ord_products:
            ord_discount_price +=  product.price * discount
        return ord_discount_price
          
    def get_customer_discounted_price (self, customer: Customer, key: str ):
        cust_orders = customer.get_orders()
        cust_orders_discount_price = 0
        if key in self.__discounts:
            discount = self.__discounts.get(key)/100
        else:
            discount = 1
        for order in cust_orders:
            ord_products = order.get_products()           
            for product in ord_products:
                cust_orders_discount_price +=  product.price * discount
        return cust_orders_discount_price 
      
              
    
                
                
                
            
        
    
        
    