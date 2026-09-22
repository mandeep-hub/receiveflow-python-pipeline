import pandas as pd


data = [
    {
        "PO Number": "200262",
        "Supplier Code": "SUP003",
        "Item Number": "1005",
        "Ordered": 100,
        "Order Date": "2026-09-22",
    },
    {
        "PO Number": "200262",
        "Supplier Code": "SUP003",
        "Item Number": "1005",
        "Ordered": 50,
        "Order Date": "2026-09-22",
    },
    {
        "PO Number": "200263",
        "Supplier Code": "SUP001",
        "Item Number": "1005",
        "Ordered": 75,
        "Order Date": "2026-09-22",
    },
]


df = pd.DataFrame(data)

df.to_excel("data/purchase_orders.xlsx", index=False)

print("Excel file created successfully.")
