from openai import OpenAI
from secrets import API_KEY

client = OpenAI(api_key=API_KEY)

### Отправь в OpenAI файл с промпт/ответ ###
file = client.files.create(
  file=open("dataset.jsonl", "rb"),
  purpose="fine-tune"
)

### Начать обучение по отправленному файлу
### (Переменная training_file береде его id, из прошлого отрывка кода)
client.fine_tuning.jobs.create(
  training_file=file.id,
  model="gpt-3.5-turbo"
#  model=CUSTOM_MODEL
)