from django.shortcuts import render

def homepage_view(request):
    # Your logic here
    return render(request, 'index.html')

def notes_view(request):
    # Your logic here
    return render(request, 'notes.html')


# https://app.ticketmaster.com/discovery/v2/events.json?apikey=D7vEv0uy1A4ZVSByA6KbKX6Yk0EVAQG3&classificationName=${genreArtistEvent}&city=${city}&sort=date,asc

