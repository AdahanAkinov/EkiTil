from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_profil_change = InlineKeyboardButton(text='🔙', callback_data='ОтменитьИзмененииПрофиля')

#инлайн клава для изменения профиля для студентов
change_profile_kb_student = InlineKeyboardButton(text='Изменить🖌️', callback_data='ИзменитьПрофильСтудент')
ikb_change_profile_student = InlineKeyboardMarkup(row_width=1).insert(change_profile_kb_student)


# инлайн клава для изменения профиля Учителей и других
change_profile_kb = InlineKeyboardButton(text='Изменить🖋️', callback_data='ИзменитьПрофильУчитель')
ikb_change_profile_teacher = InlineKeyboardMarkup().add(change_profile_kb)


# инлайн клава по пунктам, что именно хочет изменить:
change_profile_kb_student_chosen = [
                                    InlineKeyboardButton(text='Имя', callback_data='ИзменитьИмя'),
                                    InlineKeyboardButton(text='Фамилию', callback_data='ИзменитьФамилию'),
                                    InlineKeyboardButton(text='Курс', callback_data='ИзменитьКурс'),
                                    InlineKeyboardButton(text='Группа', callback_data='ИзменитьГруппа'),
                                    InlineKeyboardButton(text='Аккаунт', callback_data='ИзменитьАккаунт'),
                                    InlineKeyboardButton(text='Пароль', callback_data='ИзменитьПароль'),
                                    InlineKeyboardButton(text='Кредо', callback_data='ИзменитьКредо')
                                    ]
ikb_change_profile_kb_student_chosen = InlineKeyboardMarkup(row_width=2).add(*change_profile_kb_student_chosen).add(cancel_profil_change)

# инлайн клава по пунктам, что именно хочет изменить ПРЕПОДОВАТЕЛЬ:
change_profile_kb_teacher_chosen = [
                                    InlineKeyboardButton(text='Имя', callback_data='ИзменитьИмяПрепод'),
                                    InlineKeyboardButton(text='Фамилию', callback_data='ИзменитьФамилиюПрепод'),
                                    InlineKeyboardButton(text='Кредо', callback_data='ИзменитьКредоПрепод')
                                    ]
ikb_change_profile_kb_teacher_chosen = InlineKeyboardMarkup(row_width=1).add(*change_profile_kb_teacher_chosen).add(cancel_profil_change)
