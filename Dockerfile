FROM python:3.10

# Set the work directory for the application
WORKDIR /app

# Add Utils to Docker
COPY /Utilities/Utils.py ./Utilities/Utils.py

# Add Scores file to Docker
COPY Scores.txt .

# Add Flask app to Docker
COPY MainScores.py .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install Flask


# Run Python script
CMD [ "python", "MainScores.py" ]