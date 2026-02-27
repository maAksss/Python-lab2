from googletrans import Translator, LANGUAGES

# Ініціалізація об'єкта перекладача
translator = Translator()

def TransLate(text, lang):
    """
    Перекладає текст на вказану мову (код або назва).
    """
    try:
        result = translator.translate(text, dest=lang)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(txt):
    """
    Визначає мову тексту та рівень впевненості (confidence).
    """
    try:
        det = translator.detect(txt)
        return f"Detected(lang={det.lang}, confidence={det.confidence})"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang):
    """
    Повертає код мови за назвою, або назву за кодом.
    """
    lang = lang.lower().strip()
    
    # Якщо передано код (наприклад, 'en') -> повертаємо назву ('english')
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    
    # Якщо передано назву (наприклад, 'english') -> повертаємо код ('en')
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
            
    return "Мову не знайдено"

# --- Основна програма ---

if __name__ == "__main__":
    txt = "Доброго дня. Як справи?"
    target_lang = "en"

    print(f"Вхідний текст: {txt}")
    print(f"Визначення мови: {LangDetect(txt)}")
    print(f"Переклад ({target_lang}): {TransLate(txt, target_lang)}")
    print(f"Код для 'En': {CodeLang('En')}")
    print(f"Назва для 'english': {CodeLang('English')}")

    print("-" * 30)
    
    # Інтерактив з користувачем (п. 2.4)
    user_text = input("Введіть текст для перекладу: ")
    user_lang = input("Введіть мову призначення (назва або код): ")
    
    result = TransLate(user_text, user_lang)
    print(f"Результат: {result}")