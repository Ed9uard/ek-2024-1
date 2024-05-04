pipenv, version 2023.12.1
pipenv --rm 
pipenv sync --dev  

.venv\Scripts\activate

py createdb.py # створення testdb.db

py seed.py  # заповнення testdb.db

py run_sql_query.py виконання SQL

py delete_user.py вилучення user=1