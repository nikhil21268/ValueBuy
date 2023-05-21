
from flask import Flask, render_template, url_for, redirect, request

import demo as dm

from flask import flash


app = Flask(__name__,template_folder="C:/Users/suris/Desktop/DBMS/Project/A6/ValueBuy")

app.secret_key = "your-secret-key-here"










@app.route('/upgrade_membership_page',methods=['GET', 'POST'])
def upgrade_membership_page():
    if request.method=="POST":
        membership_type = request.form['membership']
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('upgrade_membership'))#,membership_type=membership_type,username=username,password=password)
    return render_template("/templates/upgrade_membership.html")

@app.route('/upgrade_membership', methods=['GET', 'POST'])
def upgrade_membership():
    if request.method == 'POST':
        membership_type = request.form['membership']
        username = request.form['username']
        password = request.form['password']
        # code to process membership upgrade
        print(membership_type)
        dm.upgrade_membership(username,password,membership_type)
        print("came here")
        # Redirect to cart.html with the membership type as a URL parameter
        #return redirect(f'/cart.html?membership_type={membership_type}')
        #return redirect(f'/cart.html?membership_type={membership_type}')
        return redirect(url_for('cart'))
    return render_template("/templates/upgrade_membership.html")


# @app.route("/" , methods= ["POST", "GET"])
# def login():
#     if request.method =="POST":
#         user = request.form["username"]
#         passwd = request.form["password"]

#         if dm.check_login(user, passwd):
#             return redirect(url_for("welcome", name = user))
#     else:
#         return render_template("/templates/loginpage.html")
    
@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        passwd = request.form["password"]

        if dm.check_login(user, passwd):
            return redirect(url_for("welcome", name=user))
        else:
            #flash("Invalid login credentials.")
            pass
    return render_template("/templates/loginpage.html")

@app.route('/check_admin')
def check_admin():
    return render_template('/templates/admin_login.html')

@app.route('/logout_admin')
def logout_admin():
    # Clear the session and redirect to login page
    return redirect(url_for('login'))

@app.route('/admin')
def admin():
    products=dm.get_prod_class()
    return render_template('/templates/admin.html',products=products)


