def phone_validator(v):
    if v.startswith("+998") and len(v) == 13 and v[1:].isdigit():
        return True
    else:
        raise ValueError("Telefon raqamingizda xatolik bor. Iltimos pastdagi tugma orqali telefon raqamingizni yuboring.")
