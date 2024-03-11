import openai
from openai import OpenAI
from secrets import API_KEY

client = OpenAI(api_key=API_KEY)

all_jobs = []
for job in client.fine_tuning.jobs.list(
    limit=20,
):
    all_jobs.append(job)

for job in all_jobs:
    print(f"ID задания: {job.id}")
    print(f"Создано: {job.created_at}")
    print(f"Статус: {job.status}")
    if job.error.code is not None:
        print(f"Ошибка: {job.error.message} (Код: {job.error.code})")
    else:
        print("Ошибка: Отсутствует")
    print(f"Модель для настройки: {job.model}")
    print(f"Настроенная модель: {job.fine_tuned_model}")
    print(f"Токены, использованные в обучении: {job.trained_tokens}")
    print(f"Файл обучения: {job.training_file}")
    if job.validation_file is not None:
        print(f"Файл валидации: {job.validation_file}")
    else:
        print("Файл валидации: Отсутствует")
    print(f"Гиперпараметры: Эпохи - {job.hyperparameters.n_epochs}, Размер партии - {job.hyperparameters.batch_size}, Множитель скорости обучения - {job.hyperparameters.learning_rate_multiplier}")
    print("-" * 50)