@app.route('/admin/delete-product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    # Delete the product with the specified ID from the database
    dm.delete_product(product_id)
    #flash('Product deleted successfully', 'success')

    return redirect(url_for('admin'))

@app.route('/admin/add-product', methods=['POST'])
def add_product():
    # p_id = request.form['p_id']
    prod_name = request.form['prod_name']
    price = request.form['price']
    date_of_mfg = request.form['date_of_mfg']
    qty = request.form['qty']
    net_weight = request.form['net_weight']
    manufacturing_company = request.form['manufacturing_company']
    prod_type = request.form['prod_type']
    # Save the image to the file system
    dm.add_product(prod_name,price,date_of_mfg,qty,net_weight,manufacturing_company,prod_type)
    #flash('Product added successfully', 'success')
    return redirect(url_for('admin'))

# @app.route('/admin/customers')
# def admin_customers():
#     customers = dm.get_customers()
#     return render_template('admin_customers.html', customers=customers)

# @app.route('/admin-login', methods=['GET', 'POST'])
# def admin_login():
#     if request.method == 'POST':
#         # Get form data
#         username = request.form['username']
#         password = request.form['password']
#         print(username)
#         # Check if username and password are correct
#         if dm.check_login_admin(username, password):
#             print("hey")
#             return redirect(url_for("admin"))
#         else:
#             # flash("Invalid login credentials.")
#             pass
#     return render_template("/templates/loginpage.html")

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Code to check if the provided username and password are valid admin credentials
        # ...
        # If they are, redirect to the admin dashboard
        if dm.check_login_admin(username, password):
            print("hey")
            return redirect(url_for("admin"))
        else:
            # flash("Invalid login credentials.")
            pass
    return render_template("/templates/loginpage.html")
    


@app.route('/admin/customers')
def admin_customers():
    customers = dm.get_customers()
    return render_template('/templates/admin_customers.html', customers=customers)

@app.route('/admin/delete-customer/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    # Delete the customer with the specified ID from the database
    dm.delete_customer(customer_id)
    #flash('Customer deleted successfully', 'success')

    return redirect(url_for('admin_customers'))

@app.route('/admin/add-customer', methods=['POST'])
def add_customer():
    # c_id = request.form['c_id']
    cust_first_name = request.form['cust_first_name']
    cust_last_name = request.form['cust_last_name']
    cust_dob = request.form['cust_dob']
    cust_street = request.form['cust_street']
    cust_city = request.form['cust_city']
    cust_state = request.form['cust_state']
    cust_pin = request.form['cust_pin']
    cust_title = request.form['cust_title']
    # Save the image to the file system
    dm.add_customer(cust_first_name,cust_last_name,cust_dob,cust_street,cust_city,cust_state,cust_pin,cust_title)
    #flash('Customer added successfully', 'success')
    return redirect(url_for('admin_customers'))

@app.route('/admin/employees')
def admin_employees():
    employees = dm.get_employees()
    return render_template('/templates/admin_employees.html', employees=employees)

@app.route('/admin/delete-employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    # Delete the employee with the specified ID from the database
    dm.delete_employee(employee_id)
    #flash('Employee deleted successfully', 'success')

    return redirect(url_for('admin_employees'))

@app.route('/update_employee_increment/<int:employee_id>', methods=['POST'])
def update_employee_increment(employee_id):
    # Get the employee record from the database
    #inc = request.form['inc']
    increment = request.form['increment']
    dm.update_employee_increment(employee_id,increment)

    # Increment the employee's salary by 10%
    # employee.salary *= 1.1

    # # Save the updated record back to the database
    # db.session.commit()

    # Redirect the user back to the employee list page
    return redirect(url_for('admin_employees'))


@app.route('/admin/add-employee', methods=['POST'])
def add_employee():
    # e_id = request.form['e_id']
    emp_name = request.form['emp_name']
    #emp_last_name = request.form['emp_last_name']
    emp_dob = request.form['emp_dob']
    emp_street = request.form['emp_street']
    emp_city = request.form['emp_city']
    emp_state = request.form['emp_state']
    emp_pin = request.form['emp_pin']
    emp_role = request.form['emp_role']
    emp_type = request.form['emp_type']
    base_salary=request.form['base_salary']
    # Save the image to the file system
    dm.add_employee(emp_name,emp_dob,emp_street,emp_city,emp_state,emp_pin,emp_role,emp_type,base_salary)
    #flash('Employee added successfully', 'success')
    return redirect(url_for('admin_employees'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        cust_first_name = request.form['cust_first_name']
        cust_last_name = request.form['cust_last_name']
        cust_dob = request.form['cust_dob']
        cust_street = request.form['cust_street']
        cust_city = request.form['cust_city']
        cust_state = request.form['cust_state']
        cust_pin = request.form['cust_pin']
        cust_title = request.form['cust_title']


        # Insert user into MySQL database
        dm.signup(username,password,cust_first_name,cust_last_name,cust_dob,cust_street,cust_city,cust_state,cust_pin,cust_title)

        # Redirect to login page
        #return redirect(url_for('login'))
        #return redirect(url_for('/'))
        return redirect(url_for('login'))

    # Render signup page
    return render_template('/templates/signup.html')


@app.route("/<name>")
def welcome(name):
    return render_template("/templates/welcome.html", name = name)


@app.route("/homepage")
def homepage():
    return render_template("/templates/child.html")

@app.route("/show_tables")
def citizen():
    ci = dm.get_tables()
    return render_template("/templates/index.html", content = "N", list = ci)

@app.route("/index2_new")
def index2_new():

    dm.empty_cart()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    dm.upgrade_membership_check()
    

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=0)

@app.route("/index2")
def index2():

    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()
    

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)


@app.route("/index3")
def index3():
    
    return render_template("/for_index3/dist/index.html")



@app.route("/index21")
def added_to_cart_p1():
    
    ci = dm.add_to_cart_p1()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index22")
def added_to_cart_p2():
    
    ci = dm.add_to_cart_p2()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index23")
def added_to_cart_p3():
    
    ci = dm.add_to_cart_p3()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index24")
def added_to_cart_p4():
    
    ci = dm.add_to_cart_p4()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index25")
def added_to_cart_p5():
    
    ci = dm.add_to_cart_p5()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index26")
def added_to_cart_p6():
    
    ci = dm.add_to_cart_p6()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

    return None

@app.route("/index27")
def added_to_cart_p7():
    
    ci = dm.add_to_cart_p7()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index28")
def added_to_cart_p8():
    
    ci = dm.add_to_cart_p8()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


# adding now

@app.route("/index29")
def add_to_cart_p9():
    
    ci = dm.add_to_cart_p9()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index210")
def add_to_cart_p10():
    
    ci = dm.add_to_cart_p10()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index211")
def add_to_cart_p11():
    
    ci = dm.add_to_cart_p11()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index212")
def add_to_cart_p12():
    
    ci = dm.add_to_cart_p12()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index213")
def add_to_cart_p13():
    
    ci = dm.add_to_cart_p13()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index214")
def add_to_cart_p14():
    
    ci = dm.add_to_cart_p14()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index215")
def add_to_cart_p15():
    
    ci = dm.add_to_cart_p15()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index216")
def add_to_cart_p16():
    
    ci = dm.add_to_cart_p16()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index217")
def add_to_cart_p17():
    
    ci = dm.add_to_cart_p17()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index218")
def add_to_cart_p18():
    
    ci = dm.add_to_cart_p18()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index219")
def add_to_cart_p19():
    
    ci = dm.add_to_cart_p19()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index220")
def add_to_cart_p20():
    
    ci = dm.add_to_cart_p20()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index221")
def add_to_cart_21():
    
    ci = dm.add_to_cart_p21()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index222")
def add_to_cart_p22():
    
    ci = dm.add_to_cart_p22()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index223")
def add_to_cart_p23():
    
    ci = dm.add_to_cart_p23()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index224")
def add_to_cart_p24():
    
    ci = dm.add_to_cart_p24()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index225")
def add_to_cart_p25():
    
    ci = dm.add_to_cart_p25()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index226")
def add_to_cart_p26():
    
    ci = dm.add_to_cart_p26()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index227")
def add_to_cart_p27():
    
    ci = dm.add_to_cart_p27()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index228")
def add_to_cart_p28():
    
    ci = dm.add_to_cart_p28()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index229")
def add_to_cart_p29():
    
    ci = dm.add_to_cart_p29()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index230")
def add_to_cart_p30():
    
    ci = dm.add_to_cart_p30()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index231")
def add_to_cart_p31():
    
    ci = dm.add_to_cart_p31()
    list_pid=dm.index2_1()
    
    
    list_prod_name=dm.index2_2()

    list_price=dm.index2_3()

    num=dm.index2_4()


    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)

#expeeriment
# import string

# # Define the base function
# import string

# # Define the base function
# def generate_add_to_cart_function(product_number):
#     def add_to_cart():
#         ci = getattr(dm, f"add_to_cart_p{product_number}")()
#         list_pid = dm.index2_1()
#         list_prod_name = dm.index2_2()
#         list_price = dm.index2_3()
#         num = dm.index2_4()
#         return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)
#     return add_to_cart

# # Generate the functions
# for i in range(232, 2593):
#     function_name = "add_to_cart_p" + str(i)
#     function_definition = generate_add_to_cart_function(i)
#     globals()[function_name] = function_definition


@app.route("/index232")
def add_to_cart_p32():
    ci = dm.add_to_cart_p32()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index233")
def add_to_cart_p33():
    ci = dm.add_to_cart_p33()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index234")
def add_to_cart_p34():
    ci = dm.add_to_cart_p34()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index235")
def add_to_cart_p35():
    ci = dm.add_to_cart_p35()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index236")
def add_to_cart_p36():
    ci = dm.add_to_cart_p36()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index237")
def add_to_cart_p37():
    ci = dm.add_to_cart_p37()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index238")
def add_to_cart_p38():
    ci = dm.add_to_cart_p38()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index239")
def add_to_cart_p39():
    ci = dm.add_to_cart_p39()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index240")
def add_to_cart_p40():
    ci = dm.add_to_cart_p40()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index241")
def add_to_cart_p41():
    ci = dm.add_to_cart_p41()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index242")
def add_to_cart_p42():
    ci = dm.add_to_cart_p42()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index243")
def add_to_cart_p43():
    ci = dm.add_to_cart_p43()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index244")
def add_to_cart_p44():
    ci = dm.add_to_cart_p44()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index245")
def add_to_cart_p45():
    ci = dm.add_to_cart_p45()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index246")
def add_to_cart_p46():
    ci = dm.add_to_cart_p46()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index247")
def add_to_cart_p47():
    ci = dm.add_to_cart_p47()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index248")
def add_to_cart_p48():
    ci = dm.add_to_cart_p48()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index249")
def add_to_cart_p49():
    ci = dm.add_to_cart_p49()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index250")
def add_to_cart_p50():
    ci = dm.add_to_cart_p50()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index251")
def add_to_cart_p51():
    ci = dm.add_to_cart_p51()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index252")
def add_to_cart_p52():
    ci = dm.add_to_cart_p52()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index253")
def add_to_cart_p53():
    ci = dm.add_to_cart_p53()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index254")
def add_to_cart_p54():
    ci = dm.add_to_cart_p54()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index255")
def add_to_cart_p55():
    ci = dm.add_to_cart_p55()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index256")
def add_to_cart_p56():
    ci = dm.add_to_cart_p56()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index257")
def add_to_cart_p57():
    ci = dm.add_to_cart_p57()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index258")
def add_to_cart_p58():
    ci = dm.add_to_cart_p58()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index259")
def add_to_cart_p59():
    ci = dm.add_to_cart_p59()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index260")
def add_to_cart_p60():
    ci = dm.add_to_cart_p60()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index261")
def add_to_cart_p61():
    ci = dm.add_to_cart_p61()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index262")
def add_to_cart_p62():
    ci = dm.add_to_cart_p62()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index263")
def add_to_cart_p63():
    ci = dm.add_to_cart_p63()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index264")
def add_to_cart_p64():
    ci = dm.add_to_cart_p64()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index265")
def add_to_cart_p65():
    ci = dm.add_to_cart_p65()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index266")
def add_to_cart_p66():
    ci = dm.add_to_cart_p66()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index267")
def add_to_cart_p67():
    ci = dm.add_to_cart_p67()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index268")
def add_to_cart_p68():
    ci = dm.add_to_cart_p68()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index269")
def add_to_cart_p69():
    ci = dm.add_to_cart_p69()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index270")
def add_to_cart_p70():
    ci = dm.add_to_cart_p70()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index271")
def add_to_cart_p71():
    ci = dm.add_to_cart_p71()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index272")
def add_to_cart_p72():
    ci = dm.add_to_cart_p72()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index273")
def add_to_cart_p73():
    ci = dm.add_to_cart_p73()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index274")
def add_to_cart_p74():
    ci = dm.add_to_cart_p74()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index275")
def add_to_cart_p75():
    ci = dm.add_to_cart_p75()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index276")
def add_to_cart_p76():
    ci = dm.add_to_cart_p76()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index277")
def add_to_cart_p77():
    ci = dm.add_to_cart_p77()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index278")
def add_to_cart_p78():
    ci = dm.add_to_cart_p78()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index279")
def add_to_cart_p79():
    ci = dm.add_to_cart_p79()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index280")
def add_to_cart_p80():
    ci = dm.add_to_cart_p80()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index281")
def add_to_cart_p81():
    ci = dm.add_to_cart_p81()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index282")
def add_to_cart_p82():
    ci = dm.add_to_cart_p82()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index283")
def add_to_cart_p83():
    ci = dm.add_to_cart_p83()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index284")
def add_to_cart_p84():
    ci = dm.add_to_cart_p84()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index285")
def add_to_cart_p85():
    ci = dm.add_to_cart_p85()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index286")
def add_to_cart_p86():
    ci = dm.add_to_cart_p86()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index287")
def add_to_cart_p87():
    ci = dm.add_to_cart_p87()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index288")
def add_to_cart_p88():
    ci = dm.add_to_cart_p88()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index289")
def add_to_cart_p89():
    ci = dm.add_to_cart_p89()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index290")
def add_to_cart_p90():
    ci = dm.add_to_cart_p90()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index291")
def add_to_cart_p91():
    ci = dm.add_to_cart_p91()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index292")
def add_to_cart_p92():
    ci = dm.add_to_cart_p92()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index293")
def add_to_cart_p93():
    ci = dm.add_to_cart_p93()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index294")
def add_to_cart_p94():
    ci = dm.add_to_cart_p94()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index295")
def add_to_cart_p95():
    ci = dm.add_to_cart_p95()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index296")
def add_to_cart_p96():
    ci = dm.add_to_cart_p96()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index297")
def add_to_cart_p97():
    ci = dm.add_to_cart_p97()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index298")
def add_to_cart_p98():
    ci = dm.add_to_cart_p98()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index299")
def add_to_cart_p99():
    ci = dm.add_to_cart_p99()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2100")
def add_to_cart_p100():
    ci = dm.add_to_cart_p100()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2101")
def add_to_cart_p101():
    ci = dm.add_to_cart_p101()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2102")
def add_to_cart_p102():
    ci = dm.add_to_cart_p102()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2103")
def add_to_cart_p103():
    ci = dm.add_to_cart_p103()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2104")
def add_to_cart_p104():
    ci = dm.add_to_cart_p104()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2105")
def add_to_cart_p105():
    ci = dm.add_to_cart_p105()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2106")
def add_to_cart_p106():
    ci = dm.add_to_cart_p106()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2107")
def add_to_cart_p107():
    ci = dm.add_to_cart_p107()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2108")
def add_to_cart_p108():
    ci = dm.add_to_cart_p108()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2109")
def add_to_cart_p109():
    ci = dm.add_to_cart_p109()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2110")
def add_to_cart_p110():
    ci = dm.add_to_cart_p110()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2111")
def add_to_cart_p111():
    ci = dm.add_to_cart_p111()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2112")
def add_to_cart_p112():
    ci = dm.add_to_cart_p112()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2113")
def add_to_cart_p113():
    ci = dm.add_to_cart_p113()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2114")
def add_to_cart_p114():
    ci = dm.add_to_cart_p114()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2115")
def add_to_cart_p115():
    ci = dm.add_to_cart_p115()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2116")
def add_to_cart_p116():
    ci = dm.add_to_cart_p116()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2117")
def add_to_cart_p117():
    ci = dm.add_to_cart_p117()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2118")
def add_to_cart_p118():
    ci = dm.add_to_cart_p118()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2119")
def add_to_cart_p119():
    ci = dm.add_to_cart_p119()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2120")
def add_to_cart_p120():
    ci = dm.add_to_cart_p120()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2121")
def add_to_cart_p121():
    ci = dm.add_to_cart_p121()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2122")
def add_to_cart_p122():
    ci = dm.add_to_cart_p122()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2123")
def add_to_cart_p123():
    ci = dm.add_to_cart_p123()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2124")
def add_to_cart_p124():
    ci = dm.add_to_cart_p124()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2125")
def add_to_cart_p125():
    ci = dm.add_to_cart_p125()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2126")
def add_to_cart_p126():
    ci = dm.add_to_cart_p126()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2127")
def add_to_cart_p127():
    ci = dm.add_to_cart_p127()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2128")
def add_to_cart_p128():
    ci = dm.add_to_cart_p128()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2129")
def add_to_cart_p129():
    ci = dm.add_to_cart_p129()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2130")
def add_to_cart_p130():
    ci = dm.add_to_cart_p130()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2131")
def add_to_cart_p131():
    ci = dm.add_to_cart_p131()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2132")
def add_to_cart_p132():
    ci = dm.add_to_cart_p132()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2133")
def add_to_cart_p133():
    ci = dm.add_to_cart_p133()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2134")
def add_to_cart_p134():
    ci = dm.add_to_cart_p134()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2135")
def add_to_cart_p135():
    ci = dm.add_to_cart_p135()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2136")
def add_to_cart_p136():
    ci = dm.add_to_cart_p136()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2137")
def add_to_cart_p137():
    ci = dm.add_to_cart_p137()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2138")
def add_to_cart_p138():
    ci = dm.add_to_cart_p138()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2139")
def add_to_cart_p139():
    ci = dm.add_to_cart_p139()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2140")
def add_to_cart_p140():
    ci = dm.add_to_cart_p140()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2141")
def add_to_cart_p141():
    ci = dm.add_to_cart_p141()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2142")
def add_to_cart_p142():
    ci = dm.add_to_cart_p142()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2143")
def add_to_cart_p143():
    ci = dm.add_to_cart_p143()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2144")
def add_to_cart_p144():
    ci = dm.add_to_cart_p144()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2145")
def add_to_cart_p145():
    ci = dm.add_to_cart_p145()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2146")
def add_to_cart_p146():
    ci = dm.add_to_cart_p146()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2147")
def add_to_cart_p147():
    ci = dm.add_to_cart_p147()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2148")
def add_to_cart_p148():
    ci = dm.add_to_cart_p148()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2149")
def add_to_cart_p149():
    ci = dm.add_to_cart_p149()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2150")
def add_to_cart_p150():
    ci = dm.add_to_cart_p150()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2151")
def add_to_cart_p151():
    ci = dm.add_to_cart_p151()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2152")
def add_to_cart_p152():
    ci = dm.add_to_cart_p152()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2153")
def add_to_cart_p153():
    ci = dm.add_to_cart_p153()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2154")
def add_to_cart_p154():
    ci = dm.add_to_cart_p154()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2155")
def add_to_cart_p155():
    ci = dm.add_to_cart_p155()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2156")
def add_to_cart_p156():
    ci = dm.add_to_cart_p156()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2157")
def add_to_cart_p157():
    ci = dm.add_to_cart_p157()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2158")
def add_to_cart_p158():
    ci = dm.add_to_cart_p158()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2159")
def add_to_cart_p159():
    ci = dm.add_to_cart_p159()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2160")
def add_to_cart_p160():
    ci = dm.add_to_cart_p160()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2161")
def add_to_cart_p161():
    ci = dm.add_to_cart_p161()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2162")
def add_to_cart_p162():
    ci = dm.add_to_cart_p162()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2163")
def add_to_cart_p163():
    ci = dm.add_to_cart_p163()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2164")
def add_to_cart_p164():
    ci = dm.add_to_cart_p164()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2165")
def add_to_cart_p165():
    ci = dm.add_to_cart_p165()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2166")
def add_to_cart_p166():
    ci = dm.add_to_cart_p166()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2167")
def add_to_cart_p167():
    ci = dm.add_to_cart_p167()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2168")
def add_to_cart_p168():
    ci = dm.add_to_cart_p168()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2169")
def add_to_cart_p169():
    ci = dm.add_to_cart_p169()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2170")
def add_to_cart_p170():
    ci = dm.add_to_cart_p170()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2171")
def add_to_cart_p171():
    ci = dm.add_to_cart_p171()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2172")
def add_to_cart_p172():
    ci = dm.add_to_cart_p172()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2173")
def add_to_cart_p173():
    ci = dm.add_to_cart_p173()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2174")
def add_to_cart_p174():
    ci = dm.add_to_cart_p174()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2175")
def add_to_cart_p175():
    ci = dm.add_to_cart_p175()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2176")
def add_to_cart_p176():
    ci = dm.add_to_cart_p176()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2177")
def add_to_cart_p177():
    ci = dm.add_to_cart_p177()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2178")
def add_to_cart_p178():
    ci = dm.add_to_cart_p178()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2179")
def add_to_cart_p179():
    ci = dm.add_to_cart_p179()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2180")
def add_to_cart_p180():
    ci = dm.add_to_cart_p180()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2181")
def add_to_cart_p181():
    ci = dm.add_to_cart_p181()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2182")
def add_to_cart_p182():
    ci = dm.add_to_cart_p182()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2183")
def add_to_cart_p183():
    ci = dm.add_to_cart_p183()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2184")
def add_to_cart_p184():
    ci = dm.add_to_cart_p184()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2185")
def add_to_cart_p185():
    ci = dm.add_to_cart_p185()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2186")
def add_to_cart_p186():
    ci = dm.add_to_cart_p186()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2187")
def add_to_cart_p187():
    ci = dm.add_to_cart_p187()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2188")
def add_to_cart_p188():
    ci = dm.add_to_cart_p188()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2189")
def add_to_cart_p189():
    ci = dm.add_to_cart_p189()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2190")
def add_to_cart_p190():
    ci = dm.add_to_cart_p190()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2191")
def add_to_cart_p191():
    ci = dm.add_to_cart_p191()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2192")
def add_to_cart_p192():
    ci = dm.add_to_cart_p192()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2193")
def add_to_cart_p193():
    ci = dm.add_to_cart_p193()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2194")
def add_to_cart_p194():
    ci = dm.add_to_cart_p194()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2195")
def add_to_cart_p195():
    ci = dm.add_to_cart_p195()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2196")
def add_to_cart_p196():
    ci = dm.add_to_cart_p196()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2197")
def add_to_cart_p197():
    ci = dm.add_to_cart_p197()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2198")
def add_to_cart_p198():
    ci = dm.add_to_cart_p198()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2199")
def add_to_cart_p199():
    ci = dm.add_to_cart_p199()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2200")
def add_to_cart_p200():
    ci = dm.add_to_cart_p200()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2201")
def add_to_cart_p201():
    ci = dm.add_to_cart_p201()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2202")
def add_to_cart_p202():
    ci = dm.add_to_cart_p202()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2203")
def add_to_cart_p203():
    ci = dm.add_to_cart_p203()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2204")
def add_to_cart_p204():
    ci = dm.add_to_cart_p204()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2205")
def add_to_cart_p205():
    ci = dm.add_to_cart_p205()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2206")
def add_to_cart_p206():
    ci = dm.add_to_cart_p206()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2207")
def add_to_cart_p207():
    ci = dm.add_to_cart_p207()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2208")
def add_to_cart_p208():
    ci = dm.add_to_cart_p208()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2209")
def add_to_cart_p209():
    ci = dm.add_to_cart_p209()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2210")
def add_to_cart_p210():
    ci = dm.add_to_cart_p210()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2211")
def add_to_cart_p211():
    ci = dm.add_to_cart_p211()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2212")
def add_to_cart_p212():
    ci = dm.add_to_cart_p212()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2213")
def add_to_cart_p213():
    ci = dm.add_to_cart_p213()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2214")
def add_to_cart_p214():
    ci = dm.add_to_cart_p214()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2215")
def add_to_cart_p215():
    ci = dm.add_to_cart_p215()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2216")
def add_to_cart_p216():
    ci = dm.add_to_cart_p216()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2217")
def add_to_cart_p217():
    ci = dm.add_to_cart_p217()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2218")
def add_to_cart_p218():
    ci = dm.add_to_cart_p218()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2219")
def add_to_cart_p219():
    ci = dm.add_to_cart_p219()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2220")
def add_to_cart_p220():
    ci = dm.add_to_cart_p220()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2221")
def add_to_cart_p221():
    ci = dm.add_to_cart_p221()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2222")
def add_to_cart_p222():
    ci = dm.add_to_cart_p222()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2223")
def add_to_cart_p223():
    ci = dm.add_to_cart_p223()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2224")
def add_to_cart_p224():
    ci = dm.add_to_cart_p224()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2225")
def add_to_cart_p225():
    ci = dm.add_to_cart_p225()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2226")
def add_to_cart_p226():
    ci = dm.add_to_cart_p226()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2227")
def add_to_cart_p227():
    ci = dm.add_to_cart_p227()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2228")
def add_to_cart_p228():
    ci = dm.add_to_cart_p228()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2229")
def add_to_cart_p229():
    ci = dm.add_to_cart_p229()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2230")
def add_to_cart_p230():
    ci = dm.add_to_cart_p230()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2231")
def add_to_cart_p231():
    ci = dm.add_to_cart_p231()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2232")
def add_to_cart_p232():
    ci = dm.add_to_cart_p232()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2233")
def add_to_cart_p233():
    ci = dm.add_to_cart_p233()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2234")
def add_to_cart_p234():
    ci = dm.add_to_cart_p234()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2235")
def add_to_cart_p235():
    ci = dm.add_to_cart_p235()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2236")
def add_to_cart_p236():
    ci = dm.add_to_cart_p236()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2237")
def add_to_cart_p237():
    ci = dm.add_to_cart_p237()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2238")
def add_to_cart_p238():
    ci = dm.add_to_cart_p238()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2239")
def add_to_cart_p239():
    ci = dm.add_to_cart_p239()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2240")
def add_to_cart_p240():
    ci = dm.add_to_cart_p240()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2241")
def add_to_cart_p241():
    ci = dm.add_to_cart_p241()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2242")
def add_to_cart_p242():
    ci = dm.add_to_cart_p242()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2243")
def add_to_cart_p243():
    ci = dm.add_to_cart_p243()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2244")
def add_to_cart_p244():
    ci = dm.add_to_cart_p244()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2245")
def add_to_cart_p245():
    ci = dm.add_to_cart_p245()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2246")
def add_to_cart_p246():
    ci = dm.add_to_cart_p246()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2247")
def add_to_cart_p247():
    ci = dm.add_to_cart_p247()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2248")
def add_to_cart_p248():
    ci = dm.add_to_cart_p248()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2249")
def add_to_cart_p249():
    ci = dm.add_to_cart_p249()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2250")
def add_to_cart_p250():
    ci = dm.add_to_cart_p250()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2251")
def add_to_cart_p251():
    ci = dm.add_to_cart_p251()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2252")
def add_to_cart_p252():
    ci = dm.add_to_cart_p252()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2253")
def add_to_cart_p253():
    ci = dm.add_to_cart_p253()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2254")
def add_to_cart_p254():
    ci = dm.add_to_cart_p254()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2255")
def add_to_cart_p255():
    ci = dm.add_to_cart_p255()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2256")
def add_to_cart_p256():
    ci = dm.add_to_cart_p256()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2257")
def add_to_cart_p257():
    ci = dm.add_to_cart_p257()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2258")
def add_to_cart_p258():
    ci = dm.add_to_cart_p258()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2259")
def add_to_cart_p259():
    ci = dm.add_to_cart_p259()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2260")
def add_to_cart_p260():
    ci = dm.add_to_cart_p260()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2261")
def add_to_cart_p261():
    ci = dm.add_to_cart_p261()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2262")
def add_to_cart_p262():
    ci = dm.add_to_cart_p262()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2263")
def add_to_cart_p263():
    ci = dm.add_to_cart_p263()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2264")
def add_to_cart_p264():
    ci = dm.add_to_cart_p264()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2265")
def add_to_cart_p265():
    ci = dm.add_to_cart_p265()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2266")
def add_to_cart_p266():
    ci = dm.add_to_cart_p266()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2267")
def add_to_cart_p267():
    ci = dm.add_to_cart_p267()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2268")
def add_to_cart_p268():
    ci = dm.add_to_cart_p268()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2269")
def add_to_cart_p269():
    ci = dm.add_to_cart_p269()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2270")
def add_to_cart_p270():
    ci = dm.add_to_cart_p270()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2271")
def add_to_cart_p271():
    ci = dm.add_to_cart_p271()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2272")
def add_to_cart_p272():
    ci = dm.add_to_cart_p272()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2273")
def add_to_cart_p273():
    ci = dm.add_to_cart_p273()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2274")
def add_to_cart_p274():
    ci = dm.add_to_cart_p274()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2275")
def add_to_cart_p275():
    ci = dm.add_to_cart_p275()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2276")
def add_to_cart_p276():
    ci = dm.add_to_cart_p276()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2277")
def add_to_cart_p277():
    ci = dm.add_to_cart_p277()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2278")
def add_to_cart_p278():
    ci = dm.add_to_cart_p278()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2279")
def add_to_cart_p279():
    ci = dm.add_to_cart_p279()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2280")
def add_to_cart_p280():
    ci = dm.add_to_cart_p280()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2281")
def add_to_cart_p281():
    ci = dm.add_to_cart_p281()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2282")
def add_to_cart_p282():
    ci = dm.add_to_cart_p282()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2283")
def add_to_cart_p283():
    ci = dm.add_to_cart_p283()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2284")
def add_to_cart_p284():
    ci = dm.add_to_cart_p284()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2285")
def add_to_cart_p285():
    ci = dm.add_to_cart_p285()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2286")
def add_to_cart_p286():
    ci = dm.add_to_cart_p286()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2287")
def add_to_cart_p287():
    ci = dm.add_to_cart_p287()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2288")
def add_to_cart_p288():
    ci = dm.add_to_cart_p288()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2289")
def add_to_cart_p289():
    ci = dm.add_to_cart_p289()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2290")
def add_to_cart_p290():
    ci = dm.add_to_cart_p290()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2291")
def add_to_cart_p291():
    ci = dm.add_to_cart_p291()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2292")
def add_to_cart_p292():
    ci = dm.add_to_cart_p292()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2293")
def add_to_cart_p293():
    ci = dm.add_to_cart_p293()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2294")
def add_to_cart_p294():
    ci = dm.add_to_cart_p294()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2295")
def add_to_cart_p295():
    ci = dm.add_to_cart_p295()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2296")
def add_to_cart_p296():
    ci = dm.add_to_cart_p296()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2297")
def add_to_cart_p297():
    ci = dm.add_to_cart_p297()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2298")
def add_to_cart_p298():
    ci = dm.add_to_cart_p298()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2299")
def add_to_cart_p299():
    ci = dm.add_to_cart_p299()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2300")
def add_to_cart_p300():
    ci = dm.add_to_cart_p300()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2301")
def add_to_cart_p301():
    ci = dm.add_to_cart_p301()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2302")
def add_to_cart_p302():
    ci = dm.add_to_cart_p302()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2303")
def add_to_cart_p303():
    ci = dm.add_to_cart_p303()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2304")
def add_to_cart_p304():
    ci = dm.add_to_cart_p304()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2305")
def add_to_cart_p305():
    ci = dm.add_to_cart_p305()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2306")
def add_to_cart_p306():
    ci = dm.add_to_cart_p306()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2307")
def add_to_cart_p307():
    ci = dm.add_to_cart_p307()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2308")
def add_to_cart_p308():
    ci = dm.add_to_cart_p308()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2309")
def add_to_cart_p309():
    ci = dm.add_to_cart_p309()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2310")
def add_to_cart_p310():
    ci = dm.add_to_cart_p310()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2311")
def add_to_cart_p311():
    ci = dm.add_to_cart_p311()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2312")
def add_to_cart_p312():
    ci = dm.add_to_cart_p312()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2313")
def add_to_cart_p313():
    ci = dm.add_to_cart_p313()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2314")
def add_to_cart_p314():
    ci = dm.add_to_cart_p314()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2315")
def add_to_cart_p315():
    ci = dm.add_to_cart_p315()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2316")
def add_to_cart_p316():
    ci = dm.add_to_cart_p316()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2317")
def add_to_cart_p317():
    ci = dm.add_to_cart_p317()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2318")
def add_to_cart_p318():
    ci = dm.add_to_cart_p318()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2319")
def add_to_cart_p319():
    ci = dm.add_to_cart_p319()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2320")
def add_to_cart_p320():
    ci = dm.add_to_cart_p320()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2321")
def add_to_cart_p321():
    ci = dm.add_to_cart_p321()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2322")
def add_to_cart_p322():
    ci = dm.add_to_cart_p322()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2323")
def add_to_cart_p323():
    ci = dm.add_to_cart_p323()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2324")
def add_to_cart_p324():
    ci = dm.add_to_cart_p324()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2325")
def add_to_cart_p325():
    ci = dm.add_to_cart_p325()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2326")
def add_to_cart_p326():
    ci = dm.add_to_cart_p326()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2327")
def add_to_cart_p327():
    ci = dm.add_to_cart_p327()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2328")
def add_to_cart_p328():
    ci = dm.add_to_cart_p328()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2329")
def add_to_cart_p329():
    ci = dm.add_to_cart_p329()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2330")
def add_to_cart_p330():
    ci = dm.add_to_cart_p330()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2331")
def add_to_cart_p331():
    ci = dm.add_to_cart_p331()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2332")
def add_to_cart_p332():
    ci = dm.add_to_cart_p332()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2333")
def add_to_cart_p333():
    ci = dm.add_to_cart_p333()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2334")
def add_to_cart_p334():
    ci = dm.add_to_cart_p334()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2335")
def add_to_cart_p335():
    ci = dm.add_to_cart_p335()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2336")
def add_to_cart_p336():
    ci = dm.add_to_cart_p336()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2337")
def add_to_cart_p337():
    ci = dm.add_to_cart_p337()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2338")
def add_to_cart_p338():
    ci = dm.add_to_cart_p338()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2339")
def add_to_cart_p339():
    ci = dm.add_to_cart_p339()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2340")
def add_to_cart_p340():
    ci = dm.add_to_cart_p340()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2341")
def add_to_cart_p341():
    ci = dm.add_to_cart_p341()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2342")
def add_to_cart_p342():
    ci = dm.add_to_cart_p342()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2343")
def add_to_cart_p343():
    ci = dm.add_to_cart_p343()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2344")
def add_to_cart_p344():
    ci = dm.add_to_cart_p344()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2345")
def add_to_cart_p345():
    ci = dm.add_to_cart_p345()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2346")
def add_to_cart_p346():
    ci = dm.add_to_cart_p346()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2347")
def add_to_cart_p347():
    ci = dm.add_to_cart_p347()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2348")
def add_to_cart_p348():
    ci = dm.add_to_cart_p348()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2349")
def add_to_cart_p349():
    ci = dm.add_to_cart_p349()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2350")
def add_to_cart_p350():
    ci = dm.add_to_cart_p350()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2351")
def add_to_cart_p351():
    ci = dm.add_to_cart_p351()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2352")
def add_to_cart_p352():
    ci = dm.add_to_cart_p352()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2353")
def add_to_cart_p353():
    ci = dm.add_to_cart_p353()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2354")
def add_to_cart_p354():
    ci = dm.add_to_cart_p354()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2355")
def add_to_cart_p355():
    ci = dm.add_to_cart_p355()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2356")
def add_to_cart_p356():
    ci = dm.add_to_cart_p356()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2357")
def add_to_cart_p357():
    ci = dm.add_to_cart_p357()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2358")
def add_to_cart_p358():
    ci = dm.add_to_cart_p358()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2359")
def add_to_cart_p359():
    ci = dm.add_to_cart_p359()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2360")
def add_to_cart_p360():
    ci = dm.add_to_cart_p360()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2361")
def add_to_cart_p361():
    ci = dm.add_to_cart_p361()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2362")
def add_to_cart_p362():
    ci = dm.add_to_cart_p362()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2363")
def add_to_cart_p363():
    ci = dm.add_to_cart_p363()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2364")
def add_to_cart_p364():
    ci = dm.add_to_cart_p364()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2365")
def add_to_cart_p365():
    ci = dm.add_to_cart_p365()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2366")
def add_to_cart_p366():
    ci = dm.add_to_cart_p366()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2367")
def add_to_cart_p367():
    ci = dm.add_to_cart_p367()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2368")
def add_to_cart_p368():
    ci = dm.add_to_cart_p368()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2369")
def add_to_cart_p369():
    ci = dm.add_to_cart_p369()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2370")
def add_to_cart_p370():
    ci = dm.add_to_cart_p370()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2371")
def add_to_cart_p371():
    ci = dm.add_to_cart_p371()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2372")
def add_to_cart_p372():
    ci = dm.add_to_cart_p372()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2373")
def add_to_cart_p373():
    ci = dm.add_to_cart_p373()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2374")
def add_to_cart_p374():
    ci = dm.add_to_cart_p374()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2375")
def add_to_cart_p375():
    ci = dm.add_to_cart_p375()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2376")
def add_to_cart_p376():
    ci = dm.add_to_cart_p376()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2377")
def add_to_cart_p377():
    ci = dm.add_to_cart_p377()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2378")
def add_to_cart_p378():
    ci = dm.add_to_cart_p378()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2379")
def add_to_cart_p379():
    ci = dm.add_to_cart_p379()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2380")
def add_to_cart_p380():
    ci = dm.add_to_cart_p380()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2381")
def add_to_cart_p381():
    ci = dm.add_to_cart_p381()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2382")
def add_to_cart_p382():
    ci = dm.add_to_cart_p382()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2383")
def add_to_cart_p383():
    ci = dm.add_to_cart_p383()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2384")
def add_to_cart_p384():
    ci = dm.add_to_cart_p384()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2385")
def add_to_cart_p385():
    ci = dm.add_to_cart_p385()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2386")
def add_to_cart_p386():
    ci = dm.add_to_cart_p386()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2387")
def add_to_cart_p387():
    ci = dm.add_to_cart_p387()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2388")
def add_to_cart_p388():
    ci = dm.add_to_cart_p388()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2389")
def add_to_cart_p389():
    ci = dm.add_to_cart_p389()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2390")
def add_to_cart_p390():
    ci = dm.add_to_cart_p390()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2391")
def add_to_cart_p391():
    ci = dm.add_to_cart_p391()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2392")
def add_to_cart_p392():
    ci = dm.add_to_cart_p392()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2393")
def add_to_cart_p393():
    ci = dm.add_to_cart_p393()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2394")
def add_to_cart_p394():
    ci = dm.add_to_cart_p394()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2395")
def add_to_cart_p395():
    ci = dm.add_to_cart_p395()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2396")
def add_to_cart_p396():
    ci = dm.add_to_cart_p396()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2397")
def add_to_cart_p397():
    ci = dm.add_to_cart_p397()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2398")
def add_to_cart_p398():
    ci = dm.add_to_cart_p398()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2399")
def add_to_cart_p399():
    ci = dm.add_to_cart_p399()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2400")
def add_to_cart_p400():
    ci = dm.add_to_cart_p400()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2401")
def add_to_cart_p401():
    ci = dm.add_to_cart_p401()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2402")
def add_to_cart_p402():
    ci = dm.add_to_cart_p402()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2403")
def add_to_cart_p403():
    ci = dm.add_to_cart_p403()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2404")
def add_to_cart_p404():
    ci = dm.add_to_cart_p404()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2405")
def add_to_cart_p405():
    ci = dm.add_to_cart_p405()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2406")
def add_to_cart_p406():
    ci = dm.add_to_cart_p406()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2407")
def add_to_cart_p407():
    ci = dm.add_to_cart_p407()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2408")
def add_to_cart_p408():
    ci = dm.add_to_cart_p408()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2409")
def add_to_cart_p409():
    ci = dm.add_to_cart_p409()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2410")
def add_to_cart_p410():
    ci = dm.add_to_cart_p410()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2411")
def add_to_cart_p411():
    ci = dm.add_to_cart_p411()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2412")
def add_to_cart_p412():
    ci = dm.add_to_cart_p412()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2413")
def add_to_cart_p413():
    ci = dm.add_to_cart_p413()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2414")
def add_to_cart_p414():
    ci = dm.add_to_cart_p414()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2415")
def add_to_cart_p415():
    ci = dm.add_to_cart_p415()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2416")
def add_to_cart_p416():
    ci = dm.add_to_cart_p416()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2417")
def add_to_cart_p417():
    ci = dm.add_to_cart_p417()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2418")
def add_to_cart_p418():
    ci = dm.add_to_cart_p418()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2419")
def add_to_cart_p419():
    ci = dm.add_to_cart_p419()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2420")
def add_to_cart_p420():
    ci = dm.add_to_cart_p420()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2421")
def add_to_cart_p421():
    ci = dm.add_to_cart_p421()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2422")
def add_to_cart_p422():
    ci = dm.add_to_cart_p422()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2423")
def add_to_cart_p423():
    ci = dm.add_to_cart_p423()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2424")
def add_to_cart_p424():
    ci = dm.add_to_cart_p424()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2425")
def add_to_cart_p425():
    ci = dm.add_to_cart_p425()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2426")
def add_to_cart_p426():
    ci = dm.add_to_cart_p426()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2427")
def add_to_cart_p427():
    ci = dm.add_to_cart_p427()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2428")
def add_to_cart_p428():
    ci = dm.add_to_cart_p428()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2429")
def add_to_cart_p429():
    ci = dm.add_to_cart_p429()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2430")
def add_to_cart_p430():
    ci = dm.add_to_cart_p430()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2431")
def add_to_cart_p431():
    ci = dm.add_to_cart_p431()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2432")
def add_to_cart_p432():
    ci = dm.add_to_cart_p432()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2433")
def add_to_cart_p433():
    ci = dm.add_to_cart_p433()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2434")
def add_to_cart_p434():
    ci = dm.add_to_cart_p434()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2435")
def add_to_cart_p435():
    ci = dm.add_to_cart_p435()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2436")
def add_to_cart_p436():
    ci = dm.add_to_cart_p436()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2437")
def add_to_cart_p437():
    ci = dm.add_to_cart_p437()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2438")
def add_to_cart_p438():
    ci = dm.add_to_cart_p438()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2439")
def add_to_cart_p439():
    ci = dm.add_to_cart_p439()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2440")
def add_to_cart_p440():
    ci = dm.add_to_cart_p440()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2441")
def add_to_cart_p441():
    ci = dm.add_to_cart_p441()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2442")
def add_to_cart_p442():
    ci = dm.add_to_cart_p442()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2443")
def add_to_cart_p443():
    ci = dm.add_to_cart_p443()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2444")
def add_to_cart_p444():
    ci = dm.add_to_cart_p444()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2445")
def add_to_cart_p445():
    ci = dm.add_to_cart_p445()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2446")
def add_to_cart_p446():
    ci = dm.add_to_cart_p446()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2447")
def add_to_cart_p447():
    ci = dm.add_to_cart_p447()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2448")
def add_to_cart_p448():
    ci = dm.add_to_cart_p448()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2449")
def add_to_cart_p449():
    ci = dm.add_to_cart_p449()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2450")
def add_to_cart_p450():
    ci = dm.add_to_cart_p450()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2451")
def add_to_cart_p451():
    ci = dm.add_to_cart_p451()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2452")
def add_to_cart_p452():
    ci = dm.add_to_cart_p452()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2453")
def add_to_cart_p453():
    ci = dm.add_to_cart_p453()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2454")
def add_to_cart_p454():
    ci = dm.add_to_cart_p454()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2455")
def add_to_cart_p455():
    ci = dm.add_to_cart_p455()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2456")
def add_to_cart_p456():
    ci = dm.add_to_cart_p456()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2457")
def add_to_cart_p457():
    ci = dm.add_to_cart_p457()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2458")
def add_to_cart_p458():
    ci = dm.add_to_cart_p458()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2459")
def add_to_cart_p459():
    ci = dm.add_to_cart_p459()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2460")
def add_to_cart_p460():
    ci = dm.add_to_cart_p460()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2461")
def add_to_cart_p461():
    ci = dm.add_to_cart_p461()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2462")
def add_to_cart_p462():
    ci = dm.add_to_cart_p462()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2463")
def add_to_cart_p463():
    ci = dm.add_to_cart_p463()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2464")
def add_to_cart_p464():
    ci = dm.add_to_cart_p464()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2465")
def add_to_cart_p465():
    ci = dm.add_to_cart_p465()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2466")
def add_to_cart_p466():
    ci = dm.add_to_cart_p466()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2467")
def add_to_cart_p467():
    ci = dm.add_to_cart_p467()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2468")
def add_to_cart_p468():
    ci = dm.add_to_cart_p468()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2469")
def add_to_cart_p469():
    ci = dm.add_to_cart_p469()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2470")
def add_to_cart_p470():
    ci = dm.add_to_cart_p470()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2471")
def add_to_cart_p471():
    ci = dm.add_to_cart_p471()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2472")
def add_to_cart_p472():
    ci = dm.add_to_cart_p472()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2473")
def add_to_cart_p473():
    ci = dm.add_to_cart_p473()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2474")
def add_to_cart_p474():
    ci = dm.add_to_cart_p474()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2475")
def add_to_cart_p475():
    ci = dm.add_to_cart_p475()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2476")
def add_to_cart_p476():
    ci = dm.add_to_cart_p476()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2477")
def add_to_cart_p477():
    ci = dm.add_to_cart_p477()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2478")
def add_to_cart_p478():
    ci = dm.add_to_cart_p478()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2479")
def add_to_cart_p479():
    ci = dm.add_to_cart_p479()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2480")
def add_to_cart_p480():
    ci = dm.add_to_cart_p480()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2481")
def add_to_cart_p481():
    ci = dm.add_to_cart_p481()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2482")
def add_to_cart_p482():
    ci = dm.add_to_cart_p482()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2483")
def add_to_cart_p483():
    ci = dm.add_to_cart_p483()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2484")
def add_to_cart_p484():
    ci = dm.add_to_cart_p484()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2485")
def add_to_cart_p485():
    ci = dm.add_to_cart_p485()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2486")
def add_to_cart_p486():
    ci = dm.add_to_cart_p486()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2487")
def add_to_cart_p487():
    ci = dm.add_to_cart_p487()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2488")
def add_to_cart_p488():
    ci = dm.add_to_cart_p488()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2489")
def add_to_cart_p489():
    ci = dm.add_to_cart_p489()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2490")
def add_to_cart_p490():
    ci = dm.add_to_cart_p490()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2491")
def add_to_cart_p491():
    ci = dm.add_to_cart_p491()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2492")
def add_to_cart_p492():
    ci = dm.add_to_cart_p492()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2493")
def add_to_cart_p493():
    ci = dm.add_to_cart_p493()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2494")
def add_to_cart_p494():
    ci = dm.add_to_cart_p494()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2495")
def add_to_cart_p495():
    ci = dm.add_to_cart_p495()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2496")
def add_to_cart_p496():
    ci = dm.add_to_cart_p496()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2497")
def add_to_cart_p497():
    ci = dm.add_to_cart_p497()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2498")
def add_to_cart_p498():
    ci = dm.add_to_cart_p498()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2499")
def add_to_cart_p499():
    ci = dm.add_to_cart_p499()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2500")
def add_to_cart_p500():
    ci = dm.add_to_cart_p500()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2501")
def add_to_cart_p501():
    ci = dm.add_to_cart_p501()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2502")
def add_to_cart_p502():
    ci = dm.add_to_cart_p502()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2503")
def add_to_cart_p503():
    ci = dm.add_to_cart_p503()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2504")
def add_to_cart_p504():
    ci = dm.add_to_cart_p504()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2505")
def add_to_cart_p505():
    ci = dm.add_to_cart_p505()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2506")
def add_to_cart_p506():
    ci = dm.add_to_cart_p506()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2507")
def add_to_cart_p507():
    ci = dm.add_to_cart_p507()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2508")
def add_to_cart_p508():
    ci = dm.add_to_cart_p508()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2509")
def add_to_cart_p509():
    ci = dm.add_to_cart_p509()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2510")
def add_to_cart_p510():
    ci = dm.add_to_cart_p510()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2511")
def add_to_cart_p511():
    ci = dm.add_to_cart_p511()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2512")
def add_to_cart_p512():
    ci = dm.add_to_cart_p512()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2513")
def add_to_cart_p513():
    ci = dm.add_to_cart_p513()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2514")
def add_to_cart_p514():
    ci = dm.add_to_cart_p514()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2515")
def add_to_cart_p515():
    ci = dm.add_to_cart_p515()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2516")
def add_to_cart_p516():
    ci = dm.add_to_cart_p516()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2517")
def add_to_cart_p517():
    ci = dm.add_to_cart_p517()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2518")
def add_to_cart_p518():
    ci = dm.add_to_cart_p518()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2519")
def add_to_cart_p519():
    ci = dm.add_to_cart_p519()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2520")
def add_to_cart_p520():
    ci = dm.add_to_cart_p520()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2521")
def add_to_cart_p521():
    ci = dm.add_to_cart_p521()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2522")
def add_to_cart_p522():
    ci = dm.add_to_cart_p522()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2523")
def add_to_cart_p523():
    ci = dm.add_to_cart_p523()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2524")
def add_to_cart_p524():
    ci = dm.add_to_cart_p524()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2525")
def add_to_cart_p525():
    ci = dm.add_to_cart_p525()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2526")
def add_to_cart_p526():
    ci = dm.add_to_cart_p526()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2527")
def add_to_cart_p527():
    ci = dm.add_to_cart_p527()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2528")
def add_to_cart_p528():
    ci = dm.add_to_cart_p528()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2529")
def add_to_cart_p529():
    ci = dm.add_to_cart_p529()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2530")
def add_to_cart_p530():
    ci = dm.add_to_cart_p530()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2531")
def add_to_cart_p531():
    ci = dm.add_to_cart_p531()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2532")
def add_to_cart_p532():
    ci = dm.add_to_cart_p532()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2533")
def add_to_cart_p533():
    ci = dm.add_to_cart_p533()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2534")
def add_to_cart_p534():
    ci = dm.add_to_cart_p534()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2535")
def add_to_cart_p535():
    ci = dm.add_to_cart_p535()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2536")
def add_to_cart_p536():
    ci = dm.add_to_cart_p536()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2537")
def add_to_cart_p537():
    ci = dm.add_to_cart_p537()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2538")
def add_to_cart_p538():
    ci = dm.add_to_cart_p538()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2539")
def add_to_cart_p539():
    ci = dm.add_to_cart_p539()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2540")
def add_to_cart_p540():
    ci = dm.add_to_cart_p540()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2541")
def add_to_cart_p541():
    ci = dm.add_to_cart_p541()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2542")
def add_to_cart_p542():
    ci = dm.add_to_cart_p542()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2543")
def add_to_cart_p543():
    ci = dm.add_to_cart_p543()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2544")
def add_to_cart_p544():
    ci = dm.add_to_cart_p544()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2545")
def add_to_cart_p545():
    ci = dm.add_to_cart_p545()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2546")
def add_to_cart_p546():
    ci = dm.add_to_cart_p546()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2547")
def add_to_cart_p547():
    ci = dm.add_to_cart_p547()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2548")
def add_to_cart_p548():
    ci = dm.add_to_cart_p548()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2549")
def add_to_cart_p549():
    ci = dm.add_to_cart_p549()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2550")
def add_to_cart_p550():
    ci = dm.add_to_cart_p550()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2551")
def add_to_cart_p551():
    ci = dm.add_to_cart_p551()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2552")
def add_to_cart_p552():
    ci = dm.add_to_cart_p552()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2553")
def add_to_cart_p553():
    ci = dm.add_to_cart_p553()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2554")
def add_to_cart_p554():
    ci = dm.add_to_cart_p554()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2555")
def add_to_cart_p555():
    ci = dm.add_to_cart_p555()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2556")
def add_to_cart_p556():
    ci = dm.add_to_cart_p556()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2557")
def add_to_cart_p557():
    ci = dm.add_to_cart_p557()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2558")
def add_to_cart_p558():
    ci = dm.add_to_cart_p558()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2559")
def add_to_cart_p559():
    ci = dm.add_to_cart_p559()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2560")
def add_to_cart_p560():
    ci = dm.add_to_cart_p560()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2561")
def add_to_cart_p561():
    ci = dm.add_to_cart_p561()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2562")
def add_to_cart_p562():
    ci = dm.add_to_cart_p562()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2563")
def add_to_cart_p563():
    ci = dm.add_to_cart_p563()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2564")
def add_to_cart_p564():
    ci = dm.add_to_cart_p564()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2565")
def add_to_cart_p565():
    ci = dm.add_to_cart_p565()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2566")
def add_to_cart_p566():
    ci = dm.add_to_cart_p566()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2567")
def add_to_cart_p567():
    ci = dm.add_to_cart_p567()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2568")
def add_to_cart_p568():
    ci = dm.add_to_cart_p568()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2569")
def add_to_cart_p569():
    ci = dm.add_to_cart_p569()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2570")
def add_to_cart_p570():
    ci = dm.add_to_cart_p570()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2571")
def add_to_cart_p571():
    ci = dm.add_to_cart_p571()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2572")
def add_to_cart_p572():
    ci = dm.add_to_cart_p572()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2573")
def add_to_cart_p573():
    ci = dm.add_to_cart_p573()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2574")
def add_to_cart_p574():
    ci = dm.add_to_cart_p574()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2575")
def add_to_cart_p575():
    ci = dm.add_to_cart_p575()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2576")
def add_to_cart_p576():
    ci = dm.add_to_cart_p576()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2577")
def add_to_cart_p577():
    ci = dm.add_to_cart_p577()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2578")
def add_to_cart_p578():
    ci = dm.add_to_cart_p578()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2579")
def add_to_cart_p579():
    ci = dm.add_to_cart_p579()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2580")
def add_to_cart_p580():
    ci = dm.add_to_cart_p580()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2581")
def add_to_cart_p581():
    ci = dm.add_to_cart_p581()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2582")
def add_to_cart_p582():
    ci = dm.add_to_cart_p582()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2583")
def add_to_cart_p583():
    ci = dm.add_to_cart_p583()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2584")
def add_to_cart_p584():
    ci = dm.add_to_cart_p584()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2585")
def add_to_cart_p585():
    ci = dm.add_to_cart_p585()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2586")
def add_to_cart_p586():
    ci = dm.add_to_cart_p586()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2587")
def add_to_cart_p587():
    ci = dm.add_to_cart_p587()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2588")
def add_to_cart_p588():
    ci = dm.add_to_cart_p588()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2589")
def add_to_cart_p589():
    ci = dm.add_to_cart_p589()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2590")
def add_to_cart_p590():
    ci = dm.add_to_cart_p590()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2591")
def add_to_cart_p591():
    ci = dm.add_to_cart_p591()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)

@app.route("/index2592")
def add_to_cart_p592():
    ci = dm.add_to_cart_p592()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)



