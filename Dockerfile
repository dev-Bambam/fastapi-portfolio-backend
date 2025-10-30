# 1. BASE IMAGE: Use a fully qualified tag for reproducibility.
# Using 'slim-bullseye' or 'slim-bookworm' is better than just 'slim'.
# I'll default to the stable Bullseye distribution.
FROM python:3.12-slim-bookworm

# 2. ENVIRONMENT: Crucial for production; disables output buffering.
ENV PYTHONUNBUFFERED 1

# 3. WORKDIR: Set the working directory inside the container.
WORKDIR /app

# 4. COPY & INSTALL: Leverage caching by installing dependencies first.
COPY requirements.txt .

# Use --no-cache-dir for a small image.
RUN pip install --no-cache-dir -r requirements.txt

# 5. COPY CODE: Copy the rest of the application code.
COPY . . 

# 6. EXPOSE: Declare the port that the application listens on.
# FastAPI/Uvicorn defaults to 8000, not 8080, so we adjust this.
EXPOSE 8000

# 7. CMD: Define the entrypoint. This is the most important change.
# We explicitly bind to 0.0.0.0 (required inside Docker) and use the correct port.
# The --host 0.0.0.0 flag tells Uvicorn to listen on all network interfaces
# within the container, making it accessible from outside.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
