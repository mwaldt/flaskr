import re
import pytest

from models.base import MyBaseModel


# 2025-10-21T17:26:00.805633+00:00
DATE_FORMAT = r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}\+\d{2}:\d{2})"
PUBLIC_ID_FORMAT = r"(obj_[A-Za-z\d]{32})"


def test_assert_datetime_fortmatter():
    time = "2025-10-21T17:26:00.805633+00:00"
    assert re.match(DATE_FORMAT, time)


def test_create_uuid_with_prefix():
    model = MyBaseModel()
    assert re.match(PUBLIC_ID_FORMAT, model.public_id)
    assert re.match(DATE_FORMAT, model.created_at)
    assert re.match(DATE_FORMAT, model.updated_at)
