ReceiveFlow Python Data Pipeline

A Python data pipeline built as part of the ReceiveFlow warehouse receiving application.

The pipeline imports purchase orders from Excel into ReceiveFlow, validates and transforms the data, integrates with the ReceiveFlow REST API, and generates an Excel receiving report.

Business Problem

Purchase orders can originate from external systems such as QLIK and be provided as Excel data.

The warehouse needs to:

Import purchase orders efficiently

Validate supplier, product, quantity, and date information

Register purchase orders in ReceiveFlow

Record received quantities and delivery discrepancies

Provide a report for the Buying Department

The Python pipeline automates the data ingestion, transformation, API integration, and reporting parts of this workflow.

Architecture

Excel / PO Data
      |
      v
Python Pipeline
(Pandas + Validation + Transformation)
      |
      | REST API
      v
ReceiveFlow API
(Node.js + TypeScript)
      |
      v
PostgreSQL
      |
      v
Warehouse Receiving
      |
      v
Receiving API
      |
      v
Python Reporting
      |
      v
Excel Report

Python Data Pipeline

The purchase order pipeline performs the following steps:

Reads purchase orders from Excel using Pandas.

Validates required columns and row values.

Fetches suppliers and products from the ReceiveFlow API.

Validates supplier and product mappings.

Rejects inactive suppliers or products.

Transforms Excel records into the ReceiveFlow API format.

Groups multiple Excel rows belonging to the same purchase order.

Sends purchase orders to ReceiveFlow through the REST API.

Tracks imported purchase orders with source EXCEL.

Receiving Report Pipeline

The reporting pipeline:

Retrieves receiving data from the ReceiveFlow API.

Loads the API response into a Pandas DataFrame.

Calculates delivery status:

Short delivery

Complete

Over delivery

Creates summary metrics.

Exports the report to Excel.

Uses OpenPyXL to format the workbook.

The generated workbook contains two sheets:

Summary

Receiving Report

The Receiving Report includes:

PO number

Supplier

Article number

Product

Ordered quantity

Received quantity

Remaining quantity

Difference

Reason code

Action status

EP count

Delivery status

Data Flow

Purchase Order Import

Excel
  |
  v
Pandas
  |
  v
Validation
  |
  v
Supplier/Product Lookup
  |
  v
Transformation
  |
  v
ReceiveFlow REST API
  |
  v
PostgreSQL

Receiving Report

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

Technologies

Python

Python 3.10

Pandas

Requests

OpenPyXL

Pytest

Backend

Node.js

TypeScript

Express

Prisma

PostgreSQL

Integration

REST API

Excel data processing

Project Structure

receiveflow-python-pipeline/

apps/
  api/
    src/
      server.ts

python-data-pipeline/
  data/
    purchase_orders.xlsx

  manual_tests/
    manual_post_test.py

  api_client.py
  create_test_excel.py
  main.py
  read_excel.py
  receiving_report.py
  transformer.py
  validator.py
  test_validator.py
  test_transformer.py
  pytest.ini
  requirements.txt

README.md

Example

Example Excel input:

PO Number | Supplier Code | Item Number | Ordered
200262    | SUP003        | 1005        | 100
200262    | SUP003        | 1005        | 50

The pipeline groups the rows belonging to PO 200262 and transforms them into the structure expected by the ReceiveFlow API.

Receiving Example

A receiving record can contain:

Ordered:       100
Delivered:      95
Difference:     -5
Status:        Short delivery
Reason:        PARTIAL_DELIVERY

The Python reporting pipeline retrieves this information and includes it in the generated Excel report.

Testing

The Python pipeline contains automated tests using Pytest.

Current tests cover:

Valid Excel data

Missing required columns

Invalid quantities

Invalid order dates

Valid purchase order transformation

Unknown suppliers

Unknown products

Inactive products

Run the tests with:

pytest

Current result:

8 passed

Running the Pipeline

Start the ReceiveFlow API first.

From the project root:

cd apps/api
yarn dev

Then open another terminal:

cd python-data-pipeline
source .venv/bin/activate
python main.py

Generate Receiving Report

With the ReceiveFlow API running:

cd python-data-pipeline
source .venv/bin/activate
python receiving_report.py

The report is generated at:

data/receiving_report.xlsx

Purpose

This project demonstrates practical software and data engineering skills including:

Data ingestion

Data validation

Data transformation

Data mapping

REST API integration

Pandas data processing

Excel processing

Business-rule implementation

Automated testing

Error handling

Reporting

Working with a relational database