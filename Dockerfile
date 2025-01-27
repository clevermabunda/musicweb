# Step 1: Use a Python base image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt into the container
COPY requirements.txt .

# Step 4: Install system dependencies (if any required)
# For example, you may need to install build-essential or libpq-dev for certain Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Upgrade pip and install Python dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of your application code into the container
COPY band .

# Step 7: Set the environment variable for Django settings (optional)
# This step is optional if you're setting Django settings using environment variables
ENV DJANGO_SETTINGS_MODULE=band.settings

# Step 8: Expose the port the app will run on
EXPOSE 8000

# Step 10: Start the Django application using the built-in development server (for development only)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
