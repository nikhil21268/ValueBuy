import string

with open("generated_code.txt", "w") as f:
    for i in range(32, 593):
        function_name = f"add_to_cart_p{i}"
        function_code = f"""
@app.route("/index2{i}")
def {function_name}():
    ci = dm.{function_name}()
    list_pid = dm.index2_1()
    list_prod_name = dm.index2_2()
    list_price = dm.index2_3()
    num = dm.index2_4()
    return render_template("/for_index2/dist/index.html", list_pid=list_pid, list_prod_name=list_prod_name, list_price=list_price, num=num)
"""
        f.write(function_code)
