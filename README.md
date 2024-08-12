# Where to go - Moscow through Artem's eyes
[Russian](RU_README.md)

A site about the most interesting places in Moscow.
![Куда пойти](https://github.com/user-attachments/assets/7794d2e8-bab8-4d4b-ae82-c7993b2cf923)


## Demo version of the site

[Демо-версия](https://gulfia83.pythonanywhere.com/)

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

To load a small number of locations, it is convenient to use the admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
With a large number of locations, it is possible to add them to the database using the `load_place`` command.

To do this, save the location data in separate json files of the following type:

```js
{
    "title": "Эйфелева башня в Москве",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/8868d171420b5221f8f50af5e95a7b12.jpeg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/46cb25cf1719bf546c8bbcf1b51ba4f4.jpeg"
    ],
    "description_short": "Вы можете поехать в Париж и отстоять огромную очередь, чтобы посетить главную его достопримечательность — великолепную Эйфелеву башню.А можете просто сесть в метро и, не выезжая за пределы МКАД, прикоснуться к точной её копии.",
    "description_long": "<p><strong>Эйфелева башня в Москве</strong> находится недалеко от станции метро «Авиамоторная» на территории одного из производственных предприятий — завода «Москабельмет». Соорудили точную копию мировой архитектурной знаменитости сами рабочие этого завода. Высота заводской башни — 15 метров (для справки — высота оригинальной, парижской Эйфелевой башни составляет 324 метра)."
    "coordinates": {
        "lng": "37.71241599999999",
        "lat": "55.74669399999998"
    }
}
```
Then run the command replacing `<json_url>` with the url of your file:
```
python manage.py load_place <json_url>
```

After loading is complete, run the server with the command:
```
python manage.py runserver
```
The site will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
