
from pathlib import Path
from datetime import datetime
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)


def generate_report(city, weather):
    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    safe_city = re.sub(r"[^a-zA-Z0-9_-]", "_", city)

    filename = (
        f"{safe_city}_weather_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    )

    pdf_path = reports_folder / filename
    chart_path = reports_folder / "temperature_chart.png"

    dates = weather["time"]
    maximum = weather["temperature_2m_max"]
    minimum = weather["temperature_2m_min"]
    rain = weather["precipitation_probability_max"]

    # Calculate summary statistics
    average_temp = sum(maximum) / len(maximum)
    highest_temp = max(maximum)
    lowest_temp = min(minimum)

    # Create temperature chart
    plt.figure(figsize=(8, 4))
    plt.plot(dates, maximum, marker="o", label="Maximum")
    plt.plot(dates, minimum, marker="o", label="Minimum")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"7-Day Weather Forecast - {city}")
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    # Create PDF
    document = SimpleDocTemplate(str(pdf_path))
    styles = getSampleStyleSheet()
    content = []

    content.append(
        Paragraph(f"Weather Report - {city}", styles["Title"])
    )
    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )
    content.append(Spacer(1, 15))

    content.append(Paragraph("Weather Summary", styles["Heading2"]))

    summary = [
        ["Metric", "Value"],
        ["Average maximum temperature", f"{average_temp:.1f} °C"],
        ["Highest temperature", f"{highest_temp:.1f} °C"],
        ["Lowest temperature", f"{lowest_temp:.1f} °C"]
    ]

    summary_table = Table(summary)
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("GRID", (0, 0), (-1, -1), 1, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 8)
    ]))

    content.append(summary_table)
    content.append(Spacer(1, 20))

    content.append(
        Paragraph("Daily Forecast", styles["Heading2"])
    )

    rows = [["Date", "Max °C", "Min °C", "Rain %"]]

    for i in range(len(dates)):
        rows.append([
            dates[i],
            maximum[i],
            minimum[i],
            rain[i]
        ])

    forecast_table = Table(rows)
    forecast_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("GRID", (0, 0), (-1, -1), 1, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 6)
    ]))

    content.append(forecast_table)
    content.append(Spacer(1, 20))

    content.append(
        Paragraph("Temperature Chart", styles["Heading2"])
    )
    content.append(Image(str(chart_path), width=450, height=225))

    document.build(content)

    return pdf_path
