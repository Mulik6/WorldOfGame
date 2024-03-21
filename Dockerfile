FROM python:3.10.14-slim

# Set the work directory for the application
WORKDIR /app

# Add python script to Docker
COPY /Utilities/Utils.py ./Utilities/Utils.py

# Add Scores file to Docker
COPY /Main/Scores.txt .
# Add python script to Docker
COPY /Main/MainScores.py .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install Flask


# Run Python script
CMD [ "python", "MainScores.py" ]