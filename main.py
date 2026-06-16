from database import s, Tastes, IceCream

def create_ice_cream(name, cone, taste_id):
    taste = s.query(Tastes).filter_by(id=taste_id).first()
    if taste is None:
        raise TypeError("Вкус не найден")
    if taste.weight <= 0:
        raise TypeError("Нет в наличии")
    ice_cream = IceCream(name=name, cone=cone, taste_id=taste_id)
    s.add(ice_cream)
    taste.weight -= 0.1
    s.commit()
    return ice_cream


if __name__ == '__main__':
    m1 = create_ice_cream("Банановое", "Средний", 4)
    print(m1)