
import argparse

from weather_report.api import get_weather
from weather_report.report import generate_report
from weather_report.scheduler import start_scheduler


def main():
    parser = argparse.ArgumentParser(
        description="Automated Weather PDF Report Generator"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Generate command
    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument("--city", required=True)
    generate_parser.add_argument("--latitude", type=float, required=True)
    generate_parser.add_argument("--longitude", type=float, required=True)

    # Schedule command
    schedule_parser = subparsers.add_parser("schedule")
    schedule_parser.add_argument("--city", required=True)
    schedule_parser.add_argument("--latitude", type=float, required=True)
    schedule_parser.add_argument("--longitude", type=float, required=True)
    schedule_parser.add_argument("--time", default="08:00")

    args = parser.parse_args()

    if args.command == "generate":
        try:
            weather = get_weather(args.latitude, args.longitude)
            pdf = generate_report(args.city, weather)
            print(f"PDF report created successfully: {pdf}")

        except Exception as error:
            print(f"Error: {error}")

    elif args.command == "schedule":
        start_scheduler(
            args.city,
            args.latitude,
            args.longitude,
            args.time
        )


if __name__ == "__main__":
    main()
