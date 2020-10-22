## SEP application
<p>The SEP platform is currently running on an online server. <br>
To access the service go to https://id2207-sep.herokuapp.com/ <br>
To use the local version run the next command from root directory of the SEP project just the fist time:</p>

```bash
python sep_server.py
```

To start the server for later executions (without reintalling the dependencies), run the following command:
```bash
python manage.py runserver
```

The script <i>sep_server.py</i> installs the needed requirements, checks the database structure, populates it, and runs the application server <i>(Assuming python already installed, else go to https://www.python.org/downloads/)</i>

<b>(The server needs to remain opened while the application is running to work)</b>

* To access the local application go to http://127.0.0.1:8000/
* To access the administration platform go to http://127.0.0.1:8000/admin/

-------------------------------------------------------------------------------

## Login credentials
	USERNAME	PASSWORD	EMPLOYEE
	--------------------------------------
	admin 		admin 		Platform administrator

	--------------CS Manager--------------
	janet@sep.se 	id2207sep	Janet

	----------------CS Team---------------
	carine@sep.se	id2207sep   	Carine
	judy@sep.se	id2207sep   	Judy
	sam@sep.se 	id2207sep   	Sam
	sarah@sep.se	id2207sep   	Sarah

	-----------Financial Manager----------
	alice@sep.se	id2207sep   	Alice

	--------Administration Manager--------
	mike@sep.se	id2207sep   	Mike

	----------Production Manager----------
	jack@sep.se	id2207sep   	Jack

	--------------Decoration--------------
	ang@sep.se	id2207sep   	Angelina
	magy@sep.se	id2207sep   	Magy

	--------------Photography--------------
	magd@sep.se	id2207sep   	Magdalena
	tobi@sep.se    	id2207sep   	Tobias

	-----------------Music-----------------
	adam@sep.se	id2207sep   	Adam
	anto@sep.se	id2207sep   	Antony

	------------Graphic Design-------------
	julia@sep.se	id2207sep   	Julia
	raym@sep.se	id2207sep   	Raymond

	----------------Computer---------------
	christ@sep.se	id2207sep   	Christian
	mich@sep.se	id2207sep   	Michael
	nico@sep.se	id2207sep   	Nicolas
	robert@sep.se	id2207sep   	Robert
			
	-----------Services Manager------------
	natalie@sep.se	id2207sep   	Natalie

	-----------------Chef------------------
	chris@sep.se	id2207sep   	Chris
	daniel@sep.se	id2207sep   	Daniel
	diana@sep.se	id2207sep   	Diana
	helen@sep.se	id2207sep   	Helen
	marilyn@sep.se	id2207sep   	Marilyn

	----------------Waiter-----------------
	brad@sep.se	id2207sep   	Brad
	johnny@sep.se	id2207sep   	Johnny
	kate@sep.se	id2207sep   	Kate
	lauren@sep.se	id2207sep   	Lauren
	meryl@sep.se	id2207sep   	Meryl

	--------------HR Manager---------------
	simon@sep.se	id2207sep   	Simon
	
-------------------------------------------------------------------------------

## Testing

To run the test, run the following command:
```bash
python manage.py test
```
The purpose of this test is to find differences between the system and its models by executing the system with sample input data sets. During this unit testing, we compared the object design model with each object and subsystem. The goal of testing is to discover as many faults as possible such that we can be repaired before the delivery of the system.
