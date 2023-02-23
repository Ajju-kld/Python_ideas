--question 1


create table customer(cust_id int primary key, cust_name varchar(30),cust_address varchar(30));


create table account(acc_no int primary key,acc_type ENUM('current', 'saving'),cust_id int, foreign key(cust_id) references customer(cust_id),balance int,start_date date,credit_status ENUM('Active','Disabled') default 'Active');
-- question 2
select acc_no,cust_name from customer natural join account where balance>10000 and cust_address like '%Kannur%';

--question 3
select count(*) from account join customer on account.cust_id=customer.cust_id where balance<25000;

--question 4
select cust_id,count(*) from account join customer on account.cust_id=customer.cust_id group by cust_id;

--question 5
select acc_no,cust_name from account join customer on account.cust_id=customer.cust_id  where start_date=curdate();

--question 6

create view Manager as select cust_name,acc_no,acc_type,balance from account join customer on account.cust_id=customer.cust_id;