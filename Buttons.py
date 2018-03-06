import pygame


class Buttons:
    def __init__(self, shop):
        self.shop = shop
        self.font = pygame.font.SysFont("monospace", 8)

    def range_sides(self, x, y):
        if self.rect.x + self.rect.size[0] > x > self.rect.x and self.rect.y + self.rect.size[1] > y > self.rect.y:
            return True
        else:
            return False

    def draw(self, shop_surface, pos, color):
        pass


class BuyAnimalButton(Buttons):

    def __init__(self, shop, x, y, name_animal):
        super().__init__(shop)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.button_text = self.font.render(name_animal, 1, (0, 0, 0))
        self.price_text = self.font.render(str(self.shop.choose_animal(name_animal).price_to_buy), 1, (0, 0, 0))
        self.text_pos_x = x
        self.text_pos_y = y + 15
        self.text_price_pos_y = self.text_pos_y + 10
        self.name_animal = name_animal

    def clicked_button(self):
        self.shop.buy_animal(self.name_animal)

    def draw(self, shop_surface, pos, color):
        if self.range_sides(pos[0], pos[1]):
            pygame.draw.rect(shop_surface, (255, 255, 255), self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
            shop_surface.blit(self.price_text, (self.text_pos_x, self.text_price_pos_y))
        else:
            pygame.draw.rect(shop_surface, color, self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
            shop_surface.blit(self.price_text, (self.text_pos_x, self.text_price_pos_y))


class SellAnimalButton(Buttons):
    def __init__(self, shop, x, y, name_animal):
        super().__init__(shop)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.button_text = self.font.render(name_animal, 1, (0, 0, 0))
        self.price_text = self.font.render(str(self.shop.choose_animal(name_animal).price_to_sell), 1, (0, 0, 0))
        self.text_pos_x = x
        self.text_pos_y = y + 15
        self.text_price_pos_y = self.text_pos_y + 10
        self.name_animal = name_animal

    def clicked_button(self):
        self.shop.sell_animal(self.name_animal)

    def draw(self, shop_surface, pos, color):
        if self.range_sides(pos[0], pos[1]):
            pygame.draw.rect(shop_surface, (255, 255, 255), self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
            shop_surface.blit(self.price_text, (self.text_pos_x, self.text_price_pos_y))
        else:
            pygame.draw.rect(shop_surface, color, self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
            shop_surface.blit(self.price_text, (self.text_pos_x, self.text_price_pos_y))


class SellProductButton(Buttons):
    def __init__(self, shop, x, y, name_animal):
        super().__init__(shop)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.button_text = self.font.render(self.shop.choose_animal(name_animal).product.name, 1, (0, 0, 0))
        self.price_text = self.font.render(str(self.shop.choose_animal(name_animal).product.price_to_sell), 1, (0, 0, 0))
        self.text_pos_x = x
        self.text_pos_y = y + 15
        self.text_price_pos_y = self.text_pos_y + 10
        self.name_animal = name_animal


    def clicked_button(self):
        self.shop.sell_product(self.name_animal)

    def draw(self, shop_surface, pos, color):
        if self.range_sides(pos[0], pos[1]):
            pygame.draw.rect(shop_surface, (255, 255, 255), self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
            shop_surface.blit(self.price_text, (self.text_pos_x, self.text_price_pos_y))

        else:
            pygame.draw.rect(shop_surface, color, self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
            shop_surface.blit(self.price_text, (self.text_pos_x, self.text_price_pos_y))


class BuyUpgradeButton(Buttons):

        def __init__(self, shop, x, y, name_building):
            super().__init__(shop)
            self.rect = pygame.Rect(x, y, 40, 40)
            self.button_text = self.font.render(name_building, 1, (0, 0, 0))
            self.text_pos_x = x
            self.text_pos_y = y + 15
            self.text_price_pos_y = self.text_pos_y + 10
            self.name_building = name_building

        def clicked_button(self):
            self.shop.upgrades(self.name_building)
            print("Barn", self.shop.barn.level)
            print(self.shop.barn.limit)
            print(self.shop.wallet.gold)

            print("Magazine", self.shop.magazine.level)
            print(self.shop.magazine.limit)
            print(self.shop.wallet.gold)

        def draw(self, shop_surface, pos, color):
            if self.range_sides(pos[0], pos[1]):
                pygame.draw.rect(shop_surface, (255, 255, 255), self.rect)
                shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
                # shop_surface.blit(self.shop.choose_animal(self.name_building).price_to_upgrade,
                #                   (self.text_pos_x, self.text_price_pos_y))
            else:
                pygame.draw.rect(shop_surface, color, self.rect)
                shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
                # shop_surface.blit(self.shop.choose_animal(self.name_building).price_to_upgrade,
                #                   (self.text_pos_x, self.text_price_pos_y))


class MenuButton:

    def __init__(self, x, y, name):

        self.font = pygame.font.SysFont("monospace", 10)
        self.rect = pygame.Rect(x, y, 100, 40)
        self.button_text = self.font.render(name, 1, (0, 0, 0))
        self.text_pos_x = x
        self.text_pos_y = y + 15
        self.text_price_pos_y = self.text_pos_y + 10
        self.name = name

    def range_sides(self, x, y):
        if self.rect.x + self.rect.size[0] > x > self.rect.x and self.rect.y + self.rect.size[1] > y > self.rect.y:
            return True
        else:
            return False

    def draw(self, shop_surface, pos, color):

        if self.range_sides(pos[0], pos[1]):
            pygame.draw.rect(shop_surface, (255, 255, 255), self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
        else:
            pygame.draw.rect(shop_surface, color, self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))


class BuildingButtons(Buttons):

        def __init__(self, shop, x, y, name):
            super().__init__(shop)
            self.font = pygame.font.SysFont("monospace", 10)
            self.rect = pygame.Rect(x, y, 200, 200)
            self.button_text = self.font.render(name, 1, (0, 0, 0))
            self.text_pos_x = x
            self.text_pos_y = y + 15
            self.text_price_pos_y = self.text_pos_y + 10
            self.name = name

        def clicked_button(self, farm):
            if self.name == "Shop":
                farm.run_shop()
            for building in self.shop.buildings:
                if building.name == self.name:
                    building.view(self.shop, pygame.mouse.get_pos())

        def draw(self, shop_surface, pos, color):

            if self.range_sides(pos[0], pos[1]):
                pygame.draw.rect(shop_surface, (255, 255, 255), self.rect)
                shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
            else:
                pygame.draw.rect(shop_surface, color, self.rect)
                shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))


class InformationAnimalButtons(Buttons):

    def __init__(self, shop, x, y, name):
        super().__init__(shop)
        self.font = pygame.font.SysFont("monospace", 10)
        self.rect = pygame.Rect(x, y, 100, 40)
        self.button_text = self.font.render(name, 1, (0, 0, 0))
        self.text_pos_x = x
        self.text_pos_y = y + 15
        self.text_price_pos_y = self.text_pos_y + 10
        self.name = name

    def clicked_button(self):

        for animal in self.shop.barn.animals:
            if animal.name == self.name:
                animal.information_view()

    def draw(self, shop_surface, pos, color):

        if self.range_sides(pos[0], pos[1]):
            pygame.draw.rect(shop_surface, (255, 255, 255), self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
        else:
            pygame.draw.rect(shop_surface, color, self.rect)
            shop_surface.blit(self.button_text, (self.text_pos_x, self.text_pos_y))
