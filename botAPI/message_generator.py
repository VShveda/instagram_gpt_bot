import os

from google import generativeai as gemini
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini.configure(api_key=GEMINI_API_KEY)


def get_message(bio: dict, objects_detected: str) -> str:

    prompt = f"""
    Я збираюся написати перше дружнє повідомлення людині на основі її профілю в Instagram.
    Ось що я знаю про людину: 
    - Ім'я: {bio['full_name']}
    - Опис профілю: {bio['description']}
    - Виявлені об'єкти на фото: {objects_detected}
    
    Згенеруй привітальне повідомлення, яке буде ввічливим, 
    приємним і покаже інтерес до її хобі чи того, що є в описі або на фотографії. 
    Повідомлення повинно бути коротким і підходити для першого знайомства.
    """

    model = gemini.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    text = response.text

    return text
