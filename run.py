from main import create_app, db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # 确保数据库表被创建
    app.run(debug=True)
