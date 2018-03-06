class Animal:

    def __init__(self, name_animal, name_product, time_to_product, price_to_buy, price_to_sell, price_to_product_sell):

        self.name = name_animal
        self.price_to_buy = price_to_buy
        self.price_to_sell = price_to_sell
        self.product = Product(name_product, price_to_product_sell)
        self.time_to_product = time_to_product
        if self.name == "Chicken":
            self.amount = 1
        else:
            self.amount = 0

    def do_product(self, magazine, time):
        if not time % self.time_to_product:
            if self.product.amount + self.amount < magazine.limit:
                self.product.amount += self.amount
            else:
                self.product.amount = magazine.limit

    def return_info(self):

        return self.name + " " + str(self.amount)


class Product:

    def __init__(self, name_product, price_to_sell):

        self.name = name_product
        self.price_to_sell = price_to_sell
        self.amount = 0
        self.count_sold_products = 0

    def return_info(self):

        return self.name + " " + str(self.amount) + " " + str(self.price_to_sell)

