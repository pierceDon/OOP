class CellPhone: 

#the initial creation of the values
    def __init__(self, man, mod, price):
        self.__manufact = man
        self.__model = mod
        self.__retail_price = price


#the set methods UPDATE the already created values
    def set_manufact(self, man):
        self.__manufact = man
        return self.__manufact

    def get_manufact(self):
        return self.__manufact
    
    def set_model(self, man):
        self.__model = man
        return self.__model

    def get_manufact(self):
        return self.__model
   
    def set_retail_price(self, price):
        self.__retail_price = price
        return self.__retail_price

    def get_retail_price(self):
        return self.__retail_price

    def __str__(self):
        return f"The {self.__manufact} {self.__model} is $" + format(self.__retail_price, ",.0f")

    
