from api_client import create_purchase_order


purchase_order = {
    "poNumber": "200259",
    "supplierId": 9,
    "orderDate": "2026-09-22",
    "items": [
        {
            "productId": 3,
            "quantityOrdered": 25
        }
    ]
}


result = create_purchase_order(purchase_order)

print("Purchase order created:")
print(result)
