from pydantic import BaseModel
from datetime import date

class AnimalBase(BaseModel):
    name: str
    species: str
    birth_date: date
    breed: str
    photo_url: str

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

class AnimalCreate(AnimalBase):
    pass

class Animal(AnimalBase):
    id: int

    class Config:
        orm_mode = True
