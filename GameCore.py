import pygame
import pygame.locals
from threading import Timer, Lock
from Buildings import Barn, Magazine
from Buttons import BuyAnimalButton, SellAnimalButton, SellProductButton, BuyUpgradeButton, MenuButton, \
     BuildingButtons
from Shop import Shop
from Wallet import Wallet


class Board(object):

    def __init__(self, width, height):

        self.shops_surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Farm')
        self.my_font = pygame.font.SysFont("monospace", 10)
        self.trd_loop = True


class Farm(object):

    def __init__(self, width, height):
        pygame.init()
        self.shop_board = Board(width, height)
        self.wallet = Wallet()
        self.barn = Barn()
        self.magazine = Magazine(self.barn)
        self.shop = Shop(self.barn, self.wallet, self.magazine, self.shop_board)
        self.fps_clock = pygame.time.Clock()
        self.time = 0
        buy_animal_text = self.shop_board.my_font.render("Buy Animals", 1, (255, 0, 0))
        self.shop_board.shops_surface.blit(buy_animal_text, (10, 10))

        self.buy_animal_button1 = BuyAnimalButton(self.shop, 25, 30, "Chicken")
        self.buy_animal_button2 = BuyAnimalButton(self.shop, 25, 80, "Sheep")
        self.buy_animal_button3 = BuyAnimalButton(self.shop, 25, 130, "Cow")
        self.buy_animal_button4 = BuyAnimalButton(self.shop, 25, 180, "Pig")
        self.buy_animal_button5 = BuyAnimalButton(self.shop, 25, 230, "Turkey")
        self.buy_animal_button6 = BuyAnimalButton(self.shop, 25, 280, "Goat")

        sell_animal_text = self.shop_board.my_font.render("Sell Animals", 1, (0, 255, 0))
        self.shop_board.shops_surface.blit(sell_animal_text, (80, 10))

        self.sell_animal_button1 = SellAnimalButton(self.shop, 95, 30, "Chicken")
        self.sell_animal_button2 = SellAnimalButton(self.shop, 95, 80, "Sheep")
        self.sell_animal_button3 = SellAnimalButton(self.shop, 95, 130, "Cow")
        self.sell_animal_button4 = SellAnimalButton(self.shop, 95, 180, "Pig")
        self.sell_animal_button5 = SellAnimalButton(self.shop, 95, 230, "Turkey")
        self.sell_animal_button6 = SellAnimalButton(self.shop, 95, 280, "Goat")

        sell_product_text = self.shop_board.my_font.render("Sell Products", 1, (0, 0, 255))
        self.shop_board.shops_surface.blit(sell_product_text, (160, 10))

        self.sell_product_button1 = SellProductButton(self.shop, 175, 30, "Chicken")
        self.sell_product_button2 = SellProductButton(self.shop, 175, 80, "Sheep")
        self.sell_product_button3 = SellProductButton(self.shop, 175, 130, "Cow")
        self.sell_product_button4 = SellProductButton(self.shop, 175, 180, "Pig")
        self.sell_product_button5 = SellProductButton(self.shop, 175, 230, "Turkey")
        self.sell_product_button6 = SellProductButton(self.shop, 175, 280, "Goat")

        buy_upgrades_text = self.shop_board.my_font.render("Buy Upgrades", 1, (255, 0, 255))
        self.shop_board.shops_surface.blit(buy_upgrades_text, (250, 10))

        self.buy_upgrade_button1 = BuyUpgradeButton(self.shop, 265, 30, "Barn")
        self.buy_upgrade_button2 = BuyUpgradeButton(self.shop, 265, 80, "Magazine")

        self.barn_building_button = BuildingButtons(self.shop, 50, 100, "Barn")
        self.magazine_building_button = BuildingButtons(self.shop, 260, 100, "Magazine")
        self.shop_building_button = BuildingButtons(self.shop, 470, 100, "Shop")

    def run_time(self, time=0):
        while self.shop_board.trd_loop:
            print(time)
            self.fps_clock.tick(15)
            if time % self.barn.return_the_biggest_time_to_product():
                if not self.magazine.is_full():
                    if not time % self.barn.animals[0].time_to_product:
                        self.barn.animals[0].do_product(self.magazine, self.time)
                    if not time % self.barn.animals[1].time_to_product:
                        self.barn.animals[1].do_product(self.magazine, self.time)
                    if not time % self.barn.animals[2].time_to_product:
                        self.barn.animals[2].do_product(self.magazine, self.time)
                    if not time % self.barn.animals[3].time_to_product:
                        self.barn.animals[3].do_product(self.magazine, self.time)
                    if not time % self.barn.animals[4].time_to_product:
                        self.barn.animals[4].do_product(self.magazine, self.time)
                    if not time % self.barn.animals[5].time_to_product:
                        self.barn.animals[5].do_product(self.magazine, self.time)
                else:
                    text = self.shop_board.my_font.render("Magazine is full", 1, (0, 255, 0))
                    self.shop_board.shops_surface.blit(text, (160, 300))
            else:
                time = 0
                self.time = 0
            time += 1
            self.time = time

    def run_shop(self):
        while not self.handle_events_shop():

            self.shop_board.shops_surface.fill((0, 0, 0))
            x = 10
            for animal in self.barn.animals:
                information_animals = self.shop_board.my_font.render(animal.return_info(), 1, (0, 255, 255))
                information_productions = self.shop_board.my_font.render(animal.product.return_info(), 1, (0, 255, 255))
                self.shop_board.shops_surface.blit(information_animals, (400, x))
                self.shop_board.shops_surface.blit(information_productions, (400, x + 60))
                x += 10

            wallet_information = self.shop_board.my_font.render("Wallet: " + str(self.wallet.gold), 1, (0, 255, 255))
            self.shop_board.shops_surface.blit(wallet_information, (500, 10))

            self.buy_animal_button1.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (255, 0, 0))
            self.buy_animal_button2.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (255, 0, 0))
            self.buy_animal_button3.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (255, 0, 0))
            self.buy_animal_button4.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (255, 0, 0))
            self.buy_animal_button5.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (255, 0, 0))
            self.buy_animal_button6.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (255, 0, 0))

            self.sell_animal_button1.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 255, 0))
            self.sell_animal_button2.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 255, 0))
            self.sell_animal_button3.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 255, 0))
            self.sell_animal_button4.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 255, 0))
            self.sell_animal_button5.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 255, 0))
            self.sell_animal_button6.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 255, 0))

            self.sell_product_button1.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 0, 255))
            self.sell_product_button2.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 0, 255))
            self.sell_product_button3.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 0, 255))
            self.sell_product_button4.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 0, 255))
            self.sell_product_button5.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 0, 255))
            self.sell_product_button6.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (0, 0, 255))

            self.buy_upgrade_button1.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (255, 0, 255))
            self.buy_upgrade_button2.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (255, 0, 255))

            pygame.display.flip()

    def handle_events_shop(self):

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.shop_board.trd_loop = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if self.buy_animal_button1.range_sides(pos[0], pos[1]):
                    self.buy_animal_button1.clicked_button()
                if self.buy_animal_button2.range_sides(pos[0], pos[1]):
                    self.buy_animal_button2.clicked_button()
                if self.buy_animal_button3.range_sides(pos[0], pos[1]):
                    self.buy_animal_button3.clicked_button()
                if self.buy_animal_button4.range_sides(pos[0], pos[1]):
                    self.buy_animal_button4.clicked_button()
                if self.buy_animal_button5.range_sides(pos[0], pos[1]):
                    self.buy_animal_button5.clicked_button()
                if self.buy_animal_button6.range_sides(pos[0], pos[1]):
                    self.buy_animal_button6.clicked_button()

                if self.sell_animal_button1.range_sides(pos[0], pos[1]):
                    self.sell_animal_button1.clicked_button()
                if self.sell_animal_button2.range_sides(pos[0], pos[1]):
                    self.sell_animal_button2.clicked_button()
                if self.sell_animal_button3.range_sides(pos[0], pos[1]):
                    self.sell_animal_button3.clicked_button()
                if self.sell_animal_button4.range_sides(pos[0], pos[1]):
                    self.sell_animal_button4.clicked_button()
                if self.sell_animal_button5.range_sides(pos[0], pos[1]):
                    self.sell_animal_button5.clicked_button()
                if self.sell_animal_button6.range_sides(pos[0], pos[1]):
                    self.sell_animal_button6.clicked_button()

                if self.sell_product_button1.range_sides(pos[0], pos[1]):
                    self.sell_product_button1.clicked_button()
                if self.sell_product_button2.range_sides(pos[0], pos[1]):
                    self.sell_product_button2.clicked_button()
                if self.sell_product_button3.range_sides(pos[0], pos[1]):
                    self.sell_product_button3.clicked_button()
                if self.sell_product_button4.range_sides(pos[0], pos[1]):
                    self.sell_product_button4.clicked_button()
                if self.sell_product_button5.range_sides(pos[0], pos[1]):
                    self.sell_product_button5.clicked_button()
                if self.sell_product_button6.range_sides(pos[0], pos[1]):
                    self.sell_product_button6.clicked_button()

                if self.buy_upgrade_button1.range_sides(pos[0], pos[1]):
                    self.buy_upgrade_button1.clicked_button()
                if self.buy_upgrade_button2.range_sides(pos[0], pos[1]):
                    self.buy_upgrade_button2.clicked_button()

    def run_farm(self):

        while not self.handle_events_farm():
            self.fps_clock.tick(15)
            self.shop_board.shops_surface.fill((0, 0, 0))
            self.barn_building_button.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (160, 82, 45))
            self.magazine_building_button.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (244, 164, 96))
            self.shop_building_button.draw(self.shop_board.shops_surface, pygame.mouse.get_pos(), (244, 164, 96))
            pygame.display.flip()

    def handle_events_farm(self):

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.shop_board.trd_loop = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if self.magazine_building_button.range_sides(pos[0], pos[1]):
                    self.magazine_building_button.clicked_button(self)
                if self.barn_building_button.range_sides(pos[0], pos[1]):
                    self.barn_building_button.clicked_button(self)
                if self.shop_building_button.range_sides(pos[0], pos[1]):
                    self.shop_building_button.clicked_button(self)