# added end

@app.route("/cart")
def cart():
    list_of_lists=dm.cart()
    
    
    
    return render_template("/templates/cart.html", cart_items=list_of_lists[0], total_price=list_of_lists[1], num_items=list_of_lists[2], list_names=list_of_lists[3],list_price=list_of_lists[4],discount=list_of_lists[5])



@app.route("/clothing")
def clothing():
    
    
    c1=dm.clothing1()
    c2=dm.clothing2()
    c3=dm.clothing3()
    c4=dm.clothing4()
    
    print(c1)
    return render_template("/for_index2/dist/index_clothing.html",list_pid=c1,list_prod_name=c2,list_price=c3,num=c4)

@app.route("/electronics")
def electronics():
    
    
    c1=dm.electronics1()
    c2=dm.electronics2()
    c3=dm.electronics3()
    c4=dm.electronics4()
    
    
    return render_template("/for_index2/dist/index_electronics.html",list_pid=c1,list_prod_name=c2,list_price=c3,num=c4)

@app.route("/consumables")
def consumables():
    
    
    c1=dm.consumables1()
    c2=dm.consumables2()
    c3=dm.consumables3()
    c4=dm.consumables4()

    print(c1)
    
    
    return render_template("/for_index2/dist/index_consumables.html",list_pid=c1,list_prod_name=c2,list_price=c3,num=c4)

@app.route("/cosmetics")
def cosmetics():
    
    
    c1=dm.cosmetics1()
    c2=dm.cosmetics2()
    c3=dm.cosmetics3()
    c4=dm.cosmetics4()
    
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    return render_template("/for_index2/dist/index_cosmetics.html",list_pid=c1,list_prod_name=c2,list_price=c3,num=c4)

















if __name__ == "__main__":
    app.run(debug=True)

