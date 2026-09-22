import pandas as pd

from validator import validate_columns, validate_rows


file_path = "data/purchase_orders.xlsx"

df = pd.read_excel(file_path)

validate_columns(df)
validate_rows(df)

print("Validation successful.")
print(f"Rows processed: {len(df)}")
