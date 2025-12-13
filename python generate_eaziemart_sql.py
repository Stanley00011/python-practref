import random
from datetime import datetime, timedelta

# --------------------------------------------
# Configuration
# --------------------------------------------
NUM_CUSTOMERS = 150
NUM_SALES = 1000
customer_base_names = [
    "Jide", "Chuks", "Kunle", "Ani", "Sarah", "Michael", "Jennifer", "David",
    "Grace", "Samuel", "Fatima", "Olu", "Kemi", "Tunde", "Aisha", "Ngozi"
]

products = [
    (1, "Milk", "Dairy", 1200),
    (2, "Bread", "Bakery", 800),
    (3, "Eggs", "Poultry", 1500),
    (4, "Butter", "Dairy", 1800),
    (5, "Chicken Wings", "Frozen", 3500),
    (6, "Rice 5kg", "Grains", 4200)
]

delivery_partners = [
    (1, "Speedy Riders", "Bike"),
    (2, "FastDrop", "Car"),
    (3, "SwiftExpress", "Bike")
]

# --------------------------------------------
# Helper Functions
# --------------------------------------------

def random_date(start, end):
    """Generate a random date between start and end"""
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def create_date_dimension(start_date, end_date):
    """Generate date dimension rows between two dates"""
    dates = []
    curr = start_date
    date_id = 1
    while curr <= end_date:
        dates.append((date_id, curr, curr.year, curr.month, curr.day))
        curr += timedelta(days=1)
        date_id += 1
    return dates

# --------------------------------------------
# Generate Data
# --------------------------------------------

# 1. Generate Customers
customers = []
for cid in range(1, NUM_CUSTOMERS + 1):
    name = random.choice(customer_base_names)
    surname = random.choice(["James", "Ade", "Obi", "Ola", "Danladi", "Okoro", "Mustapha"])
    full_name = f"{name} {surname}"

    email = f"{name.lower()}{cid}@gmail.com" if random.random() > 0.15 else "NULL"

    city = random.choice(["Lagos", "Abuja", "Ibadan", "Port Harcourt"])
    join_date = random_date(datetime(2023, 1, 1), datetime(2023, 9, 1)).strftime("%Y-%m-%d")

    customers.append((cid, full_name, email, city, join_date))

# 2. Generate Dates Dimension
dates_dim = create_date_dimension(datetime(2023,1,1), datetime(2023,12,31))

# 3. Generate Fact Sales (1000 rows)
sales = []
for sid in range(1, NUM_SALES + 1):
    customer_id = random.randint(1, NUM_CUSTOMERS)
    product = random.choice(products)
    product_id = product[0]

    date_obj = random.choice(dates_dim)
    date_id = date_obj[0]

    quantity = random.randint(1, 5)
    delivery_partner_id = random.choice(delivery_partners)[0]

    delivery_time = random.randint(20, 60) if random.random() > 0.1 else "NULL"
    status = "Delivered" if delivery_time != "NULL" else "Late"

    sales.append((sid, customer_id, product_id, date_id, quantity, delivery_partner_id, delivery_time, status))

# --------------------------------------------
# Write to SQL file
# --------------------------------------------

with open("eaziemart_full.sql", "w") as f:

    # Database & Tables
    f.write("""
CREATE DATABASE IF NOT EXISTS eaziemart;
USE eaziemart;

DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_customers;
DROP TABLE IF EXISTS dim_products;
DROP TABLE IF EXISTS dim_dates;
DROP TABLE IF EXISTS dim_delivery;

CREATE TABLE dim_customers (
    customer_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    join_date DATE
);

CREATE TABLE dim_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE dim_dates (
    date_id INT PRIMARY KEY,
    full_date DATE,
    year INT,
    month INT,
    day INT
);

CREATE TABLE dim_delivery (
    delivery_partner_id INT PRIMARY KEY,
    partner_name VARCHAR(100),
    vehicle_type VARCHAR(50)
);

CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    date_id INT,
    quantity INT,
    delivery_partner_id INT,
    delivery_time_minutes INT,
    order_status VARCHAR(20),
    FOREIGN KEY(customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES dim_products(product_id),
    FOREIGN KEY(date_id) REFERENCES dim_dates(date_id),
    FOREIGN KEY(delivery_partner_id) REFERENCES dim_delivery(delivery_partner_id)
);
""")

    # Insert Customers
    for c in customers:
        cid, fullname, email, city, join_date = c
        email_str = f"'{email}'" if email != "NULL" else "NULL"
        f.write(f"INSERT INTO dim_customers VALUES ({cid}, '{fullname}', {email_str}, '{city}', '{join_date}');\n")

    # Insert Products
    for p in products:
        f.write(f"INSERT INTO dim_products VALUES ({p[0]}, '{p[1]}', '{p[2]}', {p[3]});\n")

    # Insert Delivery Partners
    for d in delivery_partners:
        f.write(f"INSERT INTO dim_delivery VALUES ({d[0]}, '{d[1]}', '{d[2]}');\n")

    # Insert Dates
    for d in dates_dim:
        f.write(f"INSERT INTO dim_dates VALUES ({d[0]}, '{d[1]}', {d[2]}, {d[3]}, {d[4]});\n")

    # Insert Sales
    for s in sales:
        sid, cid, pid, did, qty, dp, dtime, stat = s
        dtime_val = dtime if dtime != "NULL" else "NULL"
        f.write(
            f"INSERT INTO fact_sales VALUES ({sid}, {cid}, {pid}, {did}, {qty}, {dp}, {dtime_val}, '{stat}');\n"
        )

print("SQL file eaziemart_full.sql generated successfully!")
