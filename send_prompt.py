from openai import OpenAI
from secrets import API_KEY, CUSTOM_MODEL
client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
  model=CUSTOM_MODEL,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
#    {"role": "user", "content": "Что тебе известно о компании kostyapy?"}
#    {"role": "user", "content": "В чем заключается деятельность компании kostyapy?"}
    {"role": "user", "content": "Чем занимается компания kostyapy?"}
#    {"role": "user", "content": "А чем занимается компания kostyapy?"}
#    {"role": "user", "content": "Где находится айти компания kostyapy?"}
  ]
)
print(completion.choices[0].message)
