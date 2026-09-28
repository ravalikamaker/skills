import csv
import io


def event_csv(rows):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["date", "title"])
    writer.writerows((row["date"], row["title"]) for row in rows)
    return output.getvalue()


class EventScreen:
    def __init__(self, rows):
        self.rows = list(rows)
        self.cached = list(rows)

    def add(self, event):
        self.rows.append(event)

    def download(self):
        return event_csv(self.cached)
