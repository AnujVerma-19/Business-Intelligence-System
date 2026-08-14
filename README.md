# Business Intelligence System

A full-stack **Business Intelligence System** built with **Flask, MySQL, HTML, CSS and JavaScript** to manage business data and provide analytical insights through dashboards and reports.

## 🚀 Project Overview

The Business Intelligence System is designed to manage and analyze business operations from a centralized application.

It provides modules for:

* Product management
* Customer management
* Sales management
* Delivery performance tracking
* Business dashboards
* Analytical reports
* Search and filtering
* CRUD operations
* Database-driven analytics

The system combines **business data management with analytics**, making it useful for understanding sales performance, customer activity, product information and delivery operations.

## 🎯 Objectives

* Centralize business data in a structured MySQL database
* Provide an easy-to-use web interface for managing business records
* Track sales and customer activity
* Monitor delivery performance
* Generate meaningful business insights
* Provide a foundation for data-driven decision making

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* Python
* Flask
* Jinja2

### Database

* MySQL
* SQLAlchemy
* PyMySQL

### Data & Analytics

* Pandas
* NumPy
* JavaScript-based charts

### Development Tools

* VS Code
* Git
* GitHub

## 📦 Main Modules

### 1. Dashboard

The dashboard provides an overview of important business KPIs such as:

* Total Products
* Total Customers
* Total Sales
* Delivery Information
* Quick access to major modules

### 2. Product Management

The product module allows users to:

* View products
* Add products
* Edit products
* Delete products
* Search products
* Manage product information

### 3. Customer Management

The customer module manages:

* Customer name
* Email
* Phone number
* Address
* Area
* Pincode
* Customer segment
* Total orders
* Average order value

It also supports customer search and CRUD operations.

### 4. Sales Management

The sales module tracks:

* Product
* Customer
* Sale date
* Quantity
* Sales amount
* Discount
* Profit

It also provides sales summaries and visual analytics.

### 5. Delivery Performance

The delivery module tracks:

* Order information
* Delivery partner
* Promised time
* Actual delivery time
* Delivery duration
* Distance
* Delivery status
* Delay reasons

This helps identify delivery performance and operational issues.

### 6. Reports & Analytics

The reports section provides visual insights into business performance using charts and summary metrics.

Examples include:

* Sales trends
* Sales performance
* Profit analysis
* Delivery performance
* Customer-related insights

## 🗄️ Database

The application uses a MySQL database named:

`blinkit_sales_analytics`

The database stores business entities such as:

* Products
* Customers
* Sales
* Delivery performance

Relationships between business entities allow the application to retrieve and analyze connected business information.

## 📁 Project Structure

```text
Business Intelligence System/
│
├── Backend/
│   ├── static/
│   │   ├── style.css
│   │   └── js/
│   │       ├── script.js
│   │       ├── sales.js
│   │       ├── delivery.js
│   │       └── reports.js
│   │
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   └── routes.py
│
├── Frontend/
│   └── templates/
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
├── Dataset/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AnujVerma-19/Business-Intelligence-System.git
```

```bash
cd Business-Intelligence-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the database

Create the MySQL database:

```sql
CREATE DATABASE blinkit_sales_analytics;
```

Configure the database credentials in the local environment configuration.

**Do not upload database passwords or other secrets to GitHub.**

### 6. Run the application

```bash
python Backend/app.py
```

The application will be available locally through the Flask development server.

## 🔐 Security

Sensitive configuration such as database passwords is kept outside the public repository using environment variables.

The `.env` file is excluded through `.gitignore`.

## 📊 Business Value

The system can help a business monitor:

* Product information
* Customer activity
* Sales performance
* Profitability
* Order activity
* Delivery efficiency

By bringing these areas together, the application provides a centralized view of business operations and supports data-driven decision making.

## 🔮 Future Enhancements

Possible future improvements include:

* Role-based user authentication
* Advanced sales forecasting
* Customer segmentation
* Inventory management
* Automated KPI alerts
* Advanced interactive analytics
* Export reports to PDF/Excel
* REST API integration
* Cloud deployment
* Power BI integration

## 👨‍💻 Author

**Anuj Verma**

BCA Student | Aspiring Data Analyst

GitHub:
https://github.com/AnujVerma-19

## ⭐ Project

If you find this project useful, consider giving the repository a star.

