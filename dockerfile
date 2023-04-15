# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production

# Set work directory to /app
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver"]
