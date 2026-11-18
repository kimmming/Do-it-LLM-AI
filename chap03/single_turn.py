from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break

    response = client.chat.completions.create(
        model = "gpt-4o",
        temperature= 0.9,
        messages = [
            {"role": "system", "content": "너는 사용자를 도와주는 상담사야"},
            {"role": "user", "content": user_input},
        ]
    )

    print("AI: " + response.choices[0].message.content)

"""
출력
사용자: 안녕 내 이름은 ooo야
AI: 안녕하세요, ooo님! 만나서 반가워요. 오늘 어떻게 도와드릴까요?
사용자: 내 이름이 뭘까?
AI: 죄송하지만, 저는 사용자의 이름을 알 수 없습니다. 저에게 제공해 주시면 기억하도록 하겠습니다. 어떻게 도와드릴까요?
사용자: exit
"""