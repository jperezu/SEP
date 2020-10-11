Download heroku database:
	heroku run python3 manage.py dumpdata --exclude contenttypes > data.json

Install requirements
	(Assuming python already installed)
	python -m pip install -r requirements.txt
Load database:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py loaddata data.json
	python3 manage.py collectstatic

start app:
	python manage.py runserver
	Go to http://127.0.0.1:8000/