## Download heroku database
```bash
heroku run python3 manage.py dumpdata --exclude contenttypes > data.json
```
## Upload Django database
```bash
heroku run python3 manage.py migrate
heroku run python3 manage.py loaddata data.json
```