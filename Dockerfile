FROM ollama/ollama:latest

ENTRYPOINT []

ENV PYTHONPATH=/app

# Установка Python и pip
RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Установка зависимостей Python
RUN pip3 install --no-cache-dir --break-system-packages fastapi uvicorn httpx pydantic requests

EXPOSE 8000 11434

# Стартуем ollama, стартуем API
CMD ["bash", "-c", "\
    ollama serve & \
    sleep 5 && \
    uvicorn reviewer.main:app --host 0.0.0.0 --port 8000 --reload \
"]














# docker build -t ai_helpers:latest .
# docker run -d -p 8000:8000 -p 11434:11434 --name ai_helpers ai_helpers:latest


#Прогрев
#curl -s -X POST http://localhost:8000/api/ai_review_deepseek_coder_6_7 \
#  -H "Content-Type: application/json" \
#  -d '{"code": "a==1"}'

#docker cp /Users/vlad/PycharmProjects/PythonProject/ai_helpers/reviewer/routers/reviewer.py ai_helpers:/app/reviewer/routers
#docker cp /Users/vlad/PycharmProjects/PythonProject/ai_helpers/reviewer/services/ollama_client.py ai_helpers:/app/reviewer/services