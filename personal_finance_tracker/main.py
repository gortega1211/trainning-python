import pandas as pd # type: ignore
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.CSV_FILE, index=False)

if __name__ == "__main__":
    CSV.initialize_csv()