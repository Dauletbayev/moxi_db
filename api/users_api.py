from fastapi import APIRouter
from database.userservice import *

users_router = APIRouter(tags=['Управление пользователями'], prefix='/users')

@users_router.post('/api/register_user')
async def register_user(user_id: int, username: str):
    new_user = register_user_db(user_id=user_id, username=username, reg_day=datetime.now())
    if new_user:
        return new_user
    return new_user


@users_router.post('/api/add_score')
async def add_score(user_id: int, additional_score: int):
    result = add_score_db(user_id=user_id, additional_score=additional_score)
    if result:
        return 'Nice'
    return 'Pizdec'


@users_router.get('/api/get_user_count')
async def get_user_count():
    result = get_user_count_db()
    if result:
        return result
    return 'Users not found'


@users_router.get('/api/get_top_users')
async def get_top_users():
    result = get_top_users_db()
    if result:
        return result
    return 'Not found'


@users_router.get('/api/get_all_users')
async def get_all_users():
    result = get_all_users_db()
    if result:
        return result
    return 'Not found'


@users_router.get('/api/get_user_score')
async def get_user_score(user_id):
    result = get_user_score_db(user_id=user_id)
    if result:
        return result
    return 'Not found'

@users_router.post('/api/add_wallet_address')
async def add_wallet_address(user_id: int, address_ton: str):
    result = add_wallet_address_db(user_id, address_ton)
    if result:
        return result
    return result


@users_router.put('/api/update_wallet_address')
async def update_wallet_address(user_id: int, address_ton: str):
    result = update_wallet_address_db(user_id=user_id, address_ton=address_ton)
    if result:
        return result
    return result


@users_router.get('/api/get_detailed_user')
async def get_detailed_user(user_id: int):
    user = get_detailed_user_db(user_id=user_id)
    if user:
        return user
    return user
