from django.shortcuts import render
import requests

def get_preferred_image(images):
    for image in images:
        if image.get('ratio') == '16_9' and image.get('width') > 1024:
            return image.get('url')
    return images[0].get('url', 'N/A') if images else 'N/A'

def homepage_view(request):
    context = {
        'events': [],
        'error_message': '',
        'genre_artist_event': '',
        'city': ''
    }

    if 'genreArtistEvent' in request.GET and 'city' in request.GET:
        genre_artist_event = request.GET.get('genreArtistEvent')
        city = request.GET.get('city')

        if not genre_artist_event or not city:
            context['error_message'] = 'Search term and city cannot be empty'
        else:
            api_key = 'D7vEv0uy1A4ZVSByA6KbKX6Yk0EVAQG3'
            url = f'https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&classificationName={genre_artist_event}&city={city}&sort=date,asc'
            try:
                response = requests.get(url)
                data = response.json()
                if '_embedded' in data and 'events' in data['_embedded']:
                    for event in data['_embedded']['events']:
                        event_info = {
                            'event_name': event.get('name', 'N/A'),
                            'local_date': event['dates']['start'].get('localDate', 'N/A'),
                            'local_time': event['dates']['start'].get('localTime', 'N/A'),
                            'image_url': get_preferred_image(event.get('images', [])),
                        }

                        venue_info = event.get('_embedded', {}).get('venues', [{}])[0]
                        event_info.update({
                            'venue': venue_info.get('name', 'N/A'),
                            'city': venue_info.get('city', {}).get('name', 'N/A'),
                            'state': venue_info.get('state', {}).get('stateCode', 'N/A'),
                            'postal_code': venue_info.get('postalCode', 'N/A'),
                        })

                        context['events'].append(event_info)
                else:
                    context['error_message'] = 'No events found.'

            except requests.RequestException as e:
                context['error_message'] = f'Error fetching data: {str(e)}'

            context['genre_artist_event'] = genre_artist_event
            context['city'] = city

    return render(request, 'index.html', context)



def notes_view(request):
    return render(request, 'notes.html')



