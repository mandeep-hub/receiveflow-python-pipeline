import requests


BASE_URL = "http://localhost:3000"


def get_suppliers():
    response = requests.get(f"{BASE_URL}/suppliers")
    response.raise_for_status()
    return response.json()


def get_products():
    response = requests.get(f"{BASE_URL}/products")
    response.raise_for_status()
    return response.json()


def create_purchase_order(purchase_order):
    response = requests.post(
        f"{BASE_URL}/purchase-orders",
        json=purchase_order
    )

    response.raise_for_status()

    return response.json()


def get_receiving_report(date):
    response = requests.get(
        f"{BASE_URL}/receivings/report",
        params={"date": date},
        timeout=10,
    )

    response.raise_for_status()

    return response.json()
