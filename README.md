# bu_banking


# Steps to run to get to Swagger API endpoints

1. Set up a Python virtual environment (to install the requirements into) - `python -m venv name_here`
2. Activate your virtual environment
3. Run `pip install -r requirements.txt` in the command line
4. To activate the application, run: `python manage.py runserver`
5. Access the webpage at the URL `http://127.0.0.1:8000/api/swagger/`



# If making changes to the model structure, make sure to run:
- `python manage.py makemigrations`
- `python manage.py migrations`