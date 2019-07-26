# PurachaseAnalytics
This project is designed to perform fast purchase analytics tasks to summarize information about instacart data.
Instacart has published a [dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders.

Problem Statement :
To calculate, for each department, the number of times a product was requested, number of times a product was requested for the first time and a ratio of those two numbers.

File Structure: 

    ├── README.md
    ├── run.sh
    ├── src
    │   └── purchase_analytics.py
    |   |__readfile.py
    |   |__writefile.py
    ├── input
    │   └── products.csv
    |   └── order_products.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
                ├── input
                │   └── products.csv
                │   └── order_products.csv
                |__ output
                |    └── report.csv
                ├── src
                     └── purchase_analytics.py
                     |__readfile.py
                     |__writefile.py
           
 How to run this code:
 This code is written in python with builtin data structures and requires no external libraries.
 To run this code you can use the following command:
 sh run.sh
 
 More about the code:
 purchase_analytics.py : is the main file that executes the required task. It has two helper files that are used to read the product information and write the processed output/
 readp
 
 
           
