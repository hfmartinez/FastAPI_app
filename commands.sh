docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=your_password -e MYSQL_DATABASE=todo_db -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3306:3306 -d arm64v8/mysql:8.0

docker run --name fastapi-app --env-file .env -p 8000:8000 --link mysql-container:mysql -d fastapi-todo