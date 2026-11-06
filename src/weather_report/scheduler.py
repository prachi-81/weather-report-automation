
import time
import schedule

from weather_report.api import get_weather
from weather_report.report import generate_report


def create_scheduled_report(city, latitude, longitude):
    try:
        weather = get_weather(latitude, longitude)
        pdf = generate_report(city, weather)
        print(f"Report generated successfully: {pdf}")

    except Exception as error:
        print(f"Scheduled report failed: {error}")


def start_scheduler(city, latitude, longitude, report_time):
    schedule.every().day.at(report_time).do(
        create_scheduled_report,
        city,
        latitude,
        longitude
    )

    print(f"Daily report scheduled at {report_time}.")
    print("Keep this program running to generate reports.")

    while True:
        schedule.run_pending()
        time.sleep(30)
