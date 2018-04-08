from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    html_ = """
            <!DOCTYPE html>
            <html lang=en>
            <head>
            </head>
            <body>
            <h3>Hello WOrld!</h3>
            <p>This is a labourous way to display text using the markup of a webpage.
            </body>
            </html>
            """
    return HttpResponse(html_)
