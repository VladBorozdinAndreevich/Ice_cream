import os
from pytest import mark
from database import database_file, Tastes, IceCream


class TestDB:
    def test_connection(self):
        assert os.path.exists(database_file)

    @mark.parametrize("attr", [
        "id", "name", "weight"
    ])
    def test_tastes_attrs(self, attr):
        assert hasattr(Tastes, attr)

    @mark.parametrize("attr", [
        "id", "name", "cone", "taste_id"
    ])
    def test_ice_cream_attrs(self, attr):
        assert hasattr(IceCream, attr)