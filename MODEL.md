# MODEL

## Database Design

The project uses Django ORM with SQLite database.

## Main Model

EmissionRecord

Fields:
- company_name
- amount
- facility_name
- status
- source_type
- is_suspicious

## Features

- CRUD operations
- CSV upload support
- Suspicious emission detection
- Search and filtering
- Emission dashboard

## Audit Logic

If amount is greater than 500, record is marked suspicious.

## Source Types

- SAP
- Utility
- Travel