# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run data preparation and training before starting the app
# Note: In a real production environment, you might separate specific build steps or use a volume for data.
# We chain them here to ensure the app has the necessary models to run.
CMD python data.py && python train.py && python app.py
