from aiogram import Bot, Dispatcher, F, types
import asyncio
from TG.handlers import router


async def main():
    bot = Bot(token='7448382566:AAEttrBHXxXGpdmVvjLG6fAEOnRYISJybv0')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
        asyncio.run(main())

