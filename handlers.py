from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
import TG.keyboards as keyboards
from aiogram.fsm.context import FSMContext
import google.generativeai as genai

router = Router()

class Data(StatesGroup):
    date = State()

API_KEY = "AIzaSyAWzec5LwDWZDtlwT0dC9VWppHLkg12g9w"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Добро пожаловать в History Bot, я помогу вам найти события по указанной дате :)', reply_markup = keyboards.kb)

@router.callback_query(F.data == 'start work')
async def help_command(callback: CallbackQuery):
    await callback.answer('На старт')
    await callback.message.answer('Добро пожаловать в History Bot, я помогу вам найти события по указанной дате :)', reply_markup = keyboards.kb)

@router.callback_query(F.data == 'try me')
async def change1(callback: CallbackQuery):
    await callback.answer('Испытать меня')
    await callback.message.answer('Выберите вариант', reply_markup = keyboards.ik )

@router.callback_query(F.data == 'finish work')
async def change2(callback: CallbackQuery):
    await callback.answer('Завершить работу')
    await callback.message.answer('Ну вот...Приходите еще!', reply_markup=keyboards.ik2)

@router.callback_query(F.data == 'finish work')
async def change3(callback: CallbackQuery):
    await callback.answer('Завершить работу')
    await callback.message.answer('Ну вот...Приходите еще!', reply_markup=keyboards.ik2)

@router.callback_query(F.data == 'write data')
async def change4(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Ввести дату')
    await callback.message.answer('Урааааа, погнали!\nВведите дату в формате:\n YYYY-MM-DD')
    await state.set_state(Data.date)

@router.message(Data.date)
async def change5(message: Message, state: FSMContext):
    await state.update_data(date = message.text)
    data = await state.get_data()
    dt = str(data['date'])

    if dt[:4] == '2009' and dt[4] == '-' and dt[5:7] == '02' and dt[8:10] == '26' and dt[7] == '-':
        await message.answer('В этот день родился скромный гений - создатель этого бота, все остальное не так уж и важно, но, ради приличия, найду для вас еще информацию :)')
    if dt[:4].isdigit() and int(dt[:4]) <= 2025 and dt[4] == '-' and dt[5:7].isdigit() and int(dt[5:7]) <= 12 and dt[7] == '-' and dt[8:10].isdigit() and int(dt[8:10]) <= 31 and len(dt) == 10:

        await message.answer('Подождите немного, поиск может занять до десяти секунд...')
        response = model.generate_content(f'Расскажи кратко, что было в этот день в мировой истории, в первую очередь ищи события в истории России {data}, распиши по пунктам с цифрами, обязательно убери все символы "*" из ответа')
        await message.answer(response.text, reply_markup=keyboards.ik2)

    else:
        await message.answer('Проверьте, пожалуйста, корректность введенных данных!\n1) Обратите внимание, что если количество разрядов вашего числа в введенной дате меньше шаблонного,то необходимо заполнить пустующие значения нулями\n '
                             '2) Обратите внимание, что вторым элементом в введенной дате является МЕСЯЦ, а уже третьим - ДЕНЬ\n 3) Бот не ищет события до нашей эры :(', reply_markup = keyboards.ik)




