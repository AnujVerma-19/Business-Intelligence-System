import pymysql
from database import get_connection

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT * FROM users
    WHERE username=%s AND password=%s
    """

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user
from database import get_connection

def get_dashboard_counts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")
    products = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM customers")
    customers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sales")
    sales = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM delivery_performance")
    deliveries = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {
        "products": products,
        "customers": customers,
        "sales": sales,
        "deliveries": deliveries
    }
def get_all_products():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products
def add_product(product_name, category, brand, price, mrp):

    conn = get_connection()
    cursor = conn.cursor()

    # Next Product ID nikalna
    cursor.execute("SELECT IFNULL(MAX(product_id), 0) + 1 FROM products")
    new_id = cursor.fetchone()[0]

    query = """
    INSERT INTO products
    (product_id, product_name, category, brand, price, mrp)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        new_id,
        product_name,
        category,
        brand,
        price,
        mrp
    ))

    conn.commit()

    cursor.close()
    conn.close()
def get_product_by_id(product_id):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(
        "SELECT * FROM products WHERE product_id=%s",
        (product_id,)
    )

    product = cursor.fetchone()

    cursor.close()
    conn.close()

    return product


def update_product(product_id, product_name, category, brand, price, mrp):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE products
    SET
        product_name=%s,
        category=%s,
        brand=%s,
        price=%s,
        mrp=%s
    WHERE product_id=%s
    """

    cursor.execute(query, (
        product_name,
        category,
        brand,
        price,
        mrp,
        product_id
    ))

    conn.commit()

    cursor.close()
    conn.close()
def delete_product(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE product_id=%s",
        (product_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()    
def search_products(keyword):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT *
    FROM products
    WHERE product_name LIKE %s
       OR category LIKE %s
       OR brand LIKE %s
    """

    search = "%" + keyword + "%"

    cursor.execute(query, (search, search, search))

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products
def get_products_paginated(offset, limit):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(
        "SELECT * FROM products ORDER BY product_id LIMIT %s OFFSET %s",
        (limit, offset)
    )

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products


def get_total_products():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

def get_all_customers():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return customers
def add_customer(
    name,
    email,
    address,
    phone_no,
    area,
    pincode,
    registration_no,
    customer_segment,
    total_order,
    avg_order
):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO customers
    (
        name,
        email,
        address,
        phone_no,
        area,
        pincode,
        registration_no,
        customer_segment,
        total_order,
        avg_order
    )

    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(
        name,
        email,
        address,
        phone_no,
        area,
        pincode,
        registration_no,
        customer_segment,
        total_order,
        avg_order
    ))

    conn.commit()

    cursor.close()
    conn.close()
def get_customer_by_id(customer_id):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(
        "SELECT * FROM customers WHERE id=%s",
        (customer_id,)
    )

    customer = cursor.fetchone()

    cursor.close()
    conn.close()

    return customer


def update_customer(
    customer_id,
    name,
    email,
    address,
    phone_no,
    area,
    pincode,
    registration_no,
    customer_segment,
    total_order,
    avg_order
):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE customers
    SET
        name=%s,
        email=%s,
        address=%s,
        phone_no=%s,
        area=%s,
        pincode=%s,
        registration_no=%s,
        customer_segment=%s,
        total_order=%s,
        avg_order=%s
    WHERE id=%s
    """

    cursor.execute(query, (
        name,
        email,
        address,
        phone_no,
        area,
        pincode,
        registration_no,
        customer_segment,
        total_order,
        avg_order,
        customer_id
    ))

    conn.commit()

    cursor.close()
    conn.close()
def delete_customer(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE id=%s",
        (customer_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()
def search_customers(keyword, limit, offset):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT *
    FROM customers
    WHERE name LIKE %s
       OR email LIKE %s
       OR phone_no LIKE %s
    ORDER BY id
    LIMIT %s OFFSET %s
    """

    search = "%" + keyword + "%"

    cursor.execute(
        query,
        (search, search, search, limit, offset)
    )

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return customers
def get_customer_search_count(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM customers
    WHERE name LIKE %s
       OR email LIKE %s
       OR phone_no LIKE %s
    """

    search = "%" + keyword + "%"

    cursor.execute(query, (search, search, search))

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total
def get_customers_paginated(limit, offset):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT *
    FROM customers
    ORDER BY id
    LIMIT %s OFFSET %s
    """

    cursor.execute(query, (limit, offset))

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return customers


def get_total_customers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total
def get_sales_paginated(limit, offset):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT
        s.sale_id,
        s.sale_date,
        s.quantity,
        s.sales_amount,
        s.discount,
        s.profit,

        p.product_name,

        c.name AS customer_name

    FROM sales s

    LEFT JOIN products p
        ON s.product_id = p.product_id

    LEFT JOIN customers c
        ON s.customer_id = c.id

    ORDER BY s.sale_id

    LIMIT %s OFFSET %s
    """

    cursor.execute(query, (limit, offset))

    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales
def get_total_sales():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM sales")

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total
def add_sale(product_id, customer_id, sale_date, quantity, sales_amount, discount, profit):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO sales
    (
        product_id,
        customer_id,
        sale_date,
        quantity,
        sales_amount,
        discount,
        profit
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        product_id,
        customer_id,
        sale_date,
        quantity,
        sales_amount,
        discount,
        profit
    ))

    conn.commit()

    cursor.close()
    conn.close()
def get_products_for_sale():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("""
        SELECT product_id, product_name
        FROM products
        ORDER BY product_name
    """)

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products


def get_customers_for_sale():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("""
        SELECT id, name
        FROM customers
        ORDER BY name
    """)

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return customers
def get_sale_by_id(sale_id):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("""
        SELECT
            sale_id,
            product_id,
            customer_id,
            sale_date,
            quantity,
            sales_amount,
            discount,
            profit
        FROM sales
        WHERE sale_id = %s
    """, (sale_id,))

    sale = cursor.fetchone()

    cursor.close()
    conn.close()

    return sale
def update_sale(
    sale_id,
    product_id,
    customer_id,
    sale_date,
    quantity,
    sales_amount,
    discount,
    profit
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE sales
        SET
            product_id = %s,
            customer_id = %s,
            sale_date = %s,
            quantity = %s,
            sales_amount = %s,
            discount = %s,
            profit = %s
        WHERE sale_id = %s
    """, (
        product_id,
        customer_id,
        sale_date,
        quantity,
        sales_amount,
        discount,
        profit,
        sale_id
    ))

    conn.commit()

    cursor.close()
    conn.close()

