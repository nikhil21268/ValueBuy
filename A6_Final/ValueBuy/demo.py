import mysql.connector
mydb  = mysql.connector.connect(host = "localhost",user = "root" , passwd = "MySQL2023",database = "final_final")

mycur = mydb.cursor()
































def upgrade_membership_check():
        
                mycur.execute("""select * from contains_table where cart_id=301 and p_id=593
                                """)
                data=mycur.fetchall()
                if data is not None:
                        mycur.execute("select c_id from current_customer")
                        data=mycur.fetchall()
                        c_id=data[0][0]
                        mycur.execute("update customer set cust_type=%s where c_id=%s",('imperia',c_id))
                        mydb.commit()
                        return
                
                mycur.execute("""select * from contains_table where cart_id=301 and p_id=594
                                """)
                data=mycur.fetchall()
                if data is not None:
                        mycur.execute("select c_id from current_customer")
                        data=mycur.fetchall()
                        c_id=data[0][0]
                        mycur.execute("update customer set cust_type=%s where c_id=%s",('premium',c_id))
                        mydb.commit()
                        return


def upgrade_membership(username,password,membership_type):
        if(membership_type=="imperia"):
               
                mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                                VALUES (1, 301,593);
                                """)
                mycur.execute("""update cart
                set amount = amount + (select price from product where p_id=593)
                where cart_id = 301;
                                        """)
                mydb.commit()
                print("done1")

        else:
                mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                                VALUES (1, 301,594);
                                """)
                mycur.execute("""update cart
                set amount = amount + (select price from product where p_id=594)
                where cart_id = 301;
                                        """)
                mydb.commit()
                print("done2")

class Product:
    def __init__(self, p_id, date_of_mfg, prod_name, price, qty, net_weight, manufacturing_company, prod_type):
        self.p_id = p_id
        self.date_of_mfg = date_of_mfg
        self.prod_name = prod_name
        self.price = price
        self.qty = qty
        self.net_weight = net_weight
        self.manufacturing_company = manufacturing_company
        self.prod_type = prod_type

class Customer:
    def __init__(self, c_id, cust_first_name, cust_last_name, cust_dob, cust_street, cust_city, cust_state, cust_pin, cust_age, cust_title, cust_type, username, password):
        self.c_id = c_id
        self.cust_first_name = cust_first_name
        self.cust_last_name = cust_last_name
        self.cust_dob = cust_dob
        self.cust_street = cust_street
        self.cust_city = cust_city
        self.cust_state = cust_state
        self.cust_pin = cust_pin
        self.cust_age = cust_age
        self.cust_title = cust_title
        self.cust_type = cust_type
        self.username = username
        self.password = password

def check_login_admin(username,password):
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    # Execute the query with the provided username and password
    mycur.execute(query, (username, password))
    # Fetch the result of the query
    result = mycur.fetchone()
    # If the result is not None, the username and password match
    if result is not None:
        return True
    else:
        return False
       
       

def update_employee_increment(e_id, inc):
       mycur.execute("update employee set increment=%s where e_id=%s", (inc,e_id))
       mydb.commit()

class Employee:
    def __init__(self, e_id, emp_name, base_salary, emp_street, emp_state, emp_city, emp_pin, emp_role, emp_type, increment, emp_dob, emp_age):
        self.e_id = e_id
        self.emp_name = emp_name
        self.base_salary = base_salary
        self.emp_street = emp_street
        self.emp_state = emp_state
        self.emp_city = emp_city
        self.emp_pin = emp_pin
        self.emp_role = emp_role
        self.emp_type = emp_type
        self.increment = increment
        self.emp_dob = emp_dob
        self.emp_age = emp_age


def get_prod_class():
        mycur.execute("SELECT * FROM product")

        # Create a list of Product objects for each row in the product table
        products = []
        for row in mycur.fetchall():
                p = Product(*row)
                products.append(p)

        return products

def get_employees():
    mycur.execute("SELECT * FROM employee")
    
    employees = []
    for row in mycur.fetchall():
        e = Employee(*row)
        employees.append(e)
        
    return employees

