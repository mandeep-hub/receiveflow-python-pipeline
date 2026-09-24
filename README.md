# ReceiveFlow

A full-stack warehouse receiving application designed around real-world purchase order, goods receiving, inventory, and delivery discrepancy workflows.

ReceiveFlow combines a React frontend, Node.js/TypeScript REST API, PostgreSQL database, and Python data pipeline for purchase-order ingestion and receiving reporting.

## Overview

ReceiveFlow helps warehouse operations manage purchase orders and goods receiving while capturing delivery quantities and discrepancies.

The application covers:

- Purchase order management
- Supplier and product management
- Goods receiving
- Delivery discrepancy tracking
- Reason codes and action statuses
- EP box counting
- End-of-day receiving reports
- Excel-based purchase-order import
- Python data validation and transformation

## Architecture

```text
                         ReceiveFlow
                              |
             +----------------+----------------+
             |                                 |
             v                                 v
       React Frontend                 Python Data Pipeline
             |                                 |
             v                                 v
    Node.js / TypeScript API          Excel / Pandas
             |                                 |
             v                                 v
        PostgreSQL                  Validation & Transformation
             |                                 |
             v                                 v
    Warehouse Receiving             REST API Integration
             |                                 |
             v                                 v
       Receiving Data                 Excel Reporting
```

## Python Data Pipeline

The Python pipeline handles the data-processing part of ReceiveFlow.

It imports purchase-order data from Excel, validates and transforms the data, integrates with the ReceiveFlow REST API, and generates Excel receiving reports.

### Purchase Order Import Pipeline

```text
Excel / PO Data
      |
      v
Pandas
      |
      v
Validation
      |
      v
Supplier / Product Mapping
      |
      v
Transformation
      |
      v
ReceiveFlow REST API
      |
      v
PostgreSQL
```

The pipeline:

- Imports purchase orders from Excel using Pandas
- Validates required columns and row values
- Validates supplier and product mappings
- Rejects unknown or inactive suppliers and products
- Validates quantities and order dates
- Groups multiple Excel rows belonging to the same purchase order
- Transforms Excel records into the ReceiveFlow API format
- Sends purchase orders to the ReceiveFlow REST API
- Tracks imported purchase orders with the Excel source

## Receiving Report Pipeline

The reporting pipeline retrieves receiving information from the ReceiveFlow API and generates an Excel report.

```text
ReceiveFlow REST API
        |
        v
      Python
        |
        v
      Pandas
        |
        v
 Business Rules
        |
        v
    OpenPyXL
        |
        v
 Excel Report
```

The report includes:

- PO number
- Supplier
- Article number
- Product
- Ordered quantity
- Received quantity
- Remaining quantity
- Difference
- Reason code
- Action status
- EP count
- Delivery status

Delivery status is calculated as:

- Short delivery
- Complete
- Over delivery

## Example

Example purchase-order data:

```text
PO Number | Supplier Code | Item Number | Ordered
200262    | SUP003        | 1005        | 100
200262    | SUP003        | 1005        | 50
```

The pipeline groups the rows belonging to the same purchase order and transforms them into the structure required by the ReceiveFlow API.

Example receiving result:

```text
Ordered:    100
Delivered:   95
Difference:  -5
Status:     Short delivery
Reason:     PARTIAL_DELIVERY
```

## Data Validation

The Python pipeline performs validation before data is sent to the API.

Validation includes:

- Required Excel columns
- Missing values
- Quantity validation
- Order date validation
- Supplier lookup
- Product lookup
- Supplier activity status
- Product activity status
- Purchase-order data structure

Invalid data is rejected before being sent to ReceiveFlow.

## Testing

The Python pipeline uses Pytest for automated testing.

Current test result:

```text
8 passed
```

Tests cover:

- Valid Excel data
- Missing required columns
- Invalid quantities
- Invalid order dates
- Valid purchase-order transformation
- Unknown suppliers
- Unknown products
- Inactive products

Run the tests with:

```bash
pytest
```

## Technologies

### Python

- Python 3.10
- Pandas
- Requests
- OpenPyXL
- Pytest

### Backend

- Node.js
- TypeScript
- Express
- Prisma
- PostgreSQL

### Frontend

- React
- Vite
- TypeScript
- Tailwind CSS
- shadcn/ui

### Integration

- REST API
- Excel data processing
- Data validation
- Data transformation
- Automated testing
- Excel reporting

## Project Structure

```text
receiveflow-python-pipeline/
│
├── apps/
│   └── api/
│       └── src/
│           └── server.ts
│
├── prisma/
│
├── python-data-pipeline/
│   ├── data/
│   │   └── purchase_orders.xlsx
│   │
│   ├── manual_tests/
│   │   └── manual_post_test.py
│   │
│   ├── api_client.py
│   ├── create_test_excel.py
│   ├── main.py
│   ├── read_excel.py
│   ├── receiving_report.py
│   ├── transformer.py
│   ├── validator.py
│   ├── test_transformer.py
│   ├── test_validator.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── README.md
│
├── package.json
├── prisma.config.ts
├── README.md
└── yarn.lock
```

## Running the Project

### Start the ReceiveFlow API

From the project root:

```bash
cd apps/api
yarn dev
```

The API runs on:

```text
http://localhost:3000
```

### Run the Python Pipeline

In another terminal:

```bash
cd python-data-pipeline
source .venv/bin/activate
python main.py
```

### Generate Receiving Report

With the API running:

```bash
cd python-data-pipeline
source .venv/bin/activate
python receiving_report.py
```

The report is generated at:

```text
data/receiving_report.xlsx
```

## Project Purpose

ReceiveFlow was developed to explore how software and data engineering can improve real-world warehouse receiving workflows.

The project combines practical warehouse domain knowledge with software development concepts including:

- Data ingestion
- Data validation
- Data transformation
- Data mapping
- REST API integration
- Relational databases
- Automated testing
- Business-rule implementation
- Excel processing
- Reporting

## Detailed Python Documentation

For detailed documentation of the Python data pipeline, including validation, transformation, API integration, reporting, and examples, see:

`python-data-pipeline/README.md`
