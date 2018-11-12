from sqlalchemy import Column, Integer, ForeignKey

from rdbms.models.database import Base


class Number(Base):
    __tablename__ = 'numbers'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    number = Column(Integer, nullable=False)
