import pandas as pd

from api_client import (
    get_suppliers,
    get_products,
    create_purchase_order,
)
from validator import validate_columns, validate_rows
from transformer import transform_purchase_orders


FILE_PATH = "data/purchase_orders.xlsx"


def main():
    print("Starting ReceiveFlow data pipeline...")

    # 1. Read Excel
    print("Reading Excel file...")
    df = pd.read_excel(FILE_PATH)

    # 2. Validate Excel data
    print("Validating Excel data...")
    validate_columns(df)
    validate_rows(df)

    # 3. Get reference data from ReceiveFlow
    print("Fetching suppliers...")
    suppliers = get_suppliers()

    print("Fetching products...")
    products = get_products()

    # 4. Transform Excel data into API format
    print("Transforming purchase orders...")
    purchase_orders = transform_purchase_orders(
        df,
        suppliers,
        products,
    )

    print(f"Purchase orders found: {len(purchase_orders)}")

    # 5. Send purchase orders to ReceiveFlow
    for purchase_order in purchase_orders:
        print(
            f"Creating PO {purchase_order['poNumber']}..."
        )

        result = create_purchase_order(purchase_order)

        print(
            f"Created PO {result['poNumber']} "
            f"with ID {result['id']}"
        )

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Pipeline failed: {error}")
        raise SystemExit(1)