import mysql.connector
mydb  = mysql.connector.connect(host = "localhost",user = "root" , passwd = "MySQL2023",database = "final_final")

mycur = mydb.cursor()



































def get_all_products():
        mycur.execute("select * from product")
        result = mycur.fetchall()
        print(result)
        for row in result:
                print(row)
        list2=[('p_id', 'date_of_mfg', 'prod_name',  'price', 'qty', 'net_weight', 'manufacturing_company', 'prod_type')]
        for row in result:
                list2.append(row)
        return list2

def get_tables():
        mycur.execute("show tables")
        result = mycur.fetchall()
        print(result)
        return result
        














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
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p14():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,14);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p15():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,15);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p16():
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,16);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p17():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,17);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p18():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,18);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p19():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,19);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p20():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,20);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p21():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,21);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p22():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,22);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p23():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,23);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p24():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,24);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p25():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,25);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p26():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,26);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p27():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,27);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p28():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,28);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p29():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,29);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p30():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,30);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
        where cart_id = 301;
                                """)
        mydb.commit() 

def add_to_cart_p31():
       
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,31);
                        """)
        mycur.execute("""update cart
        set amount = amount + (select price from product where p_id=12)
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
        return True
    else:
        return False


def signup(username,password):

        add_user_query = ("INSERT INTO users (username, password) VALUES (%s, %s)")
        user_data = (username, password)
        mycur.execute(add_user_query, user_data)
        mydb.commit()



# def common():

#     ci = dm.add_to_cart_p21()
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

#     mycur.execute("""select p_id from contains_table where cart_id=301;
#                         """)
    
#     data=mycur.fetchall()

#     num=0



#     for i in data:
#         num+=1











# def get_cloths():
#         mycur.execute("select * from clothing")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('p_id', 'category', 'size', 'type_of_clothing')]
#         for row in result:
#                 list2.append(row)
#         return list2
# def get_cosmetics():
#         mycur.execute("select * from cosmetics")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('p_id', 'date_of_expiry', 'composition', 'directions_of_use')]
#         for row in result:
#                 list2.append(row)
#         return list2
# def get_consumables():
#         mycur.execute("select * from consumables")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('p_id', 'date_of_expiry', 'ingredients')]
#         for row in result:
#                 list2.append(row)
#         return list2
# def get_electronics():
#         mycur.execute("select * from electronics")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('p_id', 'voltage', 'warranty')]
#         for row in result:
#                 list2.append(row)
#         return list2
# def get_Customers():
#         mycur.execute("select * from customer")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('c_id', 'cust_first_name',  'cust_last_name',  'cust_dob', 'cust_street', 'cust_city',  'cust_state', 'cust_pin', 'cust_age','cust_title', 'cust_type')]
#         for row in result:
#                 list2.append(row)
#         return list2
# def get_warehouse():
#         mycur.execute("select * from warehouse")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('w_id', 'ware_street', 'ware_city', 'ware_state','ware_pin',  'ware_name')]
#         for row in result:
#                 list2.append(row)
#         return list2
# def get_Employee():
#         mycur.execute("select * from employee")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('e_id','emp_name', 'base_salary','emp_street', 'emp_state', 'emp_city', 'emp_pin', 'emp_role',  'emp_type',  'increment', 'emp_dob', 'emp_age ')]
#         for row in result:
#                 list2.append(row)
#         return list2
# def get_vendor():
#         mycur.execute("select * from vendor")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('vendor_name', 'v_id', 'vendor_city')]
#         for row in result:
#                 list2.append(row)
#         return list2


# def get_Query1():
#         mycur.execute("Select Count(*),cust_type from customer group by cust_type order by count(*) desc")
#         result = mycur.fetchall()
#         print(type(result[0]))
#         for row in result:
#                 print(row)
#         list2=[('count(*)','cust_type')]
#         for row in result:
#                 list2.append(row)
        
#         return list2




# def get_Query2():
#         mycur.execute("Select Count(*) from contains_table where qty > 5")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('count(*)',)]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query3():
#         mycur.execute("Select C.c_id from Customer C,order_table O,cart Ca,contains_table Co,product P where C.c_id = O.c_id and O.Cart_ID = Ca.Cart_ID and Ca.Cart_ID = Co.Cart_ID and Co.p_id = P.p_id and P.prod_name = 'broccoli' And C.c_id in (Select c_id from Customer where c.cust_type = 'premium')")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('c_id',)]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query4():
#         mycur.execute("Select Ca.Cart_ID from Cart as Ca,contains_table as Co where Ca.Cart_ID = Co.Cart_ID and exists(select * from Product P where P.p_id = Co.p_id and P.prod_type = 'Clothing') and exists (select * from Product P where P.p_id = Co.p_id and P.prod_type = 'consumables');")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('cart_id',)]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query5():
#         mycur.execute("Select Min(Date_Of_Appointment),emp_role from Works_for Natural Join Employee group by Emp_Role;")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('Min(Date_Of_Appointment)','emp_role')]
#         for row in result:
#                 list2.append(row)
        
#         return list2

# def get_Query6():
#         mycur.execute("Select E.e_id,E.emp_name,E.emp_type from Employee E ,Increment I where E.e_id = I.e_id and exists (Select e_id from Increment I1 where I.e_id = E.e_id and I.amount != I1.amount);")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('E.e_id','E.emp_name','E.emp_type')]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query7():
#         mycur.execute("Select Avg(Amount) from Cart Natural Join order_table where order_table.discount= 10")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('Avg(Amount)',)]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query8():
#         mycur.execute("Select Avg(Amount) from Cart Natural Join order_table group by order_table.Discount having Discount =25;")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('Avg(Amount)',)]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query9():
#         mycur.execute("Select * from Delivers where tracking_status = 'delivered';")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('e_id','order_id','tracking_status','w_id')]
#         for row in result:
#                 list2.append(row)
        
#         return list2


# #OLAP queries..

# def get_Query11():
#         mycur.execute("SELECT cust_state, cust_city, cust_street, avg(cust_age) AS age_range FROM customer GROUP BY cust_state, cust_city, cust_street WITH ROLLUP;")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('cust_state', 'cust_city', 'cust_street', 'avg(cust_age)')]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query12():
#         mycur.execute("SELECT emp_state, emp_city, emp_street, avg(emp_age) AS age_range_emp FROM employee GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('emp_state', 'emp_city', 'emp_street', 'avg(emp_age)')]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query13():
#         mycur.execute("SELECT emp_state, emp_city, emp_street, avg(base_salary) AS salary_range_emp FROM employee GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('emp_state', 'emp_city', 'emp_street', 'avg(base_salary)')]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query14():
#         mycur.execute("SELECT emp_state, emp_city, emp_street, sum(base_salary) AS sum_salaries FROM employee GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('emp_state', 'emp_city', 'emp_street', 'sum(base_salary)')]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query15():
#         mycur.execute("""SELECT
#          IF(GROUPING(emp_state), 'All states', emp_state) AS emp_state,
#          IF(GROUPING(emp_city), 'All cities', emp_city) AS emp_city,
#          IF(GROUPING(emp_street), 'All streets', emp_street) AS emp_street,
#          SUM(base_salary) AS sum_salaries
#        FROM employee
#        GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;""")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('emp_state', 'emp_city', 'emp_street', 'sum(base_salary)')]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query16():
#         mycur.execute("""SELECT
#          IF(GROUPING(emp_state), 'All states', emp_state) AS emp_state,
#          IF(GROUPING(emp_city), 'All cities', emp_city) AS emp_city,
#          IF(GROUPING(emp_street), 'All streets', emp_street) AS emp_street,
#          avg(base_salary) AS salary_range_emp
#        FROM employee
#        GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;""")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('emp_state', 'emp_city', 'emp_street', 'avg(base_salary)')]
#         for row in result:
#                 list2.append(row)
        
#         return list2
# def get_Query17():
#         mycur.execute("""SELECT
#          IF(GROUPING(cust_state), 'All states', cust_state) AS cust_state,
#          IF(GROUPING(cust_city), 'All cities', cust_city) AS cust_city,
#          IF(GROUPING(cust_street), 'All streets', cust_street) AS cust_street,
#          avg(cust_age) AS age_range_cust
#        FROM customer
#        GROUP BY cust_state, cust_city, cust_street WITH ROLLUP;""")
#         result = mycur.fetchall()
#         print(result)
#         for row in result:
#                 print(row)
#         list2=[('cust_state', 'cust_city', 'cust_street', 'avg(cust_age)')]
#         for row in result:
#                 list2.append(row)
        
#         return list2


