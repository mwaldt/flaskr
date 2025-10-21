from models.item import ItemModel
import re
import pytest


PUBLIC_ID_FORMAT = r"(item_[A-Za-z\d]{32})"


def test_ItemModel():
    model = ItemModel(
        name="Bicycle Deck of Cards",
        description="Bicycle brand deck of cards, 52 cards in all!",
        currency_code="USD",
        price_cents=420,
        stock_quantity=200
    )
    assert re.match(PUBLIC_ID_FORMAT, model.public_id)
    assert model.name == "Bicycle Deck of Cards"
    assert model.description == "Bicycle brand deck of cards, 52 cards in all!"
    assert model.currency_code == "USD"
    assert model.price_cents == 420
    assert model.price == 4.20
    assert model.stock_quantity == 200

