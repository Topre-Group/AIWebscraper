""" Import the necessary modules """
import pyodbc

id = 0 

""" Establish connection to microsoft sql server """
conn = conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1P8QTPD;'
                      'Database=CRFTest;'
                      'UID=Sanchit12;'
                      'PWD=GSWarrior02;'
                      'Trusted_Connection=yes;')

cur = conn.cursor()

""" Reading lines from working product urls text file """  
file_lines = []
with open("./working_product_urls/working_product_urls.txt", "r") as fs:
    for line in fs:
        currentLine = line.rstrip().split(',')
        file_lines.append(currentLine)

""" Extracting and storing working product urls """
urls = []
for fl in file_lines:
    urls.append(fl[0])

""" Converting working product urls list to set """
urls = sorted(set(urls), key=urls.index)

""" Loop through all working product urls and store them in the database """
for url in urls:
    id = id + 1
    postgres_insert_query = """SET ANSI_WARNINGS OFF; INSERT INTO ENTITIES (entity_id, brand, model, price, stock, producturl, condition) \
VALUES (?, ?, ?, ?, ?, ?, ?); SET ANSI_WARNINGS ON; """
    record_to_insert = (str(id), '', '', '', '', url, '')
    cur.execute(postgres_insert_query, record_to_insert)
    conn.commit()

""" Close the connection """
conn.close()
