import mysql.connector as cont
data=input("enter database you want to use:")
username=input("enter username:")
password=input("enter password")
con =cont.connect(host="localhost",user=username,passwd=password,database=data)
if con.is_connected():
    print("Connection to SQL database is successful!")
else:
    print("Connection failed or has been closed.")
def insertdata():
    c = con.cursor() 
    table_name = input("Enter the table name: ")
    columns = input("Enter column names (comma-separated): ")
    values = input("Enter values (comma-separated): ")  
    sql = f"""
        INSERT INTO {table_name} ({columns})
        VALUES ({values})
        """   
    c.execute(sql)
    con.commit()
    print(f"Data inserted into '{table_name}' successfully")   
def deletedata():
    c = con.cursor()
    table_name = input("Enter the table name: ")
    condition = input("Enter condition (e.g., 'column_name=value'): ")
    sql = f"""
        DELETE FROM {table_name}
        WHERE {condition}
        """
    c.execute(sql)
    con.commit()
    print(f"Data deleted from '{table_name}' successfully")

   
def createtable():

    c = con.cursor()
    table_name = input("Enter the table name: ")
    attributes = input("Enter attributes (comma-separated): ")
    sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {attributes}
    )
    """
    c.execute(sql)
    con.commit()
    print(f"Table '{table_name}' created successfully")


def updatetable():
    c = con.cursor()
    table_name = input("Enter the table name: ")
    attributes = input("Enter attributes and new values (comma-separated, e.g., 'attribute1=new_value1, attribute2=new_value2'): ")
    condition=input("enter condition for selecting attribute:")
    sql = f"""
    UPDATE {table_name}
    SET {attributes}
    WHERE {condition};
    """
    c.execute(sql)
    con.commit()
    print(f"Table '{table_name}' updated successfully")
def deletetable():
    print("aman")
import mysql.connector

def deletetable():
        cursor = con.cursor()
        table_name = input("Enter the name of the table you want to delete: ")
        sql_query = f"DROP TABLE IF EXISTS {table_name};"
        cursor.execute(sql_query)
        con.commit()
        print(f"Table '{table_name}' has been deleted successfully.")


 
#yahan se program nahin chedhna
print("enter 1 for insert data ")
print("enter 2 for deleting data")
print("enter 3 for creating the table")
print("enter 4 for updating data")
print("enter 5 for deleting the table")
choice=int(input("enter your choice to do required operation:"))

if(choice==1):
    insertdata()
    conti=input("enter 1 for reentering the program")
    if(conti==1):
     choice=int(input("enter your choice to do required operation:"))
    else:
        exit   
elif(choice==2):
    deletedata()
    conti=input("enter 1 for reentering the program")
    if(conti==1):
     choice=int(input("enter your choice to do required operation:"))
    else:
        exit 
elif(choice==3):
    createtable()
    conti=input("enter 1 for reentering the program")
    if(conti==1):
     choice=int(input("enter your choice to do required operation:"))
    else:
        exit 
elif(choice==4):
    updatetable()
    conti=input("enter 1 for reentering the program")
    if(conti==1):
     choice=int(input("enter your choice to do required operation:"))
    else:
        exit 
elif(choice==5):
    deletetable()
    conti=input("enter 1 for reentering the program")
    if(conti==1):
     choice=int(input("enter your choice to do required operation:"))
    else:
        exit 


    


   
    