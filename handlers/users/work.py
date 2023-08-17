from aiogram import types
from aiogram.types import ContentTypes
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import menu_key, menu_key_ru, language_keyboard, contact_info, signal, signal_ru, register_course, register_course_ru
from loader import bot, dp
from utils.db_api.postgresql import send_human_info
from keyboards.inline.inline_key import course, course_ru

# matnlar
course_text = """
ASSALOMU ALAYKUM!!!
♦️Kelajakning eng rivojlanib kelayotgan kasblaridan biri — «TRADING»  sohasini chuqur va mukammal o’rganishni xohlaysizmi???
♦️Albatta bunda sizga «D_TRADING_INVEST» kompaniyamiz yordam beradi!!!
♦️Bizda online va off-line kurslar mavjud.
♦️Kursimizning davomiyligi - 40 kun, 15 ta darsdan iborat, + 1 oy amaliyot va 1 yil davomida qo’llab-quvvatlash.
♦️Qulay jadval - 1 haftada 3 ta dars.
♦️Kunduzgi va kechki guruhlar.
♦️Talabalarning o’rtacha soni 10 - 12 ta.
♦️Kursimizning har bir bitiruvchisiga Prop kompaniyasidan 5000$ dan 10.000$ gacha investitsiya olishga yordam beramiz.
♦️To’liq kursning narxlari -
Off-line 5.000.000 million sum,
Online 4.500.000 million sum.
♦️Hamda bizda 6 oy mobaynida bo'lib to'lash imkoniyati bor.Barcha savollaringizga javob olish uchun ofisimizga tashrif buyuring yoki biz bilan bo’glaning....
"""


course_text_ru = """
Здравствуйте!!!

Хотите глубоко и досконально изучить одну из самых развивающихся профессий будущего — «ТРЕЙДИНГ»???
Конечно, наша компания «D_TRADING_INVEST» Вам в этом поможет!!!

♦️У нас есть онлайн и оффлайн курсы.

♦️Продолжительность нашего курса 40 дней, состоит из 15 уроков, + 1 месяц практики и 1 год поддержки.

♦️Удобный график - 3 занятия в 1 неделю.

Дневные и вечерние группы.

♦️Среднее количество студентов 10-12 человек.

♦️Мы помогаем каждому выпускнику нашего курса получить инвестиции от 5000$ до 10000$ от компании Prop.

♦️Стоимость полного курса -
Офлайн 5 000 000 млн сум,
Онлайн 4 500 000 миллионов сум.

♦️А также есть возможность рассрочки на 6 месяцев.

Посетите наш офис или свяжитесь с нами, чтобы получить ответы на все ваши вопросы....
"""


signal_text = """
Bu yopiq kanal bo'lib, u erda D_trading_invest ning eng yaxshi analitiklari Forex savdo signallari joylanadi. Har bir signal uchun skrinshot shaklida grafik izohi ko'rsatiladi.

Har bir signal uchun Stop-Loss va Take-Profit ning aniq chegaralari beriladi   har bir operatsiyani to'liq qo'llab-quvvatlanadi: SL transferidan foydaning bir qismini belgilash va bitimni to'liq yopishgacha.

Signallar ertalabdan kechgacha kuniga  minimal 2 ta beriladi. Yaxshi natijalarga erishish uchun streyder 1-2 daqiqa ichida signal bo'yicha savdo ochishi, shuningdek, savdoni o'tkazib yubormasligi kerak.

⚡️ Forex bilan bosh og'rig'isiz savdo qiling - bitimlarni bosqichma -bosqich takrorlang va biz bilan daromad

*Diqqat! To'lov summasi bizda qaytarib berilmaydi. Savdoda tajribangiz bo'lmasa va signallardan unumli foydala olmasangiz obuna olmaganingiz ma'qul.


Nima sababdan bo'lsa ham, to'lov puli qaytarilib berilmaydi.
"""

signal_text_ru = """
Это закрытый канал, где лучшие аналитики D_trading_invest будут размещать торговые сигналы Форекс. Для каждого сигнала показано графическое объяснение в виде скриншота.

Для каждого сигнала даны четкие лимиты Stop-Loss и Take-Profit, полностью поддерживается каждая операция: от переноса SL до выставления части прибыли и полного закрытия сделки.

Сигнал подаются минимум 2 раза в сутки с утра до вечера. Для получения хороших результатов трейдер должен открывать сделку по сигналу в течение 1-2 минут, а также не пропускать сделки.

⚡️ Торгуйте на Форекс без головной боли - повторяйте сделки шаг за шагом и зарабатывайте вместе с нами

*Внимание! Сумма платежа возврату не подлежит. Если у вас нет опыта торговли и вы не можете эффективно использовать сигналы, лучше не подписывайтесь.

Сборы не подлежат возврату ни по какой причине.
"""


