def build_lookup(items, key):
    return {
        str(item[key]): item
        for item in items
    }


def transform_purchase_orders(df, suppliers, products):
    supplier_lookup = build_lookup(suppliers, "code")
    product_lookup = build_lookup(products, "articleNumber")

    purchase_orders = {}

    for _, row in df.iterrows():

        po_number = str(row["PO Number"]).strip()
        supplier_code = str(row["Supplier Code"]).strip()
        item_number = str(row["Item Number"]).strip()
        ordered = int(row["Ordered"])

        order_date = str(row["Order Date"]).strip()

        if supplier_code not in supplier_lookup:
            raise ValueError(
                f"Supplier not found: {supplier_code}"
            )

        if item_number not in product_lookup:
            raise ValueError(
                f"Product not found: {item_number}"
            )

        supplier = supplier_lookup[supplier_code]
        product = product_lookup[item_number]

        if not supplier["active"]:
            raise ValueError(
                f"Supplier is inactive: {supplier_code}"
            )

        if not product["active"]:
            raise ValueError(
                f"Product is inactive: {item_number}"
            )

        if po_number not in purchase_orders:
            purchase_orders[po_number] = {
                "poNumber": po_number,
                "supplierId": supplier["id"],
                "orderDate": order_date,
                "source": "EXCEL",
                "items": []
            }

        purchase_orders[po_number]["items"].append({
            "productId": product["id"],
            "quantityOrdered": ordered
        })

    return list(purchase_orders.values())
