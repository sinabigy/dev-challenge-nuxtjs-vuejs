from app import schemas
from .base import Base
from typing import List


class Customer(Base):
    id : int = None
    first_name : str = None
    last_name : str = None
    email : str = None
    active : bool = None
    purchase : float = None
    purchase_date : str = None
    employee_id : int = None
    employee_name : str = None