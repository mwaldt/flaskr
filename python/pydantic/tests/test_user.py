import re
from models.user import UserModel
import pytest


PUBLIC_ID_FORMAT = r"(user_[A-Za-z\d]{32})"


def test_UserModel():
    model = UserModel(
        name="John Snow",
        email="jsnow@nightswatch.com",
        phone="555-555-5555",
    )
    assert re.match(PUBLIC_ID_FORMAT, model.public_id)
    assert model.name == "John Snow"
    assert model.email == "jsnow@nightswatch.com"
    assert model.phone == "555-555-5555"
