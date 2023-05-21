import mysql.connector
mydb  = mysql.connector.connect(host = "localhost",user = "root" , passwd = "MySQL2023",database = "final_final")

mycur = mydb.cursor()



































def get_all_products():
        mycur.execute("select * from product")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('p_id', 'date_of_mfg', 'prod_name',  'price', 'qty', 'net_weight', 'manufacturing_company', 'prod_type')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2

def get_tables():
        mycur.execute("show tables")
        result = mycur.fetchall()
        print(result)
        return result
        """for row in result:
                print(row)
        list2=[('emp_state', 'emp_city', 'emp_street', 'sum(base_salary)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)"""
        
#add for index2 + index3..



def get_index2():
        '''mycur.execute("show tables")
        result = mycur.fetchall()
        print(result)
        return result'''
        """for row in result:
                print(row)
        list2=[('emp_state', 'emp_city', 'emp_street', 'sum(base_salary)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)"""
        
def get_index3():
        '''mycur.execute("show tables")
        result = mycur.fetchall()
        print(result)
        return result'''
        """for row in result:
                print(row)
        list2=[('emp_state', 'emp_city', 'emp_street', 'sum(base_salary)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)"""
        

# essential front-end + changes being reflected in back-end
#to be corrected..                   

'''def add_to_cart_p1():
        mycur.execute("select * from clothing")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2'''










# cart_id = 301
# amount = 23771


# query = "INSERT INTO cart (cart_id, amount) VALUES (%s, %s)"
# values = (cart_id, amount)

# mycur.execute(query, values)


def update_cart_table():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        # SELECT 301, 41893
        # WHERE NOT EXISTS (
        # SELECT * FROM cart WHERE cart_id = 301);""")

        mycur.execute("""DELETE FROM cart
                 WHERE cart_id = 301;""")
        mydb.commit()



def add_to_cart_p1():

        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 3432);
        #                 """)
        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,1);
                        """)
        mydb.commit()
        #session['cart'] = {'p1': 1}
        
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2


def add_to_cart_p2():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        # SELECT 301, 41893
        # WHERE NOT EXISTS (
        # SELECT * FROM cart WHERE cart_id = 301);""")
        

        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,2);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p3():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 12708);
        #                 """)
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,3);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p4():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 40872);
        #                 """)
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1,301,4);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p5():
        
        # mycur.execute("""
        #                 INSERT INTO cart (cart_id, amount)
        #                 SELECT 301, 23771
        #                 WHERE NOT EXISTS (SELECT * FROM cart WHERE cart_id = 301)
        #                 """)

        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,5);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p6():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 8189);
        #                 """)
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,6);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p7():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 30031);
        #                 """)
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,7);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p8():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 40565);
        #                 """)
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,8);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p9():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 47044);
        #                 """)
        
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,9);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2
def add_to_cart_p10():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 5959);
        #                 """)
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,10);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p11():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 9231);
        #                 """)
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,11);
                        """)
        mydb.commit()
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2

def add_to_cart_p12():
        
        # mycur.execute("""INSERT INTO cart (cart_id, amount)
        #                 VALUES (301, 26333);
        #                 """)
        mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,12);
                        """)
        mydb.commit() 
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        # mycur.execute("""INSERT INTO contains_table (qty, cart_id,p_id)
        #                 VALUES (1, 301,1);
        #                 """)
        
        # mycur.execute("select * from clothing")
        # result = mycur.fetchall()
        # print(result)
        # #return result
        # for row in result:
        #         print(row)
        # list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # # list2.insert('count(*)')
        # for row in result:
        #         list2.append(row)
        # return list2















def get_cloths():
        mycur.execute("select * from clothing")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('p_id', 'category', 'size', 'type_of_clothing')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2
def get_cosmetics():
        mycur.execute("select * from cosmetics")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('p_id', 'date_of_expiry', 'composition', 'directions_of_use')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2
def get_consumables():
        mycur.execute("select * from consumables")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('p_id', 'date_of_expiry', 'ingredients')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2
def get_electronics():
        mycur.execute("select * from electronics")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('p_id', 'voltage', 'warranty')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2
def get_Customers():
        mycur.execute("select * from customer")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('c_id', 'cust_first_name',  'cust_last_name',  'cust_dob', 'cust_street', 'cust_city',  'cust_state', 'cust_pin', 'cust_age','cust_title', 'cust_type')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2
def get_warehouse():
        mycur.execute("select * from warehouse")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('w_id', 'ware_street', 'ware_city', 'ware_state','ware_pin',  'ware_name')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2
def get_Employee():
        mycur.execute("select * from employee")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('e_id','emp_name', 'base_salary','emp_street', 'emp_state', 'emp_city', 'emp_pin', 'emp_role',  'emp_type',  'increment', 'emp_dob', 'emp_age ')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2
def get_vendor():
        mycur.execute("select * from vendor")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('vendor_name', 'v_id', 'vendor_city')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        return list2
"""
def get_Query1():
        mycur.execute("Select Count(*),cust_type from customer group by cust_type order by count(*) desc")
        result = mycur.fetchall()
        print(result)
        return result"""

