# SWIFTMARKET <center>
![image](https://github.com/Manisha0125/Ecommerce_Analysis/assets/168274273/7838200f-a9c8-45ae-babd-c23971331475)

# Overview
This project aims to analyze e-commerce sales data stored in a MySQL database. Using Jupyter Notebook, we perform SQL queries to extract insights from the data and visualize them using charts and graphs.

# FEATURES 
. Data querying with MYSQL in Jupyter Notebook.

. Data visualization using charts and graphs.

. Insights gained from the analysis.

# TECHNOLOGIES
. MySQL for database management.

. Jupyter Notebook for data analysis and visualization.

. Matplotlib and Seaborn for creating visualizations.

# QUERY EXAMPLES
Example SQL query to find the highest average selling price


query='''select 
	       
	 SubcatName,avg(UnitPrice) as AvgSellingPrice
	 
        from 
	        subcategories
        
	group by 
	        SubcatName
        
	order by
	        AvgSellingPrice desc
        
	limit 10;'''

       