def get_customers():
    mycur.execute("SELECT * FROM customer")
    
    customers = []
    for row in mycur.fetchall():
        c = Customer(*row)
        customers.append(c)
        
    return customers



def index2_1():
    #mycur.fetchall()
    mycur.execute("select p_id from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    
    print(data[0][0])

    list_pid=[]
    for i in range(len(data)):
        list_pid.append(data[i][0])

    return list_pid

def index2_2():
    mycur.execute("select prod_name from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_prod_name=[]
    for i in range(len(data)):
        list_prod_name.append(data[i][0])

    return list_prod_name
def index2_3():
        
    mycur.execute("select price from product where p_id not in ('1','2','3','4','5','6','7','8');")
    data = mycur.fetchall()

    list_price=[]
    for i in range(len(data)):
        list_price.append(data[i][0])

    return list_price
        
def empty_cart():
       mycur.execute("""delete from cart where cart_id=301;
                        """)
       mycur.execute("""delete from contains_table where cart_id=301;
                        """)
       mydb.commit()
def index2_4():
       
    mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
    data=mycur.fetchall()

    num=0



    for i in data:
        num+=1

    return num

def cart():
       
    mycur.execute("""select amount from cart where cart_id=301;
                        """)
    
    data_m=mycur.fetchall()

    print(data_m)
#     if data_m != []:
#         sum=data_m[0][0]
    sum=data_m[0][0]

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

    mycur.execute("""select cust_type from current_customer;
                        """)
    
    data3=mycur.fetchall()
    print(data3)

    cust_type=data3[0][0]

    if(cust_type=="imperia"):
           discount=25
    elif(cust_type=='premium'):
           discount=15
    else:
           discount=5
    print(list1)
    print(list_names)
    print(list_price)

    list_of_lists=[]
    list_of_lists.append(list1)
#     if data_m != []:
#         list_of_lists.append(sum)
#     else:
#            list_of_lists.append(sum)

    list_of_lists.append(sum)
    
    list_of_lists.append(num)
    list_of_lists.append(list_names)
    list_of_lists.append(list_price)
    list_of_lists.append(discount)

    return list_of_lists
        

def delete_product(product_id):

    mycur.execute('DELETE FROM product WHERE p_id = %s', (product_id,))
    mydb.commit()
    
def add_product(prod_name,price,date_of_mfg,qty,net_weight,manufacturing_company,prod_type):
        # Get the data from the form
        # new_p_id = mycur.execute("SELECT MAX(p_id) + 1 FROM product").fetchone()[0]
        mycur.execute("SELECT MAX(p_id) + 1 FROM product")
        data=mycur.fetchone()
        new_p_id=data[0]
        add_user_query = ("INSERT INTO product (p_id, date_of_mfg,prod_name,price,qty,net_weight,manufacturing_company,prod_type) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)")
        mycur.execute(add_user_query, (new_p_id, date_of_mfg,prod_name,price,qty,net_weight,manufacturing_company,prod_type))
        mydb.commit()
    # Insert the new product into the database
    
        # mycur.execute('INSERT INTO products (p_id,date_of_mfg,prod_name,price,qty,net_weight,manufacturing_company,prod_type) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)',
        #                 (prod_name,price,date_of_mfg,qty,net_weight,manufacturing_company,prod_type))
        # mydb.commit()



def delete_employee(employee_id):
    mycur.execute('DELETE FROM employee WHERE e_id = %s', (employee_id,))
    mydb.commit()

def add_employee(emp_name,emp_dob,emp_street,emp_city,emp_state,emp_pin,emp_role,emp_type,base_salary):
    mycur.execute("SELECT MAX(e_id) + 1 FROM employee")
    data=mycur.fetchone()
    new_emp_id=data[0]
    add_user_query = ("INSERT INTO employee (e_id,emp_name,emp_dob,emp_street,emp_city,emp_state,emp_pin,emp_role,emp_type,base_salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    mycur.execute(add_user_query, (new_emp_id, emp_name,emp_dob,emp_street,emp_city,emp_state,emp_pin,emp_role,emp_type,base_salary))
    mydb.commit()

def delete_customer(customer_id):
    mycur.execute('DELETE FROM customer WHERE c_id = %s', (customer_id,))
    mydb.commit()

# def add_customer(cust_name, cust_address, cust_email, cust_phone):
#     mycur.execute("SELECT MAX(c_id) + 1 FROM customer")
#     data=mycur.fetchone()
#     new_cust_id=data[0]
#     add_user_query = ("INSERT INTO customer (cust_id, cust_name, cust_address, cust_email, cust_phone) VALUES (%s, %s, %s, %s, %s)")
#     mycur.execute(add_user_query, (new_cust_id, cust_name, cust_address, cust_email, cust_phone))
#     mydb.commit()


def add_to_cart_p1():

        
        
        mycur.execute("""INSERT  INTO cart (cart_id, amount) VALUES (301, 0);""")
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,1);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=1)
        where cart_id = 301;
                                """)
        mydb.commit()
        


def add_to_cart_p2():
        
      
        

        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,2);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=2)
        where cart_id = 301;
                                """)
        mydb.commit()
        

