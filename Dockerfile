FROM python:3.9

# Install system dependencies
RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /opt/app

# Copy and install Python dependencies
COPY requirements.txt /opt/app/requirements.txt
RUN pip install -r requirements.txt

# Copy the application files
COPY . /opt/app

# Specify the command to run on container start
CMD ["python", "Hand_Recognition_System.py"]
