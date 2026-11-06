# Weather Report Automation System

## Project Description
A Python automation application that collects weather forecast data using a public API, processes the data, and generates PDF weather reports with temperature charts.

## Features
- Fetches weather data using an API.
- Processes temperature information.
- Generates PDF reports.
- Creates temperature charts.
- Supports automatic daily report scheduling.
- Provides command-line operations.

## Technologies Used
- Python
- FastAPI-free Open-Meteo Weather API
- Requests
- ReportLab
- Matplotlib
- Schedule
- Argparse

## Installation

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd weather-report-automation
python -m venv venv
```

Activate the virtual environment and install:

```bash
python -m pip install -e .
```

## Generate a Report

```bash
weather-report generate --city Mumbai --latitude 19.0760 --longitude 72.8777
```

## Schedule a Daily Report

```bash
weather-report schedule --city Mumbai --latitude 19.0760 --longitude 72.8777 --time 08:00
```

## Output
PDF weather reports and temperature charts are saved in the `reports` folder.

## API Source
Open-Meteo: https://open-meteo.com/

## Author
Prachi Tatyasaheb Bhosale