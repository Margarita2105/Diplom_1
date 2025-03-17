from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 10)
        price = ingredient.get_price()

        assert price == 10

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 10)
        name = ingredient.get_name()

        assert name == 'hot sauce'

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 10)
        type = ingredient.get_type()

        assert type == 'SAUCE'
