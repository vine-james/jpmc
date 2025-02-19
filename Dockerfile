# Step 1: Use an official Python runtime as a parent image
FROM python:3.12

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: update and install OS dependencies
# RUN apt-get update && apt-get install -y \
#     curl \
#     vim \
#     && apt-get clean

# Step 4: Copy the relevant directories contents into the container at /app (. when coppying)
COPY . /app

# COPY /banking .
# COPY /extra_credit_union .

# Step 5: Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Step 6: Make port 5000 available to the world outside this container
EXPOSE 5000

# ENV ENV_VAR=app.main.py:app
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

# # Step 7: Run the python application when the container starts
CMD ["python", "manage.py",  "runserver"]