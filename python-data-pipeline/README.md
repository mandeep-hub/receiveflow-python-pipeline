# ReceiveFlow Python Data Pipeline

A Python data pipeline that imports purchase orders from Excel into the ReceiveFlow warehouse application.

## What it does

The pipeline:

1. Reads purchase orders from Excel using Pandas.
2. Validates the input data.
3. Fetches suppliers and products from the ReceiveFlow API.
4. Transforms Excel data into the API format.
5. Groups multiple Excel rows belonging to the same PO.
6. Sends purchase orders to ReceiveFlow through the REST API.
7. Tracks imported POs with source `EXCEL`.
8. Includes automated tests using Pytest.

## Data Flow

```text
Excel File
    ↓
Pandas
    ↓
Validation
    ↓
Transformation
    ↓
ReceiveFlow REST API
    ↓
PostgreSQL Database
```

## Technologies

- Python 3.10
- Pandas
- Requests
- OpenPyXL
- Pytest
- REST API
- PostgreSQL
- Node.js / TypeScript
- Prisma

## Project Structure

```text
python-data-pipeline/
├── data/
│   └── purchase_orders.xlsx
├── manual_tests/
│   └── manual_post_test.py
├── api_client.py
├── create_test_excel.py
├── main.py
├── read_excel.py
├── transformer.py
├── validator.py
├── test_validator.py
├── test_transformer.py
├── pytest.ini
└── requirements.txt
```

## Run the Pipeline

Start the ReceiveFlow API first.

Then:

```bash
cd python-data-pipeline
source .venv/bin/activate
python main.py
```

## Run Tests

```bash
pytest
```

## Example

Excel input:

```text
PO Number | Supplier Code | Item Number | Ordered
200262    | SUP003        | 1005        | 100
200262    | SUP003        | 1005        | 50
```

The pipeline groups the rows into one purchase order and sends it to ReceiveFlow.

## Purpose

This project demonstrates practical Python data engineering skills including:

- Data ingestion
- Data validation
- Data transformation
- API integration
- Error handling
- Automated testing
- Working with relational database-backed applications
