import re
from models.address import AddressModel
import pytest


PUBLIC_ID_FORMAT = r"(addr_[A-Za-z\d]{32})"


def test_AddressModel():
    model = AddressModel(
        street1="123 Main Street",
        street2="Suite 420",
        city="Boulder",
        state="Colorado",
        postal_code="80301",
        country="US"
    )
    assert re.match(PUBLIC_ID_FORMAT, model.public_id)
    assert model.street1 == "123 Main Street"
    assert model.street2 == "Suite 420"
    assert model.city == "Boulder"
    assert model.state == "Colorado"
    assert model.postal_code == "80301"
    assert model.country == "US"
