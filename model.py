class Price:

    def get_charge(self, days_rented: int) -> float:
        pass

    def get_frequent_renter_points(self, days_rented: int) -> int:
        pass

class RegulaPrice(Price):
    pass

class NewReleasePrice(Price):
    pass

class ChildrenPrice(Price):
    pass

class Book:

    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price = self.create_price(price_code)
    
    def create_price(self, price_code: int):  
        if price_code == Book.NEW_RELEASE:
            return NewReleasePrice()
        elif price_code == Book.CHILDREN:
            return ChildrenPrice()
        return RegulaPrice()
    
    def get_charge(self, days_rented: int):
        return self.price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented: int):
        return self.price.get_frequent_renter_points(days_rented)