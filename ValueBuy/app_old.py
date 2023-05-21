# import mysql.connector
# mydb  = mysql.connector.connect(host = "localhost",user = "root" , passwd = "MySQL2023",database = "final_final")

# mycur = mydb.cursor()

from flask import Flask, redirect, url_for, render_template, request

import demo as dm

app = Flask(__name__,template_folder="C:/Users/suris/Desktop/DBMS/Project/A6/ValueBuy")#,static_url_path='/C:/Users/suris/Desktop/DBMS/Project/A6/ValueBuy')
app.secret_key = 'trial'

#from flask import session















@app.route("/" , methods= ["POST", "GET"])
def login():
    if request.method =="POST":
        user = request.form["username"]
        passwd = request.form["password"]

        return redirect(url_for("welcome", name = user))
    else:
        return render_template("/templates/loginpage.html")

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

#adding multiple indexes for further dev..

@app.route("/index2")
def index2():
    #ci = dm.get_index2()
    







    # session['price'] = {'p1': 3432}
    # session['price']['p2'] = 41893
    # session['price']['p3'] = 12708
    # session['price']['p4'] = 40872
    # session['price']['p5'] = 23771
    # session['price']['p6'] = 8189
    # session['price']['p7'] = 30031
    # session['price']['p8'] = 40565
    #session['price'] =[3432,41893,12708,40872,23771,8189,30031,40565]
    # mycur.execute("""INSERT INTO cart (cart_id, amount)
    #     SELECT 301, 41893
    #     WHERE NOT EXISTS (
    #     SELECT * FROM cart WHERE cart_id = 301);""")
    # mydb.commit()
    return render_template("/for_index2/dist/index.html")

@app.route("/index3")
def index3():
    
    #ci = dm.get_index3()
    return render_template("/for_index3/dist/index.html")



##added for putting products in cart

@app.route("/index21")
def added_to_cart_p1():
    
    ci = dm.add_to_cart_p1()
    #session['cart'] = {'p1': 1}
    return redirect('/for_index2/dist/index.html')

    #return render_template("/for_index2/dist/index.html")

@app.route("/index22")
def added_to_cart_p2():
    
    ci = dm.add_to_cart_p2()
    #session['cart']['p2'] = 1
    return redirect('/for_index2/dist/index.html')

    #return render_template("/for_index2/dist/index.html")

@app.route("/index23")
def added_to_cart_p3():
    
    ci = dm.add_to_cart_p3()
    #session['cart']['p3'] = 1
    return redirect('/for_index2/dist/index.html')

    #return render_template("/for_index2/dist/index.html")

@app.route("/index24")
def added_to_cart_p4():
    
    ci = dm.add_to_cart_p4()
    #session['cart']['p4'] = 1
    return redirect('/for_index2/dist/index.html')

    #return render_template("/for_index2/dist/index.html")

@app.route("/index25")
def added_to_cart_p5():
    
    ci = dm.add_to_cart_p5()
    #session['cart']['p5'] = 1
    return redirect('/for_index2/dist/index.html')

    #return render_template("/for_index2/dist/index.html")

@app.route("/index26")
def added_to_cart_p6():
    
    ci = dm.add_to_cart_p6()
    #session['cart']['p6'] = 1
    return redirect('/for_index2/dist/index.html')

    #return render_template("/for_index2/dist/index.html")
    return None

@app.route("/index27")
def added_to_cart_p7():
    
    ci = dm.add_to_cart_p7()
    #session['cart']['p7'] = 1
    return redirect('/for_index2/dist/index.html')

    #return render_template("/for_index2/dist/index.html")

@app.route("/index28")
def added_to_cart_p8():
    
    ci = dm.add_to_cart_p8()
    #session['cart']['p8'] = 1
    return redirect('/for_index2/dist/index.html')

    #return render_template("/for_index2/dist/index.html")

@app.route("/cart")
def cart():
    #cart_items = session.get('cart', {})
    #price = session.get('price', {})
    #price = session.get('price', [])
    sum=0
    iter=0
    for key, value in cart_items.items():

        if(value>0):
            sum+=price[iter]
            print("curr sum is=",sum)
            print("\n")
        iter+=1

    #mycur.execute("SET FOREIGN_KEY_CHECKS=0;")

    #dm.update_cart_table()
    
    
    list1=[sum]
    print("sum is=",sum)
    print("\n")
    #query = "INSERT INTO cart (cart_id, amount) VALUES (%s, %s);"# ON DUPLICATE KEY UPDATE cart_id=cart_id, amount=amount"
    query = "UPDATE cart SET amount = %s WHERE cart_id = 301"

    # mycursor.execute("UPDATE cart SET amount = %s WHERE cart_id = %s", (new_amount, 301))
    # mydb.commit()

    """ values = (301, sum)
    mycur.execute(query, values) """

    #mycur.execute("SET FOREIGN_KEY_CHECKS=1;")

    values = (list1)

    mycur.execute(query,values)
    mydb.commit()
    print("so far so good\n")
    # query = "INSERT INTO table_name (column1, column2, column3) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE column1=column1, column2=column2, column3=column3"
    # values = (value1, value2, value3)
    # mycursor.execute(query, values)
    # mydb.commit()


    # query = "INSERT INTO cart (cart_id, amount) VALUES (%s, %s) ON DUPLICATE KEY UPDATE amount=%s"
    # values = (301, sum, sum)
    # mycur.execute(query, values)
    # mydb.commit()

    
    # mycur.execute("""INSERT INTO cart (cart_id, amount)
    #     SELECT 301, {{sum}}
    #     WHERE NOT EXISTS (
    #     SELECT * FROM cart WHERE cart_id = 301);""")
    # Code to retrieve and display cart items goes here
    #send mutliple lists to the template here..
    
    return render_template("/templates/cart.html", cart_items=cart_items, total_price=sum)