def add_to_cart_p3():
        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,3);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=3)
        where cart_id = 301;
                                """)
        mydb.commit()
       

def add_to_cart_p4():
        
    
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1,301,4);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=4)
        where cart_id = 301;
                                """)
        mydb.commit()
       

def add_to_cart_p5():
        
        

        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,5);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=5)
        where cart_id = 301;
                                """)
        mydb.commit()
        

def add_to_cart_p6():
        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,6);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=6)
        where cart_id = 301;
                                """)
        mydb.commit()
        

def add_to_cart_p7():
        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,7);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=7)
        where cart_id = 301;
                                """)
        mydb.commit()
        

def add_to_cart_p8():
        
    
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,8);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=8)
        where cart_id = 301;
                                """)
        mydb.commit()
        

def add_to_cart_p9():
        
        
        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,9);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=9)
        where cart_id = 301;
                                """)
        mydb.commit()
        
def add_to_cart_p10():
        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,10);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=10)
        where cart_id = 301;
                                """)
        mydb.commit()
        

def add_to_cart_p11():
        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,11);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=11)
        where cart_id = 301;
                                """)
        mydb.commit()
      

def add_to_cart_p12():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,12);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p13():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,13);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=13)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p14():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,14);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=14)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p15():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,15);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=15)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p16():
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,16);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=16)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p17():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,17);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=17)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p18():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,18);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=18)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p19():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,19);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=19)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p20():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,20);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=20)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p21():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,21);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=21)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p22():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,22);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=22)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p23():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,23);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=23)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p24():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,24);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=24)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p25():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,25);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=25)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p26():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,26);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=26)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p27():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,27);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=27)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p28():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,28);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=28)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p29():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,29);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=29)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p30():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,30);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=30)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p31():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,31);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=31)
        where cart_id = 301;
                                """)
        mydb.commit() 



#categories



def clothing1():
       
        mycur.execute("""select p_id from product where prod_type='clothing';
                        """)
        data = mycur.fetchall()
        list_pid=[]
        for i in range(len(data)):
                list_pid.append(data[i][0])
        return list_pid

def clothing2():
       
        mycur.execute("select prod_name from product where prod_type='clothing';")
        data = mycur.fetchall()
        list_prod_name=[]
        for i in range(len(data)):
                list_prod_name.append(data[i][0])        
        return list_prod_name

def clothing3():
       
        mycur.execute("select price from product where prod_type='clothing';")
        data = mycur.fetchall()

        list_price=[]
        for i in range(len(data)):
                list_price.append(data[i][0])

        return list_price
        
def clothing4():
       
        mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
        data=mycur.fetchall()

        num=0



        for i in data:
                num+=1
        return num

def electronics1():
       
        mycur.execute("""select p_id from product where prod_type='electronics';
                        """)
        data = mycur.fetchall()
        list_pid=[]
        for i in range(len(data)):
                list_pid.append(data[i][0])
        return list_pid