def delete_sale(sale_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM sales WHERE sale_id = %s",
        (sale_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

def search_sales(search):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            s.sale_id,
            s.sale_date,
            s.quantity,
            s.sales_amount,
            s.discount,
            s.profit,
            p.product_name,
            c.name AS customer_name
        FROM sales s
        LEFT JOIN products p
            ON s.product_id = p.product_id
        LEFT JOIN customers c
            ON s.customer_id = c.id
        WHERE
            p.product_name LIKE %s
            OR c.name LIKE %s
        ORDER BY s.sale_id DESC
    """

    keyword = "%" + search + "%"

    cursor.execute(query, (keyword, keyword))

    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales

def get_sales_summary():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            COALESCE(SUM(sales_amount), 0) AS total_sales,
            COALESCE(SUM(profit), 0) AS total_profit,
            COALESCE(SUM(quantity), 0) AS total_quantity,
            COUNT(*) AS total_orders
        FROM sales
    """

    cursor.execute(query)

    summary = cursor.fetchone()

    cursor.close()
    conn.close()

    return summary

def get_monthly_sales():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            DATE_FORMAT(sale_date, '%Y-%m') AS month,
            SUM(sales_amount) AS total_sales
        FROM sales
        GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
        ORDER BY month
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def get_delivery_paginated(limit, offset):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            order_id,
            delivery_partner_id,
            promised_time,
            actual_time,
            delivery_time_minutes,
            distance_km,
            delivery_status,
            reasons_if_delayed
        FROM delivery_performance
        ORDER BY order_id
        LIMIT %s OFFSET %s
    """

    cursor.execute(query, (limit, offset))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

def get_total_deliveries():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM delivery_performance
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total
def get_avg_delivery_time():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COALESCE(AVG(delivery_time_minutes), 0)
        FROM delivery_performance
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return round(float(result), 2)
def get_avg_delivery_distance():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COALESCE(AVG(distance_km), 0)
        FROM delivery_performance
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return round(float(result), 2)
def get_total_delivery_partners():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT delivery_partner_id)
        FROM delivery_performance
        WHERE delivery_partner_id IS NOT NULL
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result

def search_deliveries(keyword):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            order_id,
            delivery_partner_id,
            promised_time,
            actual_time,
            delivery_time_minutes,
            distance_km,
            delivery_status,
            reasons_if_delayed
        FROM delivery_performance
        WHERE CAST(order_id AS CHAR) LIKE %s
           OR CAST(delivery_partner_id AS CHAR) LIKE %s
           OR delivery_status LIKE %s
           OR reasons_if_delayed LIKE %s
        ORDER BY order_id
    """

    search = f"%{keyword}%"

    cursor.execute(
        query,
        (search, search, search, search)
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

def get_delivery_status_summary():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            delivery_status,
            COUNT(*) AS total
        FROM delivery_performance
        GROUP BY delivery_status
        ORDER BY total DESC
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def get_report_total_sales():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(sales_amount), 0)
        FROM sales
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result
def get_report_total_profit():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(profit), 0)
        FROM sales
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result
def get_report_total_orders():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM sales
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result
def get_report_total_customers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM customers
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result
def get_report_monthly_sales():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            DATE_FORMAT(sale_date, '%Y-%m') AS month,
            SUM(sales_amount) AS total_sales
        FROM sales
        GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
        ORDER BY month
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def get_report_monthly_profit():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            DATE_FORMAT(sale_date, '%Y-%m') AS month,
            SUM(profit) AS total_profit
        FROM sales
        GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
        ORDER BY month
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def get_sales_by_category():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            p.category,
            SUM(s.sales_amount) AS total_sales
        FROM sales s
        JOIN products p
            ON s.product_id = p.product_id
        GROUP BY p.category
        ORDER BY total_sales DESC
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def get_top_products_by_sales():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            p.product_name,
            SUM(s.sales_amount) AS total_sales
        FROM sales s
        JOIN products p
            ON s.product_id = p.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_sales DESC
        LIMIT 5
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def get_delivery_report_summary():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            COUNT(*) AS total_deliveries,
            ROUND(AVG(delivery_time_minutes), 2) AS avg_delivery_time,
            ROUND(AVG(distance_km), 2) AS avg_distance,
            SUM(
                CASE
                    WHEN delivery_status = 'Delayed' THEN 1
                    ELSE 0
                END
            ) AS delayed_deliveries
        FROM delivery_performance
    """

    cursor.execute(query)

    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data