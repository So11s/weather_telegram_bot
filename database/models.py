from sqlalchemy import Column, Integer, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)  # telegram id
    city = Column(String)
    connection_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    reports = relationship("WeatherReport", backref="report", lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return self.tg_id


class WeatherReport(Base):
    __tablename__ = "WeatherReports"
    id = Column(Integer, primary_key=True)
    owner = Column(Integer, ForeignKey("Users.id"), nullable=False)  # id пользовтеля
    date = Column(DateTime, default=datetime.datetime.now, nullable=False)  # Дата
    temp = Column(Integer, nullable=False)  # Температура воздуха
    feels_like = Column(Integer, nullable=False)  # Температура воздуха по ощущениям
    wind_speed = Column(Integer, nullable=False)  # Скорость ветра
    pressure_mm = Column(Integer, nullable=False)  # Давление
    city = Column(String, nullable=False)

    def __repr__(self):
        return self.city
