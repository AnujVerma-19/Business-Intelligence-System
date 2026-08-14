# Business Intelligence System

A Flask and MySQL based business intelligence web application for managing and analyzing products, customers, sales, and delivery performance.

## Overview

This project provides a centralized web interface for business data management and operational reporting. It combines CRUD operations with dashboard KPIs, search, pagination, sales summaries, and delivery analytics.

## Key Features

- Admin login and session-based page protection
- Dashboard with product, customer, sales, and delivery KPIs
- Product management
  - Add products
  - Edit products
  - Delete products
  - Search products
  - Pagination
- Customer management
  - Add customers
  - Edit customers
  - Delete customers
  - Search customers
  - Pagination
- Sales management
  - Add sales
  - Edit sales
  - Delete sales
  - Product/customer selection
  - Search and pagination
  - Sales summary
  - Monthly sales data
- Delivery performance
  - Delivery records
  - Search and pagination
  - Average delivery time
  - Average delivery distance
  - Delivery partner count
  - Delivery status summary
- Reports
  - Total sales
  - Total profit
  - Total orders
  - Total customers
  - Monthly sales and profit
  - Sales by category
  - Top products by sales
  - Delivery summary
- Responsive UI built with HTML, CSS, Bootstrap-style components, and JavaScript

## Technology Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Database Connector:** PyMySQL
- **Frontend:** HTML, CSS, JavaScript
- **Charts:** JavaScript-based chart/report visualizations
- **Development Environment:** VS Code / MySQL Workbench

## Project Structure

```text
blinkit_business_intelligence_system/
│
├── Backend/
│   ├── static/
│   │   └── style.css
│   ├── js/
│   │   ├── script.js
│   │   ├── sales.js
│   │   ├── delivery.js
│   │   └── reports.js
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
│   └── database.py
│
├── Frontend/
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── dashboard.html
│       ├── products.html
│       ├── add_product.html
│       ├── edit_product.html
│       ├── customers.html
│       ├── add_customer.html
│       ├── edit_customer.html
│       ├── sales.html
│       ├── add_sales.html
│       ├── edit_sales.html
│       ├── delivery.html
│       └── reports.html
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Database

The application works with MySQL tables for:

- Users
- Products
- Customers
- Sales
- Delivery performance

Sales records connect products and customers, allowing combined business reporting and analysis.

## Running the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd blinkit_business_intelligence_system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Update the database configuration in `Backend/config.py` with your local MySQL credentials and database name.

Do not upload real passwords or credentials to GitHub.

### 5. Run the Flask application

Run the application from the `Backend` directory:

```bash
python app.py
```

Then open the local address shown by Flask in your browser.

## Important Security Note

Before deploying this application publicly:

- Move database credentials to environment variables.
- Use a strong Flask secret key.
- Store passwords securely using password hashing instead of plain-text passwords.
- Add CSRF protection to forms.
- Use HTTPS in production.

## Project Purpose

The system demonstrates how a business can manage operational data and turn it into useful business information through dashboards, summaries, and reports.

## Future Improvements

- Role-based access control
- Secure password hashing
- Export reports to CSV/PDF
- Advanced filtering and date-range analysis
- Automated inventory alerts
- Sales forecasting
- REST API
- Production deployment
