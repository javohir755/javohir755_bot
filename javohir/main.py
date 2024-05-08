import asyncio
import logging
import sys
import types
import time
from aiogram import types

from os import getenv
from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, and_f
from aiogram.types import Message
from config import TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
  

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
 

@dp.message(F.text=="guruh haqida malumot",F.chat.type=="supergroup")
async def get_group(message:Message):
    await message.answer(f"Guruh Nomi:{message.chat.title}\nGuruh Turi:{message.chat.type}\nGuruh Idisi:{message.chat.id}")


@dp.message(F.chat.type=="supergroup",F.new_chat_members)
async def get_new_chat(message:Message):
    for new_chat in message.new_chat_members:
        await message.answer(f"Salom {new_chat.full_name} guruhga hush kelibsiz")
        await message.delete()

@dp.message(F.chat.type=="supergroup",F.left_chat_member)
async def get_new_chat(message:Message):
    await message.answer(f"Xo'sh {message.left_chat_member.full_name}")



@dp.message(F.chat.type=="supergroup",and_f(F.text=="Yozma",F.reply_to_message))
async def get_banned_chat(message:Message):
    user_id=message.reply_to_message.from_user.id
    permission=types.ChatPermissions(can_send_messages=False)
    await message.chat.restrict(user_id,permission)
    await message.answer(f"yozishdan chetlatildiz❌\n{message.reply_to_message.from_user.full_name}")
   
@dp.message(F.chat.type=="supergroup",and_f(F.text=="Yozing",F.reply_to_message))
async def get_not_ban_chat(message:Message):
    user_id=message.reply_to_message.from_user.id
    permission=types.ChatPermissions(can_send_messages=True)
    await message.chat.restrict(user_id,permission)
    await message.answer(f"Yozavering\n✅{message.reply_to_message.from_user.full_name}")
 

@dp.message(F.chat.type=="supergroup",and_f(F.text=="ban",F.reply_to_message))
async def get_bann(message:Message):
    user_id=message.reply_to_message.from_user.id
    await message.chat.ban_sender_chat(user_id)
    await message.answer(f"{message.reply_to_message.from_user.full_name} siz guruhdan chetlandiz ⛔️")
    # time.sleep(6)
    # user_id=message.reply_to_message.from_user.id
    # await message.chat.unban_sender_chat(user_id)
    # await message.answer(f"{message.reply_to_message.from_user.full_name} siz foydalanishingiz mumkin ✅")



@dp.message(F.chat.type=="supergroup",and_f(F.text=="unban",F.reply_to_message))
async def get_unbann(message:Message):
    user_id=message.reply_to_message.from_user.id
    await message.chat.unban_sender_chat(user_id)
    await message.answer(f"{message.reply_to_message.from_user.full_name} siz foydalanishingiz mumkin ✅")





@dp.message()
async def echo_handler(message: Message) -> None:
   await message.send_copy(chat_id=message.chat.id)
   

async def main() -> None:
    
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())






# import asyncio
# import logging
# import sys
# import types
# import time
# from aiogram import types

# from os import getenv
# from aiogram import Bot, Dispatcher, html,F
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart, and_f
# from aiogram.types import Message
# from config import TOKEN

# dp = Dispatcher()


# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
  

#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    
# @dp.message(F.text=='salom',F.chat.type=='supergroup')
# async def get_group(message:Message):
#     await message.answer(f'{message.chat.title}/n{message.chat.type}/n{message.chat.id}')
    
# @dp.message()
