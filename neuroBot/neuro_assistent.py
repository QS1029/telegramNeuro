import requests
from config import YANCONV_TOKEN

async def get_response(message_text):
    prompt = {
        "modelUri": "gpt://b1gf5pfjsd0phsrq2ldh/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.5,
            "maxTokens": "2000"
        },
        "messages": [
            { #Ты — рекрутер в указанной компании. Имитируй собеседование на работу для указанной должности, задавая вопросы, как будто ты потенциальный работодатель. Твоя задача — определить технические навыки кандидата. Сгенерируй вопросы для интервью с потенциальным кандидатом
                "role": "system",
                "text": "Ты - Нейронная Сеть, которая может улучшить запрос от пользователя, он передает тебе запрос,"
                        "ты его улучшаешь в единичном формате и передаешь в нейронную сеть для генерации картинки."
            },
            {
                "role": "user",
                "text": message_text
            }
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {YANCONV_TOKEN}"
    }
    response = requests.post(url, headers = headers, json = prompt)
    result = response.json()
    return result['result']['alternatives'][0]['message']['text']

# @dp.message_handler()
# async def analize_message(message:types.Message):
#     response_text = await get_response((message.text))
#     await message.answer(response_text)