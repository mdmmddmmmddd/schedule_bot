# bot/handlers/start.py

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.crud import get_or_create_user
from config import ROLES

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message, state: FSMContext):
    """
    Приветствие нового или возвращающегося пользователя.
    Роль у пользователя устанавливается управляющей через команду /assign_role.
    """
    # Получаем или создаем запись пользователя в БД с дефолтной ролью 'официант'
    user = get_or_create_user(telegram_id=message.from_user.id)
    if not user.role:
        user.role = "официант"
        user.save()

    # Ответ с указанием текущей роли
    await message.answer(
        f"👋 Привет, <b>{message.from_user.first_name}</b>!\n"
        f"Ваша роль в системе: <b>{user.role}</b>.\n"
        "Дальнейшие действия доступны согласно вашим правам."
    )

    # Сброс любых состояний FSM
    await state.clear()
