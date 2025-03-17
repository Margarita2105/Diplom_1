from praktikum.bun import Bun

class TestBun:
    def test_get_name(self):
        bun = Bun('black bun', 10)
        name = bun.get_name()

        assert name == 'black bun'

    def test_get_price(self):
        bun = Bun('black bun', 10)
        price = bun.get_price()

        assert price == 10
