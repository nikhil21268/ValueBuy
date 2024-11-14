
# ValueBuy | E – Commerce Store | DBMS Project

Built an E-Commerce Store using MySQL at the back-end & Python, Flask, HTML, CSS, JavaScript at the front-end.


## Deployment
* Run **MySQL_Data/MySQL_ToRun.sql** in MySQL Workbench.
* To deploy the project run **demo.py** and **app.py** in the ValueBuy sub-directory.
* If the code doesn't run for some reason, double-check the path mentioned in the **demo.py** and **app.py** files, and update if required.

## 1. Scope of the Project / Abstract

Welcome to ValueBuy's Online Retail Store! In the ever-evolving landscape of the Indian economy, online shopping has become the norm. ValueBuy aims to revolutionize the online retail experience by providing a comprehensive platform that not only enhances the efficiency of the database system but also addresses various aspects of inventory management, warehouse logistics, and supply chain management. This project focuses on creating an end-to-end database application tailored to the specific needs of ValueBuy's online business.

## 2. Technical Requirements

### Tools Used
- **MySQL:** Database management for storing application data.
- **HTML:** Front-end development for creating a user-friendly interface.
- **CSS:** Styling elements to ensure a distinct and visually appealing design.
- **Python:** Back-end connectivity to the database and seamless data access.

## 3. Functional Requirements with Access Constraints

### Key Functions
- **Goods Handling:** Receive and stock goods from wholesale vendors in a structured manner.
- **Customer Accounts:** Users create accounts, browse products, filter by category, and make purchases.
- **Membership Benefits:** Regular, Platinum, and Imperia members enjoy specific discounts on purchases.
- **Warehouse Management:** Inventory updates, purchase orders, and employee management.
- **Employee Roles:** Different roles like Product Handler, Customer Care, and Courier with specific responsibilities.
- **Salary Management:** Increment or decrement employee salaries based on performance.

### Access Constraints
- **User Access:** Limited to shopping-related activities; no access to database or platform management.
- **Owner/Franchise Access:** Database access limited to product listing and invoicing to vendors.
- **Customer Support Access:** Access to user database for providing assistance.
- **Manager Access:** Salary adjustments for employees, except self; no access to personal salary.

## 4. Entities Involved (Primary Keys)

1. **Supplier/Vendor:** Supplier ID / Vendor ID
2. **Employee:** Employee ID (Manager, Courier, etc.)
3. **Product:** Product ID (Electronics, Edibles, Clothing, Cosmetics)
4. **Warehouse:** Warehouse ID
5. **Customer:** Customer ID
6. **Cart:** Cart ID
7. **Review (Weak Entity):** Order ID

## 5. Access Constraints

- **User Access:** Limited to shopping experience only.
- **Owner/Franchise Access:** Database access for product listing and vendor invoicing.
- **Customer Support Access:** User database access for assistance; constrained to owner/franchise database.
- **Manager Access:** Salary adjustments for employees (except self); constrained salary adjustment.

## 6. Additional Constraints

- **Unique Constraint:** Categories under which products are added should be unique.
- **Unique Keys/IDs:** Every employee should have a unique key/ID.
- **Unique Tracking Number:** Every order placed by the user should have a unique tracking number.
- **Not Null Constraint:** Products listed on the platform or available in the warehouses cannot be null.
- **Default Constraint:** Users without a membership will be given a default Regular membership.

Thank you for exploring the ValueBuy Online Retail Store project! Feel free to contribute and make the online shopping experience even better.

## Screenshots
![login_signup](https://github.com/nikhil21268/ValueBuy/blob/main/Screenshots/loginSignup.PNG)
![signup](https://github.com/nikhil21268/ValueBuy/blob/main/Screenshots/signUp.PNG)
![queries_assmt](https://github.com/nikhil21268/ValueBuy/blob/main/Screenshots/queries.PNG)
![prods](https://github.com/nikhil21268/ValueBuy/blob/main/Screenshots/products1.PNG)
![prods_add_to_cart](https://github.com/nikhil21268/ValueBuy/blob/main/Screenshots/products2.PNG)
![cart](https://github.com/nikhil21268/ValueBuy/blob/main/Screenshots/cart.PNG)
![upgrade_membership](https://github.com/nikhil21268/ValueBuy/blob/main/Screenshots/upgradeMembership.PNG)
![admin](https://github.com/nikhil21268/ValueBuy/blob/main/Screenshots/admin.PNG)

