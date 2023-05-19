# Show all customer records

select * from sales.customers ;

# Show total number of customers

select count(*) as Total_customers from sales.customers ;

# Show transactions for Chennai market (market code for chennai is Mark001 )

select * from sales.transactions
where market_code = 'Mark001' ;

# Show distinct product codes that were sold in chennai

select distinct(product_code) from sales.transactions
where market_code = 'Mark001' ;

# Show transactions where currency is US dollars

select * from sales.transactions
where currency = 'USD' ;

# Show transactions in 2020 join by date table

select sales.transactions.* from sales.transactions join sales.date
on sales.transactions.order_date = sales.date.date
where year = 2020 ;
#---------- by using Year() function ----------------#
select * from sales.transactions
where year(order_date) = 2020 ;

# Show total revenue in year 2020

select sum(sales.transactions.sales_amount) as total_revenue2020 
from sales.transactions join sales.date
on sales.transactions.order_date = sales.date.date
where year = 2020 ;

#--------------- by using year() ---------------------#
select sum(sales_amount) as total_revenue2020 
from sales.transactions
where year(order_date) =  2020 ;


SELECT SUM(transactions.sales_amount) FROM transactions INNER JOIN date 
ON transactions.order_date=date.date where date.year=2020 
and transactions.currency="INR\r" or transactions.currency="USD\r" ;

# Show total revenue in year 2020, January Month

select sum(sales.transactions.sales_amount) as revenue_jan2020
from sales.transactions join sales.date
on sales.transactions.order_date = sales.date.date
where sales.date.month_name = 'January' 
and sales.date.year = 2020 
and (transactions.currency="INR\r" or transactions.currency="USD\r") ;

# Show total revenue in year 2020 in Chennai

select sum(sales.transactions.sales_amount) as Total_revenue2020_chennai
from sales.transactions join sales.markets
on sales.transactions.market_code = sales.markets.markets_code
where market_code = 'Mark001' ;