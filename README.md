# SQL Beginner Challenge #7: Filter Groups with HAVING

**Difficulty:** Beginner  
**Estimated time:** 10–15 minutes  
**Concepts:** `GROUP BY`, `HAVING`, filtering aggregated results  

This challenge introduces the `HAVING` clause and explains how it differs from `WHERE` when working with grouped data.

---

## 🧠 The Problem

After grouping products by category, a product manager asks:

> “Show me only the categories that have **at least 2 products**.”

You already know how to count products per category using `GROUP BY`.  
Now you need to **filter the grouped results** based on the aggregated count.

---

## 📊 Table Schema

### `products`

| Column Name | Type      | Description |
|------------|-----------|-------------|
| product_id | INTEGER   | Unique product ID |
| name       | TEXT      | Product name |
| category   | TEXT      | Product category |
| price      | DECIMAL   | Product price |
| stock_qty | INTEGER   | Units in stock |
| created_at | TIMESTAMP | Creation timestamp |

---

## 🧪 Sample Data

| product_id | name                 | category     | price  |
|-----------:|----------------------|--------------|-------:|
| 101 | Wireless Mouse      | Accessories | 24.99 |
| 102 | Mechanical Keyboard | Accessories | 89.00 |
| 103 | 27-inch Monitor     | Displays    | 229.99 |
| 104 | USB-C Hub           | Accessories | 34.50 |
| 105 | Laptop Stand        | Workspace   | 39.99 |

---

## ✅ Requirements

Your query must:

- Group products by `category`
- Count how many products are in each category
- Filter groups using `HAVING`
- Return only categories with **2 or more products**
- Return exactly two columns:
  - `category`
  - `total_products`

---

## ✍️ Your Task

Write a SQL query that fulfills the requirements.

```sql
-- Write your query here

