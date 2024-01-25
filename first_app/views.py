from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Мой первый Django-сайт</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.5;
                    margin: 0;
                    padding: 20px;
                }

                h1 {
                    color: #333;
                }

                p {
                    color: #777;
                }
            </style>
        </head>
        <body>
            <h1>Добро пожаловать на мой сайт!</h1>

            <h2>О сайте</h2>
            <p> Этот сайт создан во время изучения фреймворка Django на платформе GeekBrains</p>

            <h2>Обо мне</h2>
            <p>Меня зовут Чернышов Дмитрий. Изучаю Python, С#, Java, HTML, CSS, Flask и Django.</p>

            <footer>
                <p>Связаться со мной: 1)почта chernyshov85@mail.ru, Telegram @nihi1 </p>
            </footer>
        </body>
        </html>
        """
    return HttpResponse(html)


def about(request):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
</head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }

            h1 {
                color: #333;
            }

            p {
                color: #777;
            }
        </style>
<body>
    <header>
        <h1>Меня зовут Дмитрий Чернышов.</h1>
    </header>

    <main>
        <section>
            <h2>Опыт работы</h2>
            <ul>
                <li>Место работы 1</li>
                <li>Место работы 2</li>
                <li>Место работы 3</li>
            </ul>
        </section>

        <section>
            <h2>Образование</h2>
            <ul>
                <li>Университет 1</li>
                <li>Университет 2</li>
            </ul>
        </section>

        <section>
            <h2>Навыки</h2>
            <ul>
                <li>Навык 1</li>
                <li>Навык 2</li>
                <li>Навык 3</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>Свяжитесь со мной: Mail - chernyshov85@mail.ru | TG - @nihi1</p>
    </footer>
</body>
</html>
"""
    return HttpResponse(html)