import json
from datetime import time


from sqlalchemy import false, true
from model import Users, Session, session
from main_bot import message_id, user_id, is_bot, first_name, last_name, username, language_code, is_premium, text, date



session = Session()  # Создаем новую сессию

users = Users(
    message_id=message_id,
    user_id=user_id,
    is_bot=is_bot,
    first_name=first_name,
    last_name=last_name,
    username=username,
    language_code=language_code,
    is_premium=is_premium,
    text=text,
    date=date
)
session.add(users)  # Обновляет существующую запись, если она есть, иначе добавляет новую запись.
session.commit()  # Cохранение изменений
session.close()  # Завершаем сессию


results = session.query(Users).all()
for message in results:
    print(message.message_id)
# print(results[-1].message_id)



