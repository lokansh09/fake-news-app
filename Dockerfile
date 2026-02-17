# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose HF Spaces default port
EXPOSE 7860

# Run Flask app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
