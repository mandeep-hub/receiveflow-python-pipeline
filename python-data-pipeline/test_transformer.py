import pandas as pd
import pytest

from transformer import transform_purchase_orders


SUPPLIERS = [
    {
        "id": 9,
        "code": "SUP003",
        "name": "ABC supplier",
        "active": True,
    },
    {
        "id": 1,
        "code": "SUP001",
        "name": "Fresh Fruits Denmark",
        "active": True,
    },
]


PRODUCTS = [
    {
        "id": 3,
        "articleNumber": "1005",
        "name": "Pink Lady",
        "active": True,
    },
]


def test_transform_purchase_orders():
    df = pd.DataFrame([
        {
            "PO Number": "200300",
            "Supplier Code": "SUP003",
            "Item Number": "1005",
            "Ordered": 100,
            "Order Date": "2026-09-22",
        },
        {
            "PO Number": "200300",
            "Supplier Code": "SUP003",
            "Item Number": "1005",
            "Ordered": 50,
            "Order Date": "2026-09-22",
        },
    ])

    result = transform_purchase_orders(
        df,
        SUPPLIERS,
        PRODUCTS,
    )

    assert len(result) == 1
    assert result[0]["poNumber"] == "200300"
    assert result[0]["supplierId"] == 9
    assert result[0]["source"] == "EXCEL"
    assert result[0]["orderDate"] == "2026-09-22"

    assert len(result[0]["items"]) == 2
    assert result[0]["items"][0]["productId"] == 3
    assert result[0]["items"][0]["quantityOrdered"] == 100
    assert result[0]["items"][1]["quantityOrdered"] == 50


def test_unknown_supplier():
    df = pd.DataFrame([
        {
            "PO Number": "200301",
            "Supplier Code": "UNKNOWN",
            "Item Number": "1005",
            "Ordered": 100,
            "Order Date": "2026-09-22",
        }
    ])

    with pytest.raises(ValueError, match="Supplier not found"):
        transform_purchase_orders(
            df,
            SUPPLIERS,
            PRODUCTS,
        )


def test_unknown_product():
    df = pd.DataFrame([
        {
            "PO Number": "200302",
            "Supplier Code": "SUP003",
            "Item Number": "9999",
            "Ordered": 100,
            "Order Date": "2026-09-22",
        }
    ])

    with pytest.raises(ValueError, match="Product not found"):
        transform_purchase_orders(
            df,
            SUPPLIERS,
            PRODUCTS,
        )


def test_inactive_product():
    inactive_products = [
        {
            "id": 1,
            "articleNumber": "1001",
            "name": "Green Apples",
            "active": False,
        }
    ]

    df = pd.DataFrame([
        {
            "PO Number": "200303",
            "Supplier Code": "SUP003",
            "Item Number": "1001",
            "Ordered": 100,
            "Order Date": "2026-09-22",
        }
    ])

    with pytest.raises(ValueError, match="Product is inactive"):
        transform_purchase_orders(
            df,
            SUPPLIERS,
            inactive_products,
        )