company_text = """
♦️ D_TRADING_INVEST  — 2021-yilda asos solingan, moliyaviy va investitisiya konsalting tashkiloti.

Kompaniyaning barcha xizmatlari O'zbekiston Respublikasi qonunchiligiga asosan lisenziyalangan.

D_TRADING_INVEST moliya va investitisiya, ishonchli boshqaruv, investitisiya portfelini yaratish, investitsiya kititish, jamg'arma dasturlari va investitsiya strategiyalarini baholash sohalarida konsalting xizmatlarini ko'rsatadi.

♦️ Dilshod Abdusattarov — kompaniya rahbari, oliy ma'lumotli xalqaro investitsiya konsalti,
 7-yillik tajribaga ega trader !
"""


company_text_ru = """
♦️ D_TRADING_INVEST — финансово-инвестиционная консалтинговая организация, основанная в 2021 году.

Все услуги компании лицензированы в соответствии с законодательством Республики Узбекистан.

D_TRADING_INVEST предоставляет консультационные услуги в области финансов и инвестиций, доверительного управления, создания инвестиционного портфеля, планирования инвестиций, сберегательных программ и оценки инвестиционной стратегии.

♦️ Дильшод Абдусаттаров - руководитель компании, высокообразованный международный инвестиционный консультант,
Трейдер с 7-летним стажем!
"""


contact_text = """
Murojaat uchun:
📲+998 (95)290-05-50
📲+998 (97)579-05-50
Bizning manzil:
📍Samarqand shahri, IT park (mo'ljal: Atlas savdo markazi)
"""


contact_text_ru = """
Телефоны:
📲+998 (95)290-05-50
📲+998 (97)579-05-50
Наш адрес:
📍 г.Самарканд, IT-парк (направление: ТЦ Атлас)
"""

# end of texts


@dp.message_handler(text=["🇺🇿O'zbekcha", "🇷🇺Русский"])
async def menu_fun(message: types.Message):
    if message.text == "🇺🇿O'zbekcha":
        await message.reply("📄 Kompaniyaning xizmatlar katalogi:", reply_markup=menu_key)
    elif message.text == "🇷🇺Русский":
        await message.reply("📄 Каталог услуг компании:", reply_markup=menu_key_ru)
    else:
        pass


@dp.message_handler(text=["🇷🇺Tilni uzgartirish", "🇺🇿Сменить язык"])
async def change_language(message: types.Message):
    if message.text == "🇷🇺Tilni uzgartirish":
        await message.answer("📄 Каталог услуг компании:", reply_markup=menu_key_ru)
    elif message.text == "🇺🇿Сменить язык":
        await message.answer("📄 Kompaniyaning xizmatlar katalogi:", reply_markup=menu_key)
    else:
        pass



@dp.message_handler(text=["☎Aloqalar", "☎️Контакты"])
async def send_contact(message: types.Message):
    if message.text == "☎Aloqalar":
        await bot.send_message(chat_id=message.from_user.id, text=contact_text)
        await bot.send_location(chat_id=message.from_user.id, latitude=39.646405, longitude=66.923493)
    elif message.text == "☎️Контакты":
        await bot.send_message(chat_id=message.from_user.id, text=contact_text_ru)
        await bot.send_location(chat_id=message.from_user.id, latitude=39.646405, longitude=66.923493)
    else:
        pass


@dp.message_handler(text=["ℹ️Bizning kompaniya haqida", "ℹ️ О нашей компании"])
async def send_about(message: types.Message):
    if message.text == "ℹ️Bizning kompaniya haqida":
        await message.answer(company_text)
    elif message.text == "ℹ️ О нашей компании":
        await message.answer(company_text_ru)
    else:
        pass


@dp.message_handler(text=["‍🎓Treyding kursi 2023", "🎓Курсы по трейдингу 2023"])
async def our_course(message: types.Message):
    if message.text == "‍🎓Treyding kursi 2023":
        await message.answer(course_text, reply_markup=course)
    elif message.text == "🎓Курсы по трейдингу 2023":
        await message.answer(course_text_ru, reply_markup=course_ru)
    else:
        pass



# @dp.message_handler(text=["◀️Bosh menyuga qaytish", "◀️Вернуться в главный меню"])
# async def main_menu(message: types.Message):
#     if message.text == "◀️Bosh menyuga qaytish":
#         await message.answer("Tanlang", reply_markup=menu_key)
#     elif message.text == "◀️Вернуться в главный меню":
#         await message.answer("Выберите:", reply_markup=menu_key_ru)
#     else:
#         pass


@dp.message_handler(text=["📈Forex savdo signallari", "📈Торговые сигналы Forex"])
async def forex_signals(message: types.Message):
    if message.text == "📈Forex savdo signallari":
        await message.answer(signal_text, reply_markup=signal)
    elif message.text == "📈Торговые сигналы Forex":
        await message.answer(signal_text_ru, reply_markup=signal_ru)
    else:
        pass

