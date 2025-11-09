from praktikum.burger import Burger
from data import data
from unittest.mock import Mock 




class TestBurger:
    def test_create_burger(self):
        burger = Burger()
        assert burger.bun == None
        assert burger.ingredients == []

    def test_set_buns_to_burger(self, burger):
        mock_bun = Mock()
        mock_bun.configure_mock(name=data.bun_name, price = data.bun_price)
        burger.set_buns(mock_bun)
        assert burger.bun.name == data.bun_name

    def test_add_ingredient_one_ingredient(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(type = data.ingredient_type,name=data.ingredient_name, price = data.ingredient_price)
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].name == data.ingredient_name
        assert burger.ingredients[0].type == data.ingredient_type
        assert burger.ingredients[0].price == data.ingredient_price

    def test_remove_ingredient(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(type = data.ingredient_type,name=data.ingredient_name, price = data.ingredient_price)
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].name == data.ingredient_name
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger, ingredient):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(type = data.ingredient_type,name=data.ingredient_name, price = data.ingredient_price)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].name == data.ingredient_name
        assert burger.ingredients[1].name == data.ingredient_name

    def test_get_price_burger(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(name=data.ingredient_name, type=data.ingredient_type, price=data.ingredient_price)
        mock_ingredient.get_price = Mock(return_value=data.ingredient_price) 

        mock_bun = Mock()
        mock_bun.configure_mock(price=data.bun_price, name=data.bun_name)
        mock_bun.get_price = Mock(return_value=data.bun_price) 

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = burger.bun.price * 2 + burger.ingredients[0].price
        assert price == burger.get_price()

    def test_get_receipt_burger(self, burger, ingredient, bun):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(name=data.ingredient_name, type=data.ingredient_type, price=data.ingredient_price)
        mock_ingredient.get_price = Mock(return_value=data.ingredient_price) 
        mock_ingredient.get_name = Mock(return_value=data.ingredient_name)
        mock_ingredient.get_type = Mock(return_value=data.ingredient_type)

        mock_bun = Mock()
        mock_bun.configure_mock(price=data.bun_price, name=data.bun_name)
        mock_bun.get_price = Mock(return_value=data.bun_price) 
        mock_bun.get_name = Mock(return_value=data.bun_name)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        price = burger.bun.price * 2 + burger.ingredients[0].price
        assert (
            burger.get_receipt()
            == f"(==== {data.bun_name} ====)\n= {data.ingredient_type.lower()} {data.ingredient_name} =\n(==== {data.bun_name} ====)\n\nPrice: {price}"
        )
