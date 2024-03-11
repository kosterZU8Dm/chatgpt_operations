# Steps to run fine-tuning
1. Prepare dataset
   1. Minimum 10 examples required
   2. Format must be JSONL
2. Add your OpenAI API Key to variable into secrets.py:
```bash
echo API_KEY="..." > secrets.py
echo CUSTOM_MODEL="..." >> secrets.py
```
make python3 virtual environment:
```bash
python3 -m venv venv
```
4. Install py-script requirements:
```bash
pip3 install -r requirements.py
```
5. Execute py-script like follow:
```bash
python3 start_fin-tuning.py
```

## Наблюдения
1. Подготовлен датасет из 50 строк (Каждые 10 имеют один вопрос, ответы разные, но одинаковые по смыслу)
2. Первое обучение не дало никакого результата (Training loss 0.5481)
   1. Нет ответов даже на шаблонные вопросы
3. Было выполнено второе обучение на модель, полученную после первого обучения, используя ровно тот же самый датасет (Training loss 0.1817)
   1. Ответы стали корректные
   2. Есть минимальные ошибки в ответах, но не всегда, чаще ассистент отвечает правильно