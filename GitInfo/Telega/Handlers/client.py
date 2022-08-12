from aiogram import types, Dispatcher
from create_bot import bot
from create_bot import dp
from Keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.text, 'Привет', reply_markup=kb_client)
		await message.reply('Привет', reply_markup=kb_client)
		# await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Telege_Test_Bot')

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
	await message.reply('Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')
	# await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await message.reply('ул. Советская 15')
	# await bot.send_message(message.from_user.id, 'ул. Советская 15')


# @dp.message_handler(commands=['Меню'])
# async def pizza_menu_command(message : types.Message):
# 	for ret in cur.execute('SELECT * FROM menu').fetchall():
# 	   await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

def register_handlers_client(dp:Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
	dp.register_message_handler(pizza_place_command, commands=['Расположение'])