from pytest import mark, fixture
from database import s, IceCream, Tastes
from main import create_ice_cream


@fixture
def clean_db():
    s.query(IceCream).delete()
    s.query(Tastes).delete()
    tastes = [
        Tastes(id=1, name="Ваниль", weight=10),
        Tastes(id=2, name="Клубника", weight=3),
        Tastes(id=3, name="Шоколад", weight=4),
        Tastes(id=4, name="Банан", weight=2),
        Tastes(id=5, name="Дыня", weight=0),
    ]
    s.add_all(tastes)
    s.commit()


class TestMain:
    @mark.parametrize("name, cone, taste_id", [
        ("Шоколадное", "Большой", 3),
        ("Банановое", "Маленький", 4),
        ("Ванильное", "Средний", 1),
    ])
    def test_buy_ice_cream(self, clean_db, name, cone, taste_id):
        ice = create_ice_cream(name, cone, taste_id)
        data = s.query(IceCream).all()
        assert ice in data

    def test_quantity_ices(self, clean_db):
        ices = [
        ("Шоколадное", "Большой", 3),
        ("Банановое", "Маленький", 4),
        ("Ванильное", "Средний", 1),
    ]
        for ice in  ices:
            create_ice_cream(*ice)
        data = s.query(IceCream).all()
        assert len(data) == len(ices)

    def test_taste_property(self, clean_db):
        pass