#4 others..ss

# @app.route("/index29")
# def added_to_cart_p9():
    
#     ci = dm.add_to_cart_p9()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index210")
# def added_to_cart_p10():
    
#     ci = dm.add_to_cart_p10()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index211")
# def added_to_cart_p11():
    
#     ci = dm.add_to_cart_p11()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index212")
# def added_to_cart_p12():
    
#     ci = dm.add_to_cart_p12()
#     return render_template("/for_index2/dist/index.html")









#added for index3 pages for the first 8 prods..

# @app.route("/index31")
# def added_to_cart_p1():
    
#     ci = dm.add_to_cart_p1()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index32")
# def added_to_cart_p2():
    
#     ci = dm.add_to_cart_p2()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index33")
# def added_to_cart_p3():
    
#     ci = dm.add_to_cart_p3()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index34")
# def added_to_cart_p4():
    
#     ci = dm.add_to_cart_p4()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index35")
# def added_to_cart_p5():
    
#     ci = dm.add_to_cart_p5()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index36")
# def added_to_cart_p6():
    
#     ci = dm.add_to_cart_p6()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index37")
# def added_to_cart_p7():
    
#     ci = dm.add_to_cart_p7()
#     return render_template("/for_index2/dist/index.html")

# @app.route("/index38")
# def added_to_cart_p8():
    
#     ci = dm.add_to_cart_p8()
#     return render_template("/for_index2/dist/index.html")

#4 others..

@app.route("/index39")
def added_to_cart_p9():
    
    ci = dm.add_to_cart_p9()
    return redirect('/for_index3/dist/index.html')

    #return render_template("/for_index3/dist/index.html")

@app.route("/index310")
def added_to_cart_p10():
    
    ci = dm.add_to_cart_p10()
    return redirect('/for_index3/dist/index.html')
    #return render_template("/for_index3/dist/index.html")

@app.route("/index311")
def added_to_cart_p11():
    
    ci = dm.add_to_cart_p11()
    return redirect('/for_index3/dist/index.html')
    #return render_template("/for_index3/dist/index.html")

@app.route("/index312")
def added_to_cart_p12():
    
    ci = dm.add_to_cart_p12()
    return redirect('/for_index3/dist/index.html')
    #return render_template("/for_index3/dist/index.html")






















@app.route("/clothing")
def clothing():
    cloths = dm.get_cloths()
    return render_template("/templates/clothing.html", list = cloths)

@app.route("/products")
def products():
    products = dm.get_all_products()
    return render_template("/templates/clothing.html", list = products)

@app.route("/cosmetics")
def cosmetics():
    cosmetics = dm.get_cosmetics()
    return render_template("/templates/cosmetics.html", list = cosmetics)

@app.route("/electronics")
def electronics():
    electronics = dm.get_electronics()
    return render_template("/templates/electronics.html", list = electronics)

@app.route("/consumables")
def consumables():
    consumables = dm.get_consumables()
    return render_template("/templates/consumables.html", list = consumables)

@app.route("/customer")
def Customers():
    Customers = dm.get_Customers()
    return render_template("/templates/customer.html", list = Customers)

@app.route("/warehouse")
def warehouse():
    warehouse = dm.get_warehouse()
    return render_template("/templates/warehouse.html", list = warehouse)

@app.route("/employee")
def Employee():
    Employee = dm.get_Employee()
    return render_template("/templates/employee.html", list = Employee)

@app.route("/vendor")
def vendor():
    vendor = dm.get_vendor()
    return render_template("/templates/vendor.html", list = vendor)
@app.route("/Query1")
def Query1():
    Query1 = dm.get_Query1()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query2")
def Query2():
    Query2 = dm.get_Query2()
    return render_template("/templates/vendor.html", list=Query2)
@app.route("/Query3")
def Query3():
    Query1 = dm.get_Query3()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query4")
def Query4():
    Query1 = dm.get_Query4()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query5")
def Query5():
    Query1 = dm.get_Query5()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query6")
def Query6():
    Query1 = dm.get_Query6()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query7")
def Query7():
    Query1 = dm.get_Query7()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query8")
def Query8():
    Query1 = dm.get_Query8()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query9")
def Query9():
    Query1 = dm.get_Query9()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query10")
def Query10():
    Query1 = dm.get_Query10()
    return render_template("/templates/vendor.html", list=Query1)

##OLAP queries coming up..

@app.route("/Query11")
def Query11():
    Query1 = dm.get_Query11()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query12")
def Query12():
    Query1 = dm.get_Query12()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query13")
def Query13():
    Query1 = dm.get_Query13()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query14")
def Query14():
    Query1 = dm.get_Query14()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query15")
def Query15():
    Query1 = dm.get_Query15()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query16")
def Query16():
    Query1 = dm.get_Query16()
    return render_template("/templates/vendor.html", list=Query1)
@app.route("/Query17")
def Query17():
    Query1 = dm.get_Query17()
    return render_template("/templates/vendor.html", list=Query1)

if __name__ == "__main__":
    app.run(debug=True)

