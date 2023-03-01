import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ShopView(toga.Box):
    def __init__(self, points=0, products=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.points = points
        self.products = products or []

        self.heading_label = toga.Label(
            'Shop',
            style=Pack(padding=(0, 5))
        )

        self.points_label = toga.Label(
            f'Points: {self.points}',
            style=Pack(padding=(0, 5))
        )

        self.product_buttons = []
        for product in self.products:
            self.product_buttons.append(
                toga.Button(
                    f'{product["name"]} - {product["points"]} points',
                    on_press=self.buy_product,
                    args=(product,),
                    style=Pack(flex=1)
                )
            )

        self.box = toga.Box(children=self.product_buttons)

        self.add(
            self.heading_label,
            self.points_label,
            self.box,
            style=Pack(direction=COLUMN)
        )

    def buy_product(self, widget, product):
        if self.points >= product['points']:
            # Code to process the purchase
            self.points -= product['points']
            self.points_label.text = f'Points: {self.points}'
            print(f'Purchased {product["name"]}')
        else:
            print('Insufficient points')
