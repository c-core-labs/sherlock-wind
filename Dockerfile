FROM python:3.8.8-slim

# Install the C compiler tools
RUN apt-get update -y && \
        apt-get install build-essential cmake wget git -y && \
        pip install --upgrade pip

# Requirements for cartopy
RUN apt-get install libproj-dev proj-data proj-bin -y
RUN apt-get install libgeos-dev -y
RUN pip install numpy

# Install application dependencies
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY .env ./.env
COPY cloud_storage.json ./cloud_storage.json

COPY sherlock_wind ./sherlock_wind
CMD ["python", "-m", "sherlock_wind.main"]