class Menu:

    def __init__(self, width, height):
        pygame.init()
        self.board = Board(width, height)

        self.start_button = MenuButton(400, 20, "Start")
        self.load_game_button = MenuButton(400, 70, "Load Game")
        self.controls_button = MenuButton(400, 120, "Controls")
        self.quit_button = MenuButton(400, 170, "Quit")

    def run(self):

        while not self.handle_events():

            self.board.shops_surface.fill((0, 0, 0))

            self.start_button.draw(self.board.shops_surface, pygame.mouse.get_pos(), (0, 255, 255))
            self.load_game_button.draw(self.board.shops_surface, pygame.mouse.get_pos(), (0, 255, 255))
            self.controls_button.draw(self.board.shops_surface, pygame.mouse.get_pos(), (0, 255, 255))
            self.quit_button.draw(self.board.shops_surface, pygame.mouse.get_pos(), (0, 255, 255))

            pygame.display.flip()

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                game.shop_board.trd_loop = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if self.start_button.range_sides(pos[0], pos[1]):
                    game = Farm(800, 400)
                    f = Timer(1, game.run_time)
                    f.start()
                    game.run_farm()
                if self.load_game_button.range_sides(pos[0], pos[1]):
                    pass
                if self.controls_button.range_sides(pos[0], pos[1]):
                    pass
                if self.quit_button.range_sides(pos[0], pos[1]):
                    pygame.quit()


if __name__ == "__main__":
    menu = Menu(800, 400)
    menu.run()
