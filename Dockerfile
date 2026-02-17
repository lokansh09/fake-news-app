FROM python:3.11-slim

# Create a user
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Copy requirements and install
COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all files
COPY --chown=user . /app

# Expose HF port
EXPOSE 7860

# Start your Flask app with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
