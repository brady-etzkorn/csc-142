from abc import ABC, abstractmethod

class Item(ABC):

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def calculate_cost(self):
        return self.price * self.quantity
    
    def __repr__(self):
     return f"{self.name}: ${self.calculate_cost()}"

class ByWeightItem(Item):
    def __init__(self, name, weight, cost_per_pound):
        self.weight = weight
        self.cost_per_pound = cost_per_pound
        super().__init__(name, cost_per_pound, weight)

    def calculate_cost(self):
        return self.weight * self.cost_per_pound

class ByQuantityItem(Item):
    def __init__(self, name, quantity, cost_each):
        self.cost_each = cost_each
        super().__init__(name, cost_each, quantity)
    
    def calculate_cost(self):
        return self.quantity * self.cost_each
    
class Grapes(ByWeightItem):
    def __init__(self, name, weight, cost_per_pound):
        super().__init__(name, weight, cost_per_pound)

class Bananas(ByWeightItem):
    def __init__(self, name, weight, cost_per_pound):
        super().__init__(name, weight, cost_per_pound)

class Oranges(ByQuantityItem):
    def __init__(self, name, quantity, cost_each):
        super().__init__(name, quantity, cost_each)

class Cantaloupes(ByQuantityItem):
    def __init__(self, name, quantity, cost_each):
        super().__init__(name, quantity, cost_each)

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_cost()
        return total
    
    def get_items(self):
        return self.items

    def __len__(self):
        return len(self.items)


order = Order()
    
item1 = Bananas("Bananas", 10, 1)
item2 = Oranges("Oranges", 5, 2)
item3 = Grapes("Grapes", 7, 2)
item4 = Cantaloupes("Cantaloupes", 2, 4)

order.add_item(item1)
order.add_item(item2)
order.add_item(item3)
order.add_item(item4)

print("Your total is $",order.calculate_total())
print(order.get_items())
print("Your order has",len(order),"items")