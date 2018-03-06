import pygame

from Animal import Animal
from Buttons import InformationAnimalButtons


class Barn:

    def __init__(self, limit=0):

        self.level = 1
        self.limit = limit + self.level*10
        self.animals = []
        self.price_to_upgrade = self.level * 1000.0
        self.name = "Barn"

        chicken = Animal("Chicken", "Egg", 100, 1.0, 0.8, 0.5)
        sheep = Animal("Sheep", "Wool", 200, 10.0, 8.0, 5)
        cow = Animal("Cow", "Milk", 400, 20.0, 16.0, 10.0)
        pig = Animal("Pig", "Bacon", 800, 50.0, 40.0, 25.0)
        turkey = Animal("Turkey", "Turkey's Egg", 1600, 100.0, 80.0, 50.0)
        goat = Animal("Goat", "Goat's Milk", 3200, 200.0, 160.0, 100.0)

        self.animals.append(chicken)
        self.animals.append(sheep)
        self.animals.append(cow)
        self.animals.append(pig)
        self.animals.append(turkey)
        self.animals.append(goat)

        self.button = None

    def how_many_animals(self):
        count_animals = 0
        for animal in self.animals:
            count_animals += animal.amount

        return count_animals

    def return_the_biggest_time_to_product(self):
        the_biggest_time_to_product = 0
        for animal in self.animals:
            if animal.time_to_product > the_biggest_time_to_product:
                the_biggest_time_to_product = animal.time_to_product

        return the_biggest_time_to_product

    def upgrade(self):
        self.limit = self.level*10
        self.price_to_upgrade = self.level*1000

    def view(self, shop, pos):
        while not self.handle_events_view_barn(shop):
            shop.shop_board.shops_surface.fill((0, 0, 0))

            y = 100

            for animal in self.animals:
                self.button = InformationAnimalButtons(shop, 400, y, animal.name)
                self.button.draw(shop.shop_board.shops_surface, pos, (38, 201, 108))
                y += 45

            pygame.display.flip()

    def handle_events_view_barn(self, shop):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                shop.shop_board.trd_loop = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if self.button.range_sides(pos[0], pos[1]):
                    self.button.clicked_button()

class Magazine:

    def __init__(self, barn, limit=0):

        self.barn = barn
        self.level = 1
        self.limit = limit + self.level*20
        self.price_to_upgrade = 1000.0 * self.level
        self.name = "Magazine"

    def how_many_products(self):
        count_product = 0
        for animal in self.barn.animals:
            count_product += animal.product.amount

        return count_product

    def is_full(self):
        if self.how_many_products() >= self.limit:
            return True
        else:
            return False

    def upgrade(self):
        self.limit += self.level*10
        self.price_to_upgrade = self.level * 1000
