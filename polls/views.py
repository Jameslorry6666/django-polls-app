from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Welcome to My Django Project!</h1>
        <p><a href="/polls/message/">Go to Polls Message</a></p>
    """)



def polls_message(request):
    return HttpResponse("This is a message from the poll app! ")