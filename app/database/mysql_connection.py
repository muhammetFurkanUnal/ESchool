import mysql.connector
from mysql.connector import Error
from app.config import DB_CONFIG
from typing import Optional, Dict, List, Any
import os

class Database:
    def __init__(self, insert:bool):
        
        setup_db = "database_setup.sql"
        sample_insert_db = "database_sample_insertion.sql"
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        setup_full_path = os.path.join(base_path, setup_db)
        sample_insert_full_path = os.path.join(base_path, sample_insert_db)
        
        connected = self.connect()
        if not connected:
            raise Error("Can not connected to database")
        
        self.run_sql_file(setup_full_path)
        if insert:
            self.run_sql_file(sample_insert_full_path)
    
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=DB_CONFIG["host"],
                user=DB_CONFIG["user"], 
                password=DB_CONFIG["password"],
                database=DB_CONFIG["database"]
            )
            return True

        except Error as e:
            print(f"Database connection error: {e}")
            return False

    
    
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    
    def execute_query(self, query: str, params: tuple = None) -> Optional[List[Dict]]:
        if not self.connection or not self.connection.is_connected():
            self.connect()
        
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            
            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
                cursor.close()
                return result
            else: 
                self.connection.commit()
                last_id = cursor.lastrowid  # only nonzero when query is INSERT
                cursor.close()
                return last_id
                
        except Error as e:
            print(f"Query execution error: {e}")
            return None
    
    
    def execute_single(self, query: str, params: tuple = None) -> Optional[Dict]:
        result = self.execute_query(query, params)
        return result[0] if result else None
    
    
    def run_sql_file(self, filepath: str):
        if not os.path.exists(filepath):
            print(f"SQL file not found: {filepath}")
            return

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                sql_commands = f.read()

            # SQL komutlarını noktalı virgülle ayır
            commands = sql_commands.strip().split(';')

            cursor = self.connection.cursor()
            for command in commands:
                command = command.strip()
                if command:
                    try:
                        cursor.execute(command)
                    except Error as e:
                        print(f"Error executing command:\n{command}\n{e}")
            self.connection.commit()
            cursor.close()
            print(f"Executed SQL file: {filepath}")
        except Error as e:
            print(f"Error executing SQL file: {e}")
                
                
                
                
                
db = Database(insert=False)




