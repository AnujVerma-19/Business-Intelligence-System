from flask import request, render_template, redirect, url_for, session
from models import (
    login_user,
    get_dashboard_counts,
    get_all_products,
    add_product,
    get_product_by_id,
    update_product,
    delete_product,
    search_products,
    get_products_paginated,
    get_total_products,

    get_all_customers,
    add_customer,
    get_customer_by_id,
    update_customer,
    delete_customer,
    search_customers,
    get_customer_search_count,
    get_customers_paginated,
    get_total_customers,

    get_sales_paginated,
    get_total_sales,
    add_sale,
    get_products_for_sale,
    get_customers_for_sale,
    add_sale as add_sale_record,
    get_products_for_sale,
    get_customers_for_sale,
    get_sale_by_id,
    update_sale,
    delete_sale as delete_sale_record,
    search_sales,
    get_sales_summary,
    get_monthly_sales,

    get_delivery_paginated,
    get_total_deliveries,
    get_avg_delivery_time,
    get_avg_delivery_distance,
    get_total_delivery_partners,
    search_deliveries,
    get_delivery_status_summary,

    get_report_total_sales,
    get_report_total_profit,
    get_report_total_orders,
    get_report_total_customers,
    get_report_monthly_sales,
    get_report_monthly_profit,
    get_sales_by_category,
    get_top_products_by_sales,
    get_delivery_report_summary
)
def register_routes(app):

    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            user = login_user(username, password)

            if user:
                session["user"] = username
                return redirect(url_for("dashboard"))
            else:
                return render_template(
                    "login.html",
                    error="Invalid Username or Password"
                )

        return render_template("login.html")


    @app.route("/dashboard")
    def dashboard():

        if "user" not in session:
            return redirect(url_for("login"))

        counts = get_dashboard_counts()

        return render_template(
            "dashboard.html",
            products=counts["products"],
            customers=counts["customers"],
            sales=counts["sales"],
            deliveries=counts["deliveries"]
        )
    @app.route("/products")
    def products():

        if "user" not in session:
            return redirect(url_for("login"))

        page = request.args.get("page", 1, type=int)
        per_page = 10

        offset = (page - 1) * per_page

        keyword = request.args.get("search")

        if keyword:
            products = search_products(keyword)
            total = len(products)
        else:
            products = get_products_paginated(offset, per_page)
            total = get_total_products()

        total_pages = (total + per_page - 1) // per_page

        return render_template(
            "products.html",
            products=products,
            page=page,
            total_pages=total_pages,
        )
    @app.route("/customers")
    @app.route("/customers")
    def customers():

        if "user" not in session:
            return redirect(url_for("login"))

        page = request.args.get("page", 1, type=int)
        per_page = 10

        offset = (page - 1) * per_page

        keyword = request.args.get("search", "").strip()

        if keyword:

            customers = search_customers(
                keyword,
                per_page,
                offset
            )

            total = get_customer_search_count(keyword)

        else:

            customers = get_customers_paginated(
                per_page,
                offset
            )

            total = get_total_customers()

        total_pages = (total + per_page - 1) // per_page

        return render_template(
            "customers.html",
            customers=customers,
            page=page,
            total_pages=total_pages,
            search=keyword
        )
    @app.route("/add-customer", methods=["GET","POST"])
    def add_customer_page():

        if "user" not in session:
            return redirect(url_for("login"))

        if request.method=="POST":

            add_customer(
                request.form["name"],
                request.form["email"],
                request.form["address"],
                request.form["phone_no"],
                request.form["area"],
                request.form["pincode"],
                request.form["registration_no"],
                request.form["customer_segment"],
                request.form["total_order"],
                request.form["avg_order"]
            )

            return redirect(url_for("customers"))

        return render_template("add_customer.html")
    @app.route("/edit-customer/<int:customer_id>", methods=["GET", "POST"])
    def edit_customer(customer_id):

        if "user" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            update_customer(
                customer_id,
                request.form["name"],
                request.form["email"],
                request.form["address"],
                request.form["phone_no"],
                request.form["area"],
                request.form["pincode"],
                request.form["registration_no"],
                request.form["customer_segment"],
                int(request.form.get("total_order") or 0),
                float(request.form.get("avg_order") or 0)
            ) 

            return redirect(url_for("customers"))

        customer = get_customer_by_id(customer_id)

        return render_template(
            "edit_customer.html",
            customer=customer
        )
    @app.route("/delete-customer/<int:customer_id>")
    def delete_customer_page(customer_id):

        if "user" not in session:
            return redirect(url_for("login"))

        delete_customer(customer_id)

        return redirect(url_for("customers"))
    @app.route("/add-product", methods=["GET", "POST"])
    def add_product_page():

        if "user" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            product_name = request.form["product_name"]
            category = request.form["category"]
            brand = request.form["brand"]
            price = request.form["price"]
            mrp = request.form["mrp"]

            add_product(
                product_name,
                category,
                brand,
                price,
                mrp
            )

            return redirect(url_for("products"))

        return render_template("add_product.html")
    @app.route("/edit-product/<int:product_id>", methods=["GET", "POST"])
    def edit_product(product_id):

        if "user" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            update_product(
                product_id,
                request.form["product_name"],
                request.form["category"],
                request.form["brand"],
                request.form["price"],
                request.form["mrp"]
            )

            return redirect(url_for("products"))

        product = get_product_by_id(product_id)

        return render_template(
            "edit_product.html",
            product=product
        )
    @app.route("/delete-product/<int:product_id>")
    def delete_product_route(product_id):

        if "user" not in session:
            return redirect(url_for("login"))

        delete_product(product_id)

        return redirect(url_for("products"))

    @app.route("/sales")
    def sales():

        if "user" not in session:
            return redirect(url_for("login"))

        page = request.args.get("page", 1, type=int)
        per_page = 10

        keyword = request.args.get("search", "").strip()

        if keyword:
            sales_data = search_sales(keyword)
            total = len(sales_data)

            total_pages = 1
            page = 1

        else:
            offset = (page - 1) * per_page

            sales_data = get_sales_paginated(
                per_page,
                offset
            )

            total = get_total_sales()

            total_pages = (total + per_page - 1) // per_page

        summary = get_sales_summary()
        monthly_sales = get_monthly_sales()
        print("MONTHLY SALES DATA:", monthly_sales)
        return render_template(
            "sales.html",
            sales=sales_data,
            page=page,
            total_pages=total_pages,
            summary=summary,
            monthly_sales=monthly_sales
        )
    @app.route("/sales/add", methods=["GET", "POST"])
    def add_sale_page():

        if "user" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            add_sale_record(
                request.form["product_id"],
                request.form["customer_id"],
                request.form["sale_date"],
                request.form["quantity"],
                request.form["sales_amount"],
                request.form["discount"],
                request.form["profit"]
            )

            return redirect(url_for("sales"))

        products = get_products_for_sale()
        customers = get_customers_for_sale()

        return render_template(
            "add_sale.html",
            products=products,
            customers=customers
        )
    @app.route("/sales/edit/<int:sale_id>", methods=["GET", "POST"])
    def edit_sale(sale_id):

        if "user" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            update_sale(
                sale_id,
                request.form["product_id"],
                request.form["customer_id"],
                request.form["sale_date"],
                request.form["quantity"],
                request.form["sales_amount"],
                request.form["discount"],
                request.form["profit"]
            )

            return redirect(url_for("sales"))

        sale = get_sale_by_id(sale_id)

        products = get_products_for_sale()
        customers = get_customers_for_sale()

        return render_template(
            "edit_sale.html",
            sale=sale,
            products=products,
            customers=customers
        )
    @app.route("/sales/delete/<int:sale_id>")
    def delete_sale_page(sale_id):

        if "user" not in session:
            return redirect(url_for("login"))

        delete_sale_record(sale_id)

        return redirect(url_for("sales"))
    @app.route("/delivery")
    def delivery():

        if "user" not in session:
            return redirect(url_for("login"))

        page = request.args.get("page", 1, type=int)

        per_page = 10

        keyword = request.args.get("search", '').strip()

        if keyword:

            delivery_data = search_deliveries(keyword)

            total = len(delivery_data)

            total_pages = 1
            page = 1

        else:


            offset = (page - 1) * per_page

            delivery_data = get_delivery_paginated(
                per_page,
                offset
            )

            total = get_total_deliveries()

            total_pages = (total + per_page - 1) // per_page

        avg_delivery_time = get_avg_delivery_time()
        avg_distance = get_avg_delivery_distance()
        total_partners = get_total_delivery_partners()
        delivery_status = get_delivery_status_summary()

        return render_template(
            "delivery.html",
            deliveries=delivery_data,
            page=page,
            total_pages=total_pages,
            total_deliveries=total,
            avg_delivery_time=avg_delivery_time,
            avg_distance=avg_distance,
            total_partners=total_partners,
            delivery_status=delivery_status,
            search=keyword
        )
    @app.route("/reports")
    def reports():

        if "user" not in session:
            return redirect(url_for("login"))

        total_sales = get_report_total_sales()
        total_profit = get_report_total_profit()
        total_orders = get_report_total_orders()
        total_customers = get_report_total_customers()

        monthly_sales = get_report_monthly_sales()
        monthly_profit = get_report_monthly_profit()
        sales_by_category = get_sales_by_category()
        top_products = get_top_products_by_sales()
        delivery_summary = get_delivery_report_summary()

        return render_template(
            "reports.html",
            total_sales=total_sales,
            total_profit=total_profit,
            total_orders=total_orders,
            total_customers=total_customers,
            monthly_sales=monthly_sales,
            monthly_profit=monthly_profit,
            sales_by_category=sales_by_category,
            top_products=top_products,
            delivery_summary=delivery_summary
        )