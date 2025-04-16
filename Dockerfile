FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application (replace with your app's entry point)
CMD ["python", "app.py"]
