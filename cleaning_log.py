import datetime

class CleaningEntry:
    def __init__(self, item, method, date, result):
        self.item = item
        self.method = method
        self.date = date
        self.result = result

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - Item: {self.item}, Method: {self.method}, Result: {self.result}"

class CleaningLog:
    def __init__(self):
        self.entries = []

    def log_entry(self, item, method, result):
        entry = CleaningEntry(item, method, datetime.datetime.now(), result)
        self.entries.append(entry)
        print(f"Entry logged.")

    def review_entries(self):
        for entry in self.entries:
            print(str(entry))

# Sample usage
if __name__ == "__main__":
    cleaning_log = CleaningLog()

    cleaning_log.log_entry("Toothbrush", "Soaked in water for a month", "Hard particles formed on glass. Suspected fluoride.")
    cleaning_log.log_entry("Kitchenware", "Cleaned with dish soap and water", "No noticeable change.")

    print("\nReviewing entries:")
    cleaning_log.review_entries()
