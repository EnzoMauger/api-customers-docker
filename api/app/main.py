"""
Par soucis de simplicité et de par la nature du projet, tout le code a été réuni dans ce fichier
"""

from fastapi import FastAPI, Response
import sys
import mysql.connector
from pydantic import BaseModel, Field 

# Setup connection to db
try:
    conn = mysql.connector.connect(user='root', password='root',
                              host='mariadb',
                              database='mydatabase')
except Exception as e:
    print(f"Error connecting to database: {e}")
    sys.exit(1)
cursor = conn.cursor()

async def readonly_execute_sql(sql: str):
    """
    Permet d'exécuter une requête de type SELECT (on retourne le résultat)
    """
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    except Exception as e:
        print(f"Exception during database (readonly) query : {e}")
        return False
    
async def execute_sql(sql: str):
    """
    Permet d'exécuter une requête de type SELECT
    (on retourne True/False selon si la requête s'est correctement exécutée)
    """
    try:
        cursor.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        print(f"Exception during database (modification) query : {e}")
        return False

async def get_next_available_id():
    """
    Retourne le prochain Id disponible
    (si nous ne voulons pas modifier le schéma de la table, cette fonction est nécessaire)
    """
    res = await readonly_execute_sql("""SELECT Auto_increment FROM information_schema.tables
    WHERE table_name='customers';""")

    return res[0][0]

async def handle_modification_query(query: str):
    """
    
    """
    is_state_ok = await execute_sql(query)

    return is_state_ok

class Customer(BaseModel):
    """
    Classe de validation de paramètres pour la ressource Customer
    """
    firstname: str = Field(None, max_length=200)
    name: str = Field(None, max_length=200)
    email: str = Field(None, max_length=200)

app = FastAPI()

### ROUTES ###

@app.get("/customers")
async def get_all_customers():
    """
    Permet de LIRE l'ensemble des customers
    """
    sql_request = """SELECT `id`, `firstname`, `name`, `email`, `created` FROM `customers`;"""

    return await readonly_execute_sql(sql_request)

@app.get("/customers/{id}")
async def get_one_customer(id: int, response: Response):
    """
    Permet de LIRE un customer
    """
    sql_request = f"""SELECT `id`, `firstname`, `name`, `email`, `created` FROM `customers` WHERE `id`={id};"""
    res = await readonly_execute_sql(sql_request)

    if len(res) > 0:
        return res[0]
    response.status_code = 404
    return "Customer not found"

@app.post("/customers")
async def create_customer(customer: Customer):
    """
    Permet de CRÉER un customer
    """
    id = await get_next_available_id()
    sql_request = f"""INSERT INTO `customers` (`id`, `firstname`, `name`, `email`) VALUES
({id}, '{customer.firstname}', '{customer.name}', '{customer.email}');"""
    
    return (await execute_sql(sql_request), id)


@app.put("/customers/{id}")
async def update_customer(customer: Customer, id: int):
    """
    Permet de METTRE À JOUR un customer
    """
    sql_request = f"""UPDATE `customers` SET `firstname`='{customer.firstname}', `name`='{customer.name}',
    `email`='{customer.email}' WHERE `id`={id};"""
    
    return await execute_sql(sql_request)

@app.delete("/customers/{id}")
async def delete_customer(id: int):
    """
    Permet de SUPPRIMER un customer
    """
    sql_request = f"""DELETE FROM `customers` WHERE `id`={id};"""
    
    return await execute_sql(sql_request)