from openai_api import OpenAI
import os

#利用OpenAI類別，建立一個可以跟OpenAI伺服器互動的物件
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

#完成一段對話
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say This is a test.",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)