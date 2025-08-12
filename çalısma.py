import pyodbc
from datetime import datetime, date

# MSSQL bağlantı bilgileri
conn = pyodbc.connect(

    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=BUGRA;"
    "DATABASE=ExpenseTracker;"
    "Trusted_Connection=yes;"
)

def add_expense(category,amount,description):
    cursor = conn.cursor()
    query = """
    INSERT INTO Expenses (Category, Amount, Description, ExpenseDate) VALUES(?, ?, ?, ?)
    """
    cursor.execute(query, (category,amount,description,date.today()))
    conn.commit()
    print("Harcama başarıyla eklendi.")

cat = input("Harcama Kategorisi:")
amt = float(input("Tutar:"))
des = input("Açıklama:")

add_expense(cat,amt,des)

def list_expenses():
    cursor = conn.cursor()
    cursor.execute("SELECT ExpenseID,Category,Amount,Description,ExpenseDate FROM Expenses")
    rows = cursor.fetchall()

    for row in rows:
        print(f"{row.ExpenseID} - {row.Category} - {row.Amount} - {row.Description} - {row.ExpenseDate}")

list_expenses()