def electronics2():
       
        mycur.execute("select prod_name from product where prod_type='electronics';")
        data = mycur.fetchall()
        list_prod_name=[]
        for i in range(len(data)):
                list_prod_name.append(data[i][0])        
        return list_prod_name

def electronics3():
       
        mycur.execute("select price from product where prod_type='electronics';")
        data = mycur.fetchall()

        list_price=[]
        for i in range(len(data)):
                list_price.append(data[i][0])

        return list_price
        
def electronics4():
       
        mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
        data=mycur.fetchall()

        num=0



        for i in data:
                num+=1
        return num

def consumables1():
       
        mycur.execute("""select p_id from product where prod_type='consumables';
                        """)
        data = mycur.fetchall()
        list_pid=[]
        for i in range(len(data)):
                list_pid.append(data[i][0])
        return list_pid

def consumables2():
       
        mycur.execute("select prod_name from product where prod_type='consumables';")
        data = mycur.fetchall()
        list_prod_name=[]
        for i in range(len(data)):
                list_prod_name.append(data[i][0])        
        return list_prod_name

def consumables3():
       
        mycur.execute("select price from product where prod_type='consumables';")
        data = mycur.fetchall()

        list_price=[]
        for i in range(len(data)):
                list_price.append(data[i][0])

        return list_price
        
def consumables4():
       
        mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
        data=mycur.fetchall()

        num=0



        for i in data:
                num+=1
        return num

def cosmetics1():
       
        mycur.execute("""select p_id from product where prod_type='cosmetics';
                        """)
        data = mycur.fetchall()
        list_pid=[]
        for i in range(len(data)):
                list_pid.append(data[i][0])
        return list_pid

def cosmetics2():
       
        mycur.execute("select prod_name from product where prod_type='cosmetics';")
        data = mycur.fetchall()
        list_prod_name=[]
        for i in range(len(data)):
                list_prod_name.append(data[i][0])        
        return list_prod_name

def cosmetics3():
       
        mycur.execute("select price from product where prod_type='cosmetics';")
        data = mycur.fetchall()

        list_price=[]
        for i in range(len(data)):
                list_price.append(data[i][0])

        return list_price
        
def cosmetics4():
       
        mycur.execute("""select p_id from contains_table where cart_id=301;
                        """)
    
        data=mycur.fetchall()

        num=0



        for i in data:
                num+=1
        return num

def check_login(username, password):

    # Construct the query to check if the username and password match
    query = "SELECT * FROM customer WHERE username = %s AND password = %s"
    # Execute the query with the provided username and password
    mycur.execute(query, (username, password))
    # Fetch the result of the query
    result = mycur.fetchone()
    # If the result is not None, the username and password match
    if result is not None:
        mycur.execute("""INSERT INTO current_customer
                        SELECT * FROM customer
                        WHERE username = %s AND password = %s;
                        """, (username,password))
        
        mydb.commit()
    
        data=mycur.fetchall()


        return True
    else:
        return False


def signup(username,password,cust_first_name,cust_last_name,cust_dob,cust_street,cust_city,cust_state,cust_pin,cust_title):
         
        # add_user_query = ("INSERT INTO customer (username,password,cust_first_name,cust_last_name,cust_dob,cust_street,cust_city,cust_state,cust_pin,cust_title) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)")
        # user_data = (username, password,cust_first_name,cust_last_name,cust_dob,cust_street,cust_city,cust_state,cust_pin,cust_title)
        # mycur.execute(add_user_query, user_data)
        # mydb.commit()

        #new_c_id = mycur.execute("SELECT MAX(c_id) + 1 FROM customer").fetchone()[0]
        mycur.execute("SELECT MAX(c_id) + 1 FROM customer")
        data=mycur.fetchall()
        new_c_id=data[0][0]
        print(new_c_id)
        add_user_query = ("INSERT INTO customer (c_id, username, password, cust_first_name, cust_last_name, cust_dob, cust_street, cust_city, cust_state, cust_pin, cust_title) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        mycur.execute(add_user_query, (new_c_id, username, password, cust_first_name, cust_last_name, cust_dob, cust_street, cust_city, cust_state, cust_pin, cust_title))
        mydb.commit()





