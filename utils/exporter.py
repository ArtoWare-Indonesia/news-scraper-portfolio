from pathlib import Path
from datetime import datetime
import csv
import json
from openpyxl import Workbook


class Exporter:
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def to_csv(self, data, filename=None):
        if filename is None:
            filename = f"news_{self.timestamp}.csv"

        filepath = self.output_dir / filename

        if not data:
            return filepath

        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        return filepath

    def to_excel(self, data, filename=None):
        if filename is None:
            filename = f"news_{self.timestamp}.xlsx"

        filepath = self.output_dir / filename

        wb = Workbook()
        ws = wb.active
        ws.title = "News"

        if data:
            ws.append(list(data[0].keys()))
            for row in data:
                ws.append(list(row.values()))

        wb.save(filepath)

        return filepath

    def to_json(self, data, filename=None):
        if filename is None:
            filename = f"news_{self.timestamp}.json"

        filepath = self.output_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return filepath