INSERT  INTO cart (cart_id, amount) VALUES (301, 0);

INSERT  INTO contains_table (qty, cart_id, p_id) VALUES (1, 301, 1);

update cart
set amount = (select price from product where p_id=1)
where cart_id = 301;

select * from cart where cart_id=301;

select * from contains_table where cart_id=301;

INSERT INTO contains_table (qty, cart_id,p_id)
                        VALUES (1, 301,2);
                        
update cart
set amount = amount + (select price from product where p_id=2)
where cart_id = 301;
                        
show create table contains_table;


select amount from cart where cart_id=301;

select prod_name from product where p_id=1;

select p_id from contains_table where cart_id=301;