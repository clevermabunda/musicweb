# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Install dependencies
# Copy the requirements file first to leverage Docker caching
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Step 5: Copy the current directory contents into the container at /app
COPY . /app/

# Step 6: Expose the port that the Django app will run on (default is 8000)
EXPOSE 8000

# Step 7: Set the entrypoint to run Django
# Using `ENTRYPOINT` allows the container to run any command as the default when started.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
