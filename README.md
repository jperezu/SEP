## Download heroku database
```bash
heroku run python3 manage.py dumpdata --exclude contenttypes > data.json
```
## Upload Django database
```bash
heroku run python3 manage.py migrate
heroku run python3 manage.py loaddata data.json
```
-------------------------------------------------------------------------------	
## Installation
* Assuming python already installed
```bash
python -m pip install -r requirements.txt
```
## Load database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data.json
python3 manage.py collectstatic
```
## Start app
```bash
python manage.py runserver
Go to http://127.0.0.1:8000/
```
## Login credentials
  USERNAME    |    PASSWORD  |  EMPLOYEE
------------- | -------------|-----------
admin|admin|Platform administrator
(open http://127.0.0.1:8000/admin for the administration platform)
-----------------------CS Manager----------------------
janet@sep.se|id2207sep|Janet
------------------------CS Team------------------------
	carine@sep.se		id2207sep   Carine
	judy@sep.se		    id2207sep   Judy
	sam@sep.se		    id2207sep   Sam
	sarah@sep.se		id2207sep   Sarah

	-------------------Financial Manager-------------------
	alice@sep.se		id2207sep   Alice

	-----------------Administration Manager----------------
	mike@sep.se		    id2207sep   Mike

	-------------------Production Manager------------------
	jack@sep.se		    id2207sep   Jack

	----------------------Decoration-----------------------
	ang@sep.se		    id2207sep   Angelina
	magy@sep.se		    id2207sep   Magy

	----------------------Photography----------------------
	magd@sep.se		    id2207sep   Magdalena
	tobi@sep.se         id2207sep   Tobias

	-------------------------Music-------------------------
	adam@sep.se		    id2207sep   Adam
	anto@sep.se		    id2207sep   Antony

	--------------------Graphic Design---------------------
	julia@sep.se		id2207sep   Julia
	raym@sep.se		    id2207sep   Raymond

	------------------------Computer-----------------------
	christ@sep.se		id2207sep   Christian
	mich@sep.se		    id2207sep   Michael
	nico@sep.se		    id2207sep   Nicolas
	robert@sep.se		id2207sep   Robert
			
	-------------------Services Manager--------------------
	natalie@sep.se		id2207sep   Natalie

	-------------------------Chef--------------------------
	chris@sep.se		id2207sep   Chris
	daniel@sep.se		id2207sep   Daniel
	diana@sep.se		id2207sep   Diana
	helen@sep.se		id2207sep   Helen
	marilyn@sep.se		id2207sep   Marilyn

	------------------------Waiter-------------------------
	brad@sep.se		    id2207sep   Brad
	johnny@sep.se		id2207sep   Johnny
	kate@sep.se		    id2207sep   Kate
	lauren@sep.se		id2207sep   Lauren
	meryl@sep.se		id2207sep   Meryl

	----------------------HR Manager-----------------------
	simon@sep.se		id2207sep   Simon
	

	






