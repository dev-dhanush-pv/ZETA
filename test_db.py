from app import create_app
from app.models.models import User

# 1. Create the Flask app
app = create_app()

# 2. Open an application context
with app.app_context():
    print("Testing Database Connection...")
    
    try:
        # 3. Run a query to get all users
        users = User.query.all()
        
        print(f"✅ Success! Found {len(users)} users in the database.\n")
        
        # 4. Loop through and print them
        for user in users:
            print(f"ID: {user.id} | Name: {user.full_name} | Email: {user.email}")
            
    except Exception as e:
        print("❌ Query failed!")
        print(f"Error: {e}")