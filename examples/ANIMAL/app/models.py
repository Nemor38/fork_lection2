from sqlalchemy import Column, Integer, String, Date
from app.database import Base
from datetime import date

class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String, index=True)
    birth_date = Column(Date)
    breed = Column(String)  # Нове поле
    photo_url = Column(String)  # Нове поле

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
