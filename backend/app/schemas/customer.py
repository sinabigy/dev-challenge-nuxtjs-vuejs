from email.policy import default
from sqlalchemy import Column, ForeignKey, Boolean, Float, Integer, String, Date, func, or_, and_
from sqlalchemy.orm import relationship, object_session
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
import datetime as dt

from sqlalchemy.sql.sqltypes import VARCHAR

from app import utils
from app.db.base import Base
from enum import IntEnum


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    active = Column(Boolean, default=True)
    purchase = Column(Float, default=0.0)
    purchase_date = Column(String)
    employee_id = Column(Integer, default=0)
    sqlite_autoincrement=True