import os 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

db_user = os.getenv('DB_USER')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_password = os.getenv('DB_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# with app.app_context():
#     try:
#         with db.engine.connect() as connection:
#             # Run a simple query to ensure the connection is fully established
#             result = connection.execute(text('show tables;'))
#             rows = result.fetchall()
#         print(rows,"✅ Successfully connected to the database!",sep='\n')
#     except Exception as e:
#         print("❌ Database connection failed.")
#         print(f"Error: {e}")
# ------------------------------

if __name__=='__main__':
    app.run()