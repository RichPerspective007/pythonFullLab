'''
B) Read a text file which contain monthly electricity bills of different customers. Print the electricity consumption for July and November month.

'''

from calendar import month_name
from random import *


#Creating a random file having random Customers bills 
billFile = open('Cust_Elec_Bills.txt','a')

#list of customers
customers = ['One','Two','Three','Four','Five']

#per unit cost of electricity
per_unit = 25

#writing to the file
billFile.write(f'Per Unit Cost = {per_unit}\n\n')
for i in customers:
    billFile.write(f'Name of the Customer: {i}\n- Monthly Bills:\n')
    for j in range(1,13,1):
        units = randint(100,500)
        billFile.write(f'\t-  {month_name[j]}:\n\t  \t- Units Consumed = {units}\n\t  \t- Bill = {units*per_unit}\n')
    billFile.write('\n\n')

billFile.close()


units_july, bills_july, units_sept, bills_sept = 0,0,0,0

#opening the file in read mode and then doing required calculations
with open('Cust_Elec_Bills.txt','r') as bills:
    for line in bills:
        bill = ''
        unit = ''
        if 'July' in line:

            unitline = bills.readline()
            billline = bills.readline()

            for i in unitline:
                if i.isdigit():
                    unit+=i
            
            for i in billline:
                if i.isdigit():
                    bill+=i
            
            units_july+= int(unit)
            bills_july+= int(bill)
        
        if 'September' in line:
            
            unitline = bills.readline()
            billline = bills.readline()

            
            for i in unitline:
                if i.isdigit():
                    unit+=i
            
            for i in billline:
                if i.isdigit():
                    bill+=i
            
            units_sept+= int(unit)
            bills_sept+= int(bill)


print(f'Electricity Consumption:\n\t- July\n\t    - Total Units Consumed = {units_july}\n\t    - Total Bill Revenue = {bills_july}\n\t- September\n\t    - Total Units Consumed = {units_sept}\n\t    - Total Bill Revenue = {bills_sept}')
        
            