def get_Query1():
        mycur.execute("Select Count(*),cust_type from customer group by cust_type order by count(*) desc")
        result = mycur.fetchall()
        print(type(result[0]))
        for row in result:
                print(row)
        list2=[('count(*)','cust_type')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2

# def get_Query1():
#     mycur.execute("SELECT COUNT(*) AS total_customers, cust_type FROM customer GROUP BY cust_type ORDER BY total_customers DESC")
#     result = mycur.fetchall()
#     if result:
#         # Fetch the column names from the cursor description
#         columns = [col[0] for col in mycur.description]
#         print(columns)
#         # Print the column names and the query result
#         print("\t".join(columns))
#         for row in result:
#             print("\t".join(str(val) for val in row))
#     else:
#         print("No data found.")
#     return result

# def get_Query1():
#     mycur.execute("SELECT COUNT(*) AS total_customers, cust_type FROM customer GROUP BY cust_type ORDER BY total_customers DESC")
#     result = mycur.fetchall()
#     if result:
#         # Fetch the column names from the cursor description
#         columns = [col[0] for col in mycur.description]
#         print(columns)
#         # Print the column names and the query result
#         print("{:<20} {}".format(columns[0], columns[1]))
#         for row in result:
#             print("{:<20} {}".format(row[0], row[1]))
#     else:
#         print("No data found.")
#     return result



def get_Query2():
        mycur.execute("Select Count(*) from contains_table where qty > 5")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('count(*)',)]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query3():
        mycur.execute("Select C.c_id from Customer C,order_table O,cart Ca,contains_table Co,product P where C.c_id = O.c_id and O.Cart_ID = Ca.Cart_ID and Ca.Cart_ID = Co.Cart_ID and Co.p_id = P.p_id and P.prod_name = 'broccoli' And C.c_id in (Select c_id from Customer where c.cust_type = 'premium')")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('c_id',)]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query4():
        mycur.execute("Select Ca.Cart_ID from Cart as Ca,contains_table as Co where Ca.Cart_ID = Co.Cart_ID and exists(select * from Product P where P.p_id = Co.p_id and P.prod_type = 'Clothing') and exists (select * from Product P where P.p_id = Co.p_id and P.prod_type = 'consumables');")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('cart_id',)]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query5():
        mycur.execute("Select Min(Date_Of_Appointment),emp_role from Works_for Natural Join Employee group by Emp_Role;")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('Min(Date_Of_Appointment)','emp_role')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2

#to be corrected here..
def get_Query6():
        mycur.execute("Select E.e_id,E.emp_name,E.emp_type from Employee E ,Increment I where E.e_id = I.e_id and exists (Select e_id from Increment I1 where I.e_id = E.e_id and I.amount != I1.amount);")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('E.e_id','E.emp_name','E.emp_type')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query7():
        mycur.execute("Select Avg(Amount) from Cart Natural Join order_table where order_table.discount= 10")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('Avg(Amount)',)]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query8():
        mycur.execute("Select Avg(Amount) from Cart Natural Join order_table group by order_table.Discount having Discount =25;")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('Avg(Amount)',)]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query9():
        mycur.execute("Select * from Delivers where tracking_status = 'delivered';")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('e_id','order_id','tracking_status','w_id')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2

# was previously an update command - removed for simplicity..
"""def get_Query10():
        mycur.execute("select * from customer")
        result = mycur.fetchall()
        print(result)
        return result"""

#OLAP queries..

def get_Query11():
        mycur.execute("SELECT cust_state, cust_city, cust_street, avg(cust_age) AS age_range FROM customer GROUP BY cust_state, cust_city, cust_street WITH ROLLUP;")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('cust_state', 'cust_city', 'cust_street', 'avg(cust_age)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query12():
        mycur.execute("SELECT emp_state, emp_city, emp_street, avg(emp_age) AS age_range_emp FROM employee GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('emp_state', 'emp_city', 'emp_street', 'avg(emp_age)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query13():
        mycur.execute("SELECT emp_state, emp_city, emp_street, avg(base_salary) AS salary_range_emp FROM employee GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('emp_state', 'emp_city', 'emp_street', 'avg(base_salary)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query14():
        mycur.execute("SELECT emp_state, emp_city, emp_street, sum(base_salary) AS sum_salaries FROM employee GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('emp_state', 'emp_city', 'emp_street', 'sum(base_salary)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query15():
        mycur.execute("""SELECT
         IF(GROUPING(emp_state), 'All states', emp_state) AS emp_state,
         IF(GROUPING(emp_city), 'All cities', emp_city) AS emp_city,
         IF(GROUPING(emp_street), 'All streets', emp_street) AS emp_street,
         SUM(base_salary) AS sum_salaries
       FROM employee
       GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;""")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('emp_state', 'emp_city', 'emp_street', 'sum(base_salary)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query16():
        mycur.execute("""SELECT
         IF(GROUPING(emp_state), 'All states', emp_state) AS emp_state,
         IF(GROUPING(emp_city), 'All cities', emp_city) AS emp_city,
         IF(GROUPING(emp_street), 'All streets', emp_street) AS emp_street,
         avg(base_salary) AS salary_range_emp
       FROM employee
       GROUP BY emp_state, emp_city, emp_street WITH ROLLUP;""")
        result = mycur.fetchall()
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('emp_state', 'emp_city', 'emp_street', 'avg(base_salary)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2
def get_Query17():
        mycur.execute("""SELECT
         IF(GROUPING(cust_state), 'All states', cust_state) AS cust_state,
         IF(GROUPING(cust_city), 'All cities', cust_city) AS cust_city,
         IF(GROUPING(cust_street), 'All streets', cust_street) AS cust_street,
         avg(cust_age) AS age_range_cust
       FROM customer
       GROUP BY cust_state, cust_city, cust_street WITH ROLLUP;""")
        result = mycur.fetchall()
        #result = mycur.description
        print(result)
        #return result
        for row in result:
                print(row)
        list2=[('cust_state', 'cust_city', 'cust_street', 'avg(cust_age)')]
        # list2.insert('count(*)')
        for row in result:
                list2.append(row)
        
        return list2


