from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint, REAL
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property


database_file = "data.db"
engine = create_engine(f"sqlite:///{database_file}")
Session = sessionmaker(engine)
s = Session()


class Base(DeclarativeBase):
    pass


class Tastes(Base):
    __tablename__ = "tastes"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    weight = Column(REAL)


class IceCream(Base):
    __tablename__ = "ice_cream"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cone = Column(String(20))
    taste_id = Column(Integer, nullable=False)

    @hybrid_property
    def taste(self):
        taste = s.query(Tastes).filter_by(id=self.taste_id).first()
        if taste is None:
            return None
        return taste.name

    @hybrid_property
    def rem_weight(self):
        taste = s.query(Tastes).filter_by(id=self.taste_id).first()
        if taste is None:
            return None
        return taste.weight

    __table_args__ = (CheckConstraint(cone.in_(["Большой", "Средний", "Маленький"]), name="check_cone_type"),)



Base.metadata.create_all(engine)

# if __name__ == '__main__':
#     tastes = {"Ваниль": 10, "Клубника": 3, "Шоколад": 4, "Банан": 2, "Дыня": 0}
#     for key, value in tastes.items():
#         taste = Tastes(name=key, weight=value)
#         s.add(taste)
#     s.commit()
