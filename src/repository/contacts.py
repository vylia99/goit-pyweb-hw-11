from typing import List
from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactCreate, ContactUpdate
from datetime import date, timedelta


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactCreate, db: Session) -> Contact:
    contact = Contact(name=body.name,
                      surname=body.surname,
                      email=body.email,
                      phone=body.phone,
                      birthday=body.birthday,
                      info=body.info
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.info = body.info
        db.commit()
        db.refresh(contact)
    return contact


async def get_upcoming_birthdays(db: Session) -> List[Contact]:
    today = date.today()
    next_week = today + timedelta(days=7)

    contacts = db.query(Contact).all()
    upcoming = []

    for contact in contacts:
        if contact.birthday:
            birthday_this_year = contact.birthday.replace(year=today.year)
            if today <= birthday_this_year <= next_week:
                upcoming.append(contact)

    return upcoming


async def search_contacts(name: str | None, surname: str | None, email: str | None, db: Session) -> List[Contact]:
    query = db.query(Contact)

    if name:
        query = query.filter(Contact.name.ilike(f"%{name}%"))
    if surname:
        query = query.filter(Contact.surname.ilike(f"%{surname}%"))
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))

    return query.all()


async def delete_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact
