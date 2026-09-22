import pandas as pd
import pytest

from validator import validate_columns, validate_rows


def test_valid_data():
    df = pd.DataFrame([
        {
            "PO Number": "200300",
            "Supplier Code": "SUP003",
            "Item Number": "1005",
            "Ordered": 100,
            "Order Date": "2026-09-22",
        }
    ])

    validate_columns(df)
    validate_rows(df)


def test_missing_required_column():
    df = pd.DataFrame([
        {
            "PO Number": "200300",
            "Supplier Code": "SUP003",
            "Item Number": "1005",
            "Ordered": 100,
        }
    ])

    with pytest.raises(ValueError, match="Missing columns"):
        validate_columns(df)


def test_invalid_quantity():
    df = pd.DataFrame([
        {
            "PO Number": "200300",
            "Supplier Code": "SUP003",
            "Item Number": "1005",
            "Ordered": -10,
            "Order Date": "2026-09-22",
        }
    ])

    with pytest.raises(
        ValueError,
        match="Ordered quantity must be greater than 0"
    ):
        validate_rows(df)


def test_invalid_order_date():
    df = pd.DataFrame([
        {
            "PO Number": "200300",
            "Supplier Code": "SUP003",
            "Item Number": "1005",
            "Ordered": 100,
            "Order Date": "wrong-date",
        }
    ])

    with pytest.raises(
        ValueError,
        match="Order Date is invalid"
    ):
        validate_rows(df)