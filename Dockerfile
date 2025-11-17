FROM ollama/ollama:latest

# Убираем ENTRYPOINT ollama
ENTRYPOINT []

# Устанавливаем Python и pip
RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./reviewer /app

# Установка зависимостей Python
RUN pip3 install --no-cache-dir --break-system-packages fastapi uvicorn httpx pydantic requests

EXPOSE 8000 11434

# Стартуем ollama, ждём, грузим модель, стартуем API
CMD ["bash", "-c", "\
    ollama serve & \
    sleep 10 && \
    ollama pull qwen2.5-coder:7b-base && \
    uvicorn reviewer.main:app --host 0.0.0.0 --port 8000 \
"]



# docker build -t ai_helpers:latest .
# docker run -d -p 8000:8000 -p 11434:11434 --name ai_helpers ai_helpers:latest
# curl http://localhost:8000/docs
# curl http://localhost:11434/api/tags