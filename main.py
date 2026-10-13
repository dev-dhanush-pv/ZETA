from app import create_app

app = create_app()
# users = User.query.all()
# print(users)

if __name__ == '__main__':
    app.run(debug=True)