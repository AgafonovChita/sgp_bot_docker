async def start_message(username: str, chat_title: str) -> str:
    return f"Привет, <b>{username}</b>\U0000270C\U0000270C\nЯ бот-администратор канала <b>{chat_title}</b>" \
           f"\n\nЧтобы я смог присоединить тебя к каналу, нам с тобой нужно сделать несколько простых шагов." \
           f"\nНачинаем? 🙃 \n\nПредставься, пожалуйста <i>(фамилии и имени вполне достаточно)</i>"


async def not_valid(error_text: str) -> str:
    return f"Что-то пошло не так \U0001F914\n\n<i>{error_text}</i>\n\nПопробуй ещё раз"


async def get_position(username: str) -> str:
    return f"Приятно познакомиться, <b>{username}</b> \U0001F917" \
           f"\n\nА теперь напиши свою должность в компании"


async def get_phone() -> str:
    return f"Отлично!\nОстался последний шаг:\n\nНажми кнопку <b>«Поделиться моим контактом»</b>\n" \
           f"\U000023EC\U000023EC" \
           f"\n\n\n<i>Мой друг, не переживай, эта информация необходима только нашим прекрасным HR СГП🥰</i>"


async def finish_reg() -> str:
    return f"Ура, мы справились! \n"


async def send_link() -> str:
    return f"Жми по кнопке и скорее становись частью нашего коммьюнити \U0001F609\n"








