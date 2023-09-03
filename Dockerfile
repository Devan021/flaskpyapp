# Use the official Python Image
FROM python:3.9-slim


# Set the environmnet variables

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies 
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port your app runs on 
EXPOSE 5000

# Start the Application 
CMD ["python" , "app.py"]







