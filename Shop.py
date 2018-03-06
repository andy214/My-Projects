class Shop:

    def __init__(self, barn, wallet, magazine, shop_board):
        self.buildings = []

        self.wallet = wallet
        self.barn = barn
        self.buildings.append(self.barn)
        self.magazine = magazine
        self.buildings.append(self.magazine)
        self.shop_board = shop_board

    # def reducing_sell(self):
    #
    #     for animal in self.barn.animals:
    #         if not animal.product.count_sold_products == 0:
    #             factor = round(1 - (animal.product.count_sold_products / self.all_count_selling_products() * 0.8))
    #         else:
    #             factor = 1
    #
    #         animal.product.price_to_sell = animal.product.price_to_sell * factor

    def all_count_selling_products(self):

        number_of_all_sold_products = 0
        for animal in self.barn.animals:
            number_of_all_sold_products += animal.product.count_sold_products

        return number_of_all_sold_products

    def choose_animal(self, name_animal):
        for animal in self.barn.animals:
            if animal.name == name_animal:
                return animal

    def sell_animal(self, name_animal):

        for animal in self.barn.animals:
            if animal.name == name_animal:
                if self.barn.how_many_animals() > 1:
                    if animal.amount > 0:
                        animal.amount -= 1
                        self.wallet.gold += animal.price_to_sell
                    else:
                        text = self.shop_board.my_font.render("You don't have this animal yet", 1, (0, 0, 0))
                        self.shop_board.shops_surface.blit(text, (160, 350))
                else:
                    text = self.shop_board.my_font.render("You don't have animals to sell(Must have at least 1 animal",
                                                          1, (0, 0, 0))
                    self.shop_board.shops_surface.blit(text, (160, 350))

    def buy_animal(self, name_animal):

        for animal in self.barn.animals:
            if animal.name == name_animal:
                if self.barn.how_many_animals() < self.barn.limit:
                    if self.wallet.gold >= animal.price_to_buy:
                        animal.amount += 1
                        self.wallet.gold -= animal.price_to_buy
                    else:
                        text = self.shop_board.my_font.render("You don't have money", 1, (0, 0, 0))
                        self.shop_board.shops_surface.blit(text, (160, 350))
                else:
                    text = self.shop_board.my_font.render("You don't have space in barn", 1, (0, 0, 0))
                    self.shop_board.shops_surface.blit(text, (160, 350))

    def sell_product(self, name_animal):

        for animal in self.barn.animals:
            if animal.name == name_animal:
                if animal.product.amount > 0:
                    animal.product.amount -= 1
                    self.wallet.gold += animal.product.price_to_sell
                    # self.reducing_sell()
                    animal.product.count_sold_products += 1
                else:
                    text = self.shop_board.my_font.render("You don't have products", 1, (0, 0, 0))
                    self.shop_board.shops_surface.blit(text, (160, 350))

    def upgrades(self, building):

        if building == "Barn" and self.wallet.gold >= 100:
            self.barn.level += 1
            self.wallet.gold -= 100
            self.barn.upgrade()

        elif building == "Magazine" and self.wallet.gold >= 100:
            self.magazine.level += 1
            self.wallet.gold -= 100
            self.magazine.upgrade()
        else:
            text = self.shop_board.my_font.render("You don't have money", 1, (0, 0, 0))
            self.shop_board.shops_surface.blit(text, (160, 350))

