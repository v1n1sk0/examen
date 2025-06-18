class Product:
    def __init__(self, name: str, quantity: int, price: float):
        if quantity < 0:
            raise ValueError("Количество не может быть меньше нуля!")
        if price < 0:
            raise ValueError("Цена не может быть меньше нуля!")
        self.name = name
        self.quantity = quantity
        self.price = price

    def __add__(self, other):
        if isinstance(other, Product):
            total_quantity = self.quantity + other.quantity
            if total_quantity == 0:
                avg_price = 0
            else:
                # Средневзвешенная цена
                avg_price = ((self.price * self.quantity) + (other.price * other.quantity)) / total_quantity
            return Product(f"{self.name} + {other.name}", total_quantity, avg_price)
        raise TypeError("Можно складывать только объекты Product")

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        raise TypeError("Можно сравнивать только объекты Product")

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        raise TypeError("Можно сравнивать только объекты Product")

    def __str__(self):
        return f"{self.name} (Количество: {self.quantity}, Цена: {self.price})"


class Book(Product):
    def __init__(self, name: str, quantity: int, price: float, author: str):
        super().__init__(name, quantity, price)
        self.author = author

    def __str__(self):
        return f"Книга: {self.name}, Автор: {self.author} (Количество: {self.quantity}, Цена: {self.price})"


class Laptop(Product):
    def __init__(self, name: str, quantity: int, price: float, brand: str):
        super().__init__(name, quantity, price)
        self.brand = brand

    def __str__(self):
        return f"Ноутбук: {self.name}, Бренд: {self.brand} (Количество: {self.quantity}, Цена: {self.price})"
