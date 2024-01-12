
from flask import Flask, render_template, url_for, redirect, request

import demo as dm

app = Flask(__name__,template_folder="C:/Users/suris/Desktop/DBMS/Project/A6/ValueBuy")




import mysql.connector
mydb  = mysql.connector.connect(host = "localhost",user = "root" , passwd = "MySQL2023",database = "final_final")

mycur = mydb.cursor()












@app.route("/" , methods= ["POST", "GET"])
def login():
    if request.method =="POST":
        user = request.form["username"]
        passwd = request.form["password"]

        if dm.check_login(user, passwd):
            return redirect(url_for("welcome", name = user))
    else:
        return render_template("/templates/loginpage.html")
    
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     # Implement the sign up functionality here
#     return render_template('signup.html')

@app.route('/admin/delete-product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    # Delete the product with the specified ID from the database
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM products WHERE id = %s', (product_id,))
    db.commit()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/add-product', methods=['POST'])
def add_product():
    # Get the data from the form
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    image = request.files['image']
    # Save the image to the file system
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # Insert the new product into the database
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO products (name, description, price, image) VALUES (%s, %s, %s, %s)',
                   (name, description, price, filename))
    db.commit()
    flash('Product added successfully', 'success')
    return redirect(url_for('admin'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Insert user into MySQL database
        dm.signup(username,password)

        # Redirect to login page
        return redirect(url_for('login'))

    # Render signup page
    return render_template('signup.html')


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



@app.route("/index2")
def index2():
    
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)
    #return render_template("C:/Users/suris/Desktop/DBMS/Project/A6/ValueBuy/for_index2/dist/index.html")   

@app.route("/index3")
def index3():
    
    return render_template("/for_index3/dist/index.html")



@app.route("/index21")
def added_to_cart_p1():
    
    ci = dm.add_to_cart_p1()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index22")
def added_to_cart_p2():
    
    ci = dm.add_to_cart_p2()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index23")
def added_to_cart_p3():
    
    ci = dm.add_to_cart_p3()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index24")
def added_to_cart_p4():
    
    ci = dm.add_to_cart_p4()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index25")
def added_to_cart_p5():
    
    ci = dm.add_to_cart_p5()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index26")
def added_to_cart_p6():
    
    ci = dm.add_to_cart_p6()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

    return None

@app.route("/index27")
def added_to_cart_p7():
    
    ci = dm.add_to_cart_p7()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


@app.route("/index28")
def added_to_cart_p8():
    
    ci = dm.add_to_cart_p8()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)


# adding now

@app.route("/index29")
def add_to_cart_p9():
    
    ci = dm.add_to_cart_p9()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index210")
def add_to_cart_p10():
    
    ci = dm.add_to_cart_p10()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index211")
def add_to_cart_p11():
    
    ci = dm.add_to_cart_p11()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index212")
def add_to_cart_p12():
    
    ci = dm.add_to_cart_p12()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index213")
def add_to_cart_p13():
    
    ci = dm.add_to_cart_p13()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index214")
def add_to_cart_p14():
    
    ci = dm.add_to_cart_p14()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index215")
def add_to_cart_p15():
    
    ci = dm.add_to_cart_p15()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index216")
def add_to_cart_p16():
    
    ci = dm.add_to_cart_p16()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index217")
def add_to_cart_p17():
    
    ci = dm.add_to_cart_p17()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index218")
def add_to_cart_p18():
    
    ci = dm.add_to_cart_p18()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index219")
def add_to_cart_p19():
    
    ci = dm.add_to_cart_p19()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index220")
def add_to_cart_p20():
    
    ci = dm.add_to_cart_p20()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index221")
def add_to_cart_21():
    
    ci = dm.add_to_cart_p21()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index222")
def add_to_cart_p22():
    
    ci = dm.add_to_cart_p22()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index223")
def add_to_cart_p23():
    
    ci = dm.add_to_cart_p23()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index224")
def add_to_cart_p24():
    
    ci = dm.add_to_cart_p24()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index225")
def add_to_cart_p25():
    
    ci = dm.add_to_cart_p25()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index226")
def add_to_cart_p26():
    
    ci = dm.add_to_cart_p26()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

# @app.route("/index226")
# def added_to_cart_p26():
    
#     ci = dm.add_to_cart_p26()
#     mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
#     data = mycur.fetchall()

    
#     print(data[0][0])

#     list_pid=[]
#     for i in range(len(data)):
#         list_pid.append(data[i][0])

#     mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
#     data = mycur.fetchall()

#     list_prod_name=[]
#     for i in range(len(data)):
#         list_prod_name.append(data[i][0])

#     mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
#     data = mycur.fetchall()

#     list_price=[]
#     for i in range(len(data)):
#         list_price.append(data[i][0])
#     #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index227")
def add_to_cart_p27():
    
    ci = dm.add_to_cart_p27()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index228")
def add_to_cart_p28():
    
    ci = dm.add_to_cart_p28()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index229")
def add_to_cart_p29():
    
    ci = dm.add_to_cart_p29()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index230")
def add_to_cart_p30():
    
    ci = dm.add_to_cart_p30()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)
    #return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price)

@app.route("/index231")
def add_to_cart_p31():
    
    ci = dm.add_to_cart_p31()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1


    return render_template("/for_index2/dist/index.html",list_pid=list_pid,list_prod_name=list_prod_name,list_price=list_price,num=num)



# added end

