import datetime as dt
from os import error, rename, path
from urllib.parse import urlencode
from typing import List
import requests
from fastapi import APIRouter, Depends  # Body,
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import config, models, utils, schemas


router = APIRouter()


@router.get("/customers", response_model=List[models.Customer])
def get_customers(*, db: Session = Depends(utils.get_db)):
    customers = db.query(schemas.Customer).all()
    return customers

@router.get("/customer/{id}", response_model=models.Customer)
def get_customer(*, db: Session = Depends(utils.get_db), id: int):
    customer = db.query(schemas.Customer).filter(schemas.Customer.id == id).first()
    return customer

@router.post("/customer", response_model=models.Customer)
def create_customer(
    *,
    db: Session = Depends(utils.get_db),
    customer: models.Customer
):
    customer_data = customer.dict(exclude_unset=True)
    db_customer = schemas.Customer(**customer_data)
    db.add(db_customer)
    db.commit()
    
    return db_customer


@router.delete("/customer")
def delete_milestone_type_ref(
    *, db: Session = Depends(utils.get_db), id: int
):
    db.query(schemas.Customer).filter(schemas.Customer.id == id).delete()
    db.commit()


@router.put("/customer/{id}", response_model=models.Customer)
def update_customer(
    *,
    db: Session = Depends(utils.get_db),
    id: int,
    customer: models.Customer
):
    customer_data = customer.dict(exclude_unset=True)
    db.query(schemas.Customer).filter(schemas.Customer.id == id).update(customer_data)
    db.commit()
    return db.query(schemas.Customer).filter(schemas.Customer.id == id).first()
