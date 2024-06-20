from database.models import User
from datetime import datetime
from database import get_db


def register_user_db(user_id, username, reg_day):
    db = next(get_db())

    # Проверка на уникальность user_id
    if db.query(User).filter(User.user_id == user_id).first():
        return "User ID already exists."

    # Проверка на уникальность username
    if db.query(User).filter(User.username == username).first():
        return "Username already exists."

    new_user = User(user_id=user_id, username=username, reg_day=reg_day)
    db.add(new_user)
    db.commit()
    return new_user

def add_score_db(user_id, additional_score):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        user.score += additional_score
        db.commit()
        return user
    return None

def get_user_count_db():
    db = next(get_db())
    return db.query(User).count()

def get_top_users_db(limit=3):
    db = next(get_db())
    return db.query(User).order_by(User.score.desc()).limit(limit).all()

def get_all_users_db():
    db = next(get_db())
    return db.query(User).all()

def get_user_score_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        return user.score
    return None

def add_wallet_address_db(user_id, address_ton):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        # Обновление или добавление адреса кошелька
        user.address_ton = address_ton
        db.commit()
        return "Wallet address added successfully."
    return "User not found."

def update_wallet_address_db(user_id, address_ton):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        user.address_ton = address_ton
        db.commit()
        return "Wallet address updated successfully."
    return "User not found."


def get_detailed_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        return user
    return 'User not found'

