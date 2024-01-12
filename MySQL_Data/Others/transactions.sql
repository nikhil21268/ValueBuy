select  base_salary FROM employee WHERE e_id = 25;
START TRANSACTION;
UPDATE employee SET base_salary = base_salary + 100 WHERE e_id = 25;
COMMIT;


START TRANSACTION;
UPDATE employee SET base_salary = base_salary + 200 WHERE e_id = 25;
COMMIT;

Grant UPDATE ON employee TO MANAGER;

Grant SELECT ON Product To customer;

Grant SELECT ON Product To Employee;
Grant SELECT ON Order_table To Employee;
Grant SELECT ON Cart To Employee;
Grant SELECT ON Delivers To Employee;
Grant SELECT ON review To Employee;

-- Revoke UPDATE ON MANAGER TO MANAGER

Show grants for Manager;

Show grants for customer;

Grant UPDATE ON CART TO customer;


Create view Electronics AS SELECT E.p_id, Voltage, Warranty, Date_of_mfg,
Prod_name, Price, Prod_type, Qty, Net_weight,Manufacturing_company from
Electronics E,Product P where E.p_id = P.p_id;

Create view consumables AS SELECT P.p_id, Date_of_mfg, Prod_name, Price,
Prod_type, Qty, Net_weight,Manufacturing_company,Date_of_expiry, Ingredients from consumables E,Product P where E.p_id =
P.p_id;

Create view Cosmetics AS SELECT P.p_id, Date_of_mfg, Prod_name,
Price, Prod_type, Qty, Net_weight,Manufacturing_company,Date_of_expiry, Composition, Directions_of_use from Cosmetics E,Product P where
E.p_id = P.p_id;

Create view Clothing AS SELECT P.p_id, Date_of_mfg, Prod_name,
Price, Prod_type, Qty, Net_weight,Manufacturing_company,Category, Size, Type
from Clothing E,Product P where E.p_id = P.p_id;


