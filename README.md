# Where to go - Moscow through Artem's eyes
[Russian](RU_README.md)

A site about the most interesting places in Moscow.
![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)

## Demo version of the site

## Setting up environment variables
Create a `.env` file next to the `manage.py` file

Create or generate a secret key and save it in `.env`:
```
SECRET_KEY=<Your secret key>
```
If you want to enable debug mode, save the `DEBUG` variable as well:
```
DEBUG=True
```
Create the `ALLOWED_HOSTS` variable

## Launch

Download the code to your computer

Install dependencies with the command
```
pip install -r requirements.txt
```
Run migrations:
```
python manage.py migrate
```
Create a superuser:
```
python manage.py createsuperuser
```

## Loading locations

It is convenient to use the admin panel to load locations: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
After loading is complete, run the server with the command:
```
python manage.py runserver
```
The site will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)