@app.route("/cart")
def cart():
    
    mycur.execute("""select amount from cart where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    # print(data)
    sum=data[0][0]

    # for i in data:
    #     sum+=int(i)

    
    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    list1=[]
    num=0

    list_names=[]

    list_price=[]

    for i in data:
        num+=1
        
        p_id = i[0]
        mycur.execute("SELECT prod_name FROM product WHERE p_id = %s", (p_id,))
        data2=mycur.fetchall()

        list_names.append(data2)

        mycur.execute("SELECT price FROM product WHERE p_id = %s", (p_id,))
        data3=mycur.fetchall()

        list_price.append(data3)

        list1.append(i[0])


    print(list1)
    print(list_names)
    print(list_price)
    
    return render_template("/templates/cart.html", cart_items=list1, total_price=sum, num_items=num, list_names=list_names,list_price=list_price)



@app.route("/clothing")
def clothing():
    
    
    c1=dm.clothing1()
    c2=dm.clothing2()
    c3=dm.clothing3()
    c4=dm.clothing4()
    
    
    return render_template("/for_index2/dist/index.html",list_pid=c1,list_prod_name=c2,list_price=c3,num=c4)

@app.route("/electronics")
def clothing():
    
    
    c1=dm.electronics1()
    c2=dm.electronics2()
    c3=dm.electronics3()
    c4=dm.electronics4()
    
    
    return render_template("/for_index2/dist/index.html",list_pid=c1,list_prod_name=c2,list_price=c3,num=c4)

@app.route("/consumables")
def clothing():
    
    
    c1=dm.consumables1()
    c2=dm.consumables2()
    c3=dm.consumables3()
    c4=dm.consumables4()
    
    
    return render_template("/for_index2/dist/index.html",list_pid=c1,list_prod_name=c2,list_price=c3,num=c4)

@app.route("/cosmetics")
def clothing():
    
    
    c1=dm.cosmetics1()
    c2=dm.cosmetics2()
    c3=dm.cosmetics3()
    c4=dm.cosmetics4()
    
    
    return render_template("/for_index2/dist/index.html",list_pid=c1,list_prod_name=c2,list_price=c3,num=c4)




# later

# @app.route("/index39")
# def added_to_cart_p9():
    
#     ci = dm.add_to_cart_p9()
#     return render_template('/for_index3/dist/index.html')


# @app.route("/index310")
# def added_to_cart_p10():
    
#     ci = dm.add_to_cart_p10()
#     return render_template('/for_index3/dist/index.html')

# @app.route("/index311")
# def added_to_cart_p11():
    
#     ci = dm.add_to_cart_p11()
#     return render_template('/for_index3/dist/index.html')

# @app.route("/index312")
# def added_to_cart_p12():
    
#     ci = dm.add_to_cart_p12()
#     return render_template('/for_index3/dist/index.html')






















# @app.route("/clothing")
# def clothing():
#     cloths = dm.get_cloths()
#     return render_template("/templates/clothing.html", list = cloths)

# @app.route("/products")
# def products():
#     products = dm.get_all_products()
#     return render_template("/templates/clothing.html", list = products)

# @app.route("/cosmetics")
# def cosmetics():
#     cosmetics = dm.get_cosmetics()
#     return render_template("/templates/cosmetics.html", list = cosmetics)

# @app.route("/electronics")
# def electronics():
#     electronics = dm.get_electronics()
#     return render_template("/templates/electronics.html", list = electronics)

# @app.route("/consumables")
# def consumables():
#     consumables = dm.get_consumables()
#     return render_template("/templates/consumables.html", list = consumables)

# @app.route("/customer")
# def Customers():
#     Customers = dm.get_Customers()
#     return render_template("/templates/customer.html", list = Customers)

# @app.route("/warehouse")
# def warehouse():
#     warehouse = dm.get_warehouse()
#     return render_template("/templates/warehouse.html", list = warehouse)

# @app.route("/employee")
# def Employee():
#     Employee = dm.get_Employee()
#     return render_template("/templates/employee.html", list = Employee)

# @app.route("/vendor")
# def vendor():
#     vendor = dm.get_vendor()
#     return render_template("/templates/vendor.html", list = vendor)
# @app.route("/Query1")
# def Query1():
#     Query1 = dm.get_Query1()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query2")
# def Query2():
#     Query2 = dm.get_Query2()
#     return render_template("/templates/vendor.html", list=Query2)
# @app.route("/Query3")
# def Query3():
#     Query1 = dm.get_Query3()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query4")
# def Query4():
#     Query1 = dm.get_Query4()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query5")
# def Query5():
#     Query1 = dm.get_Query5()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query6")
# def Query6():
#     Query1 = dm.get_Query6()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query7")
# def Query7():
#     Query1 = dm.get_Query7()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query8")
# def Query8():
#     Query1 = dm.get_Query8()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query9")
# def Query9():
#     Query1 = dm.get_Query9()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query10")
# def Query10():
#     Query1 = dm.get_Query10()
#     return render_template("/templates/vendor.html", list=Query1)

# ##OLAP queries coming up..

# @app.route("/Query11")
# def Query11():
#     Query1 = dm.get_Query11()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query12")
# def Query12():
#     Query1 = dm.get_Query12()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query13")
# def Query13():
#     Query1 = dm.get_Query13()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query14")
# def Query14():
#     Query1 = dm.get_Query14()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query15")
# def Query15():
#     Query1 = dm.get_Query15()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query16")
# def Query16():
#     Query1 = dm.get_Query16()
#     return render_template("/templates/vendor.html", list=Query1)
# @app.route("/Query17")
# def Query17():
#     Query1 = dm.get_Query17()
#     return render_template("/templates/vendor.html", list=Query1)

if __name__ == "__main__":
    app.run(debug=True)

