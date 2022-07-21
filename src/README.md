# GoG


### Project Setup 
```
1. Download Python version 3.x on your machine

2. Create a virtual environment by typing "python -m venv project-name"

3. Activate the virtual environment by typing "project-name\Scripts\activate.bat" (For windows OS)

4. If you're running unix base OS type "source project-name/bin/activate"

5. Change into the project directory by typing "cd wonder\src"

6. Install the project requirements by typing "pip install -r requirements.txt"
```

### Compile and run for development 
```
1. Make migrations of django models by typing "python manage.py makemigrations"

2. Migrate the model data into sqlite3 database by typing "python manage.py migrate"

3. Create a superuser for the management of the system by typing "python manage.py createsuperuser".

4. Run the Application by typing "python manage.py runserver". This should show the url to access the site in your browser (default: http://127.0.0.1:8000).

5. You can access the administrator section of the app by visiting http://127.0.0.1:8000/admin/

6. You can also visit the API endpoints by visiting http://127.0.0.1:8000/api/
```

### On successfull execution of the application in the browser, you should see a rocket on the screen of the homepage. Now you can open another terminal/cmd to run the frontend. Do not terminate the terminal/cmd running the Django application.

### Make sure you have node.js and npm or yarn installed on your machine to be able to successfully run the second part of the system.