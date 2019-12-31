from .database_connection import DatabaseConnection
companies = []



def add_company(name, location, industry, CEO):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
#        cursor.execute("SELECT count(*) FROM companies WHERE UPPER(name) = UPPER(?)", (name,))
        
#          if cursor.fetchall()[0][0] == 1:
#             print("Error. This company already exists!")
#             return
        query = """INSERT INTO companies (name, location, industry, CEO) 
                     VALUES (?,?,?,?)"""
        insert_values = (name, location, industry, CEO)
#         try:
        cursor.execute(query, insert_values)
#         except:
#             pass

def update_company(old_name, name, location, industry, CEO):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
#         cursor.execute('Select id from companies where UPPER(name) = UPPER(?)', (old_name,))
        update_values = (name, location, industry, CEO, old_name.upper())
        update_string = '''UPDATE companies SET name = ?, location = ?, industry = ?, CEO = ? 
                       WHERE UPPER(name) = ?'''
        cursor.execute(update_string, update_values)
#         except:
#             pass

def company_exists(name):
    with DatabaseConnection('data.db') as connection:
        exists = False
        cursor = connection.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM companies where UPPER(name) = UPPER(?)', (name, ))
        exists = cursor.fetchall()[0][0]
    
    return exists
        
def remove_company(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute('DELETE FROM companies where UPPER(name) = ?', (name.upper(),))
            
def list_companies():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute("SELECT * from companies")
        comp_list = cursor.fetchall()
        for comp in comp_list:
            print(comp)

def read_company(new_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM companies WHERE UPPER(name) = ?", (new_name.upper(),))
        comp = cursor.fetchall()[0]
        print(f"id: {comp[0]} name: {comp[1]}, location: {comp[2]}, industry: {comp[3]}, CEO: {comp[4]}")
    
