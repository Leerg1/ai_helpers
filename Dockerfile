FROM ollama/ollama:latest

# Убираем ENTRYPOINT ollama
ENTRYPOINT []

ENV PYTHONPATH=/app

# Устанавливаем Python и pip
RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Установка зависимостей Python
RUN pip3 install --no-cache-dir --break-system-packages fastapi uvicorn httpx pydantic requests

EXPOSE 8000 11434

# Стартуем ollama, ждём, грузим модель, стартуем API
CMD ["bash", "-c", "\
    ollama serve & \
    sleep 5 && \
    ollama pull deepseek-coder:6.7b-instruct-q8_0 && \
    uvicorn reviewer.main:app --host 0.0.0.0 --port 8000 \
"]


# docker build -t ai_helpers:latest .
# docker run -d -p 8000:8000 -p 11434:11434 --name ai_helpers ai_helpers:latest

# curl http://localhost:8000/docs


#Прогрев
#curl -s -X POST http://localhost:8000/api/ai_review_deepseek_coder_6_7 \
#  -H "Content-Type: application/json" \
#  -d '{"code": "a==1"}'

#curl http://localhost:11434/api/generate \
#  -d '{"model": "deepseek-coder:1.3b", "prompt": "test", "stream": false}' \
#  | jq

#передать файл
#docker cp /Users/vlad/PycharmProjects/PythonProject/ai_helpers/reviewer/routers/reviewer.py ai_helpers:/app/reviewer