from aiogram import Router
from aiogram.types import Message

router: Router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer('я тебя не понимаю! воспользуйся командой /help')