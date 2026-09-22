import pandas as pd


REQUIRED_COLUMNS = [
    "PO Number",
    "Supplier Code",
    "Item Number",
    "Ordered",
    "Order Date",
]


def validate_columns(df):
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )


def validate_rows(df):
    errors = []

    for index, row in df.iterrows():

        if pd.isna(row["PO Number"]) or str(row["PO Number"]).strip() == "":
            errors.append(
                f"Row {index + 2}: PO Number is missing"
            )

        if pd.isna(row["Supplier Code"]) or str(row["Supplier Code"]).strip() == "":
            errors.append(
                f"Row {index + 2}: Supplier Code is missing"
            )

        if pd.isna(row["Item Number"]) or str(row["Item Number"]).strip() == "":
            errors.append(
                f"Row {index + 2}: Item Number is missing"
            )

        if pd.isna(row["Ordered"]) or row["Ordered"] <= 0:
            errors.append(
                f"Row {index + 2}: Ordered quantity must be greater than 0"
            )

        if pd.isna(row["Order Date"]) or str(row["Order Date"]).strip() == "":
            errors.append(
                f"Row {index + 2}: Order Date is missing"
            )
        else:
            try:
                pd.to_datetime(row["Order Date"])
            except (ValueError, TypeError):
                errors.append(
                    f"Row {index + 2}: Order Date is invalid"
                )

    if errors:
        raise ValueError("\n".join(errors))
