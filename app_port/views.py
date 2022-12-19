from django.shortcuts import render
from app_port.forms import DateForm
import time
import requests
from datetime import datetime
import pytz

t1 = time.time()
tz = pytz.timezone("Asia/Yekaterinburg")


def enter(request):
    return render(request, 'port/enter.html')


def home(request):
    tz = pytz.timezone("Asia/Yekaterinburg")
    date_start = datetime(2022, 1, 1).replace(tzinfo=pytz.UTC).astimezone(tz)
    end_time = datetime.now().replace(tzinfo=pytz.UTC).astimezone(tz)
    url = f'https://api.vk.com/method/wall.get'
    token = '0b5e3db80b5e3db80b5e3db8f1084fdc7400b5e0b5e3db868c7cb354b3955f61562280e'
    version = 5.131
    domain = 'port.surgut'
    count = 100
    offset = 0
    all_posts = []
    desc = ''

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date_start = datetime.combine(form.cleaned_data.get('date_start'), datetime.min.time())
            end_time = datetime.combine(form.cleaned_data.get('end_time'), datetime.min.time())
    else:
        form = DateForm()
    print(date_start.timestamp(), end_time.timestamp())
    while offset < 250:
        resp = requests.get(url, params={
            'access_token': token,
            'domain': domain,
            'count': count,
            'offset': offset,
            'v': version
        }
                            )

        data = resp.json()['response']['items']

        for post in data:
            try:
                if post['attachments'][0]['type']:
                    desc = post['attachments'][0]['video']['description']
                else:
                    desc = None
            except:
                pass
            all_posts.extend([{'text': post['text'],
                               'desc': desc,
                               'comments': post['comments']['count'],
                               'likes': post['likes']['count'],
                               'reposts': post['reposts']['count'],
                               'views': post['views']['count'],
                               'date': datetime.utcfromtimestamp(int(post['date'])).replace(
                                   tzinfo=pytz.UTC).astimezone(tz)}])
        offset += 100

    all_posts = list(filter(lambda x: end_time.timestamp() >= x['date'].timestamp() >= date_start.timestamp(), all_posts))
    # print(all_posts)
    # my_date = all_posts[-1]['date']
    count_post = len(all_posts)
    count_comments = sum([post['comments'] for post in all_posts])
    count_likes = sum([post['likes'] for post in all_posts])
    count_reposts = sum([post['reposts'] for post in all_posts])
    count_views = sum([post['views'] for post in all_posts])
    max_comments = max(all_posts, key=lambda i: i['comments'])
    max_likes = max(all_posts, key=lambda i: i['likes'])
    max_reposts = max(all_posts, key=lambda i: i['reposts'])
    max_views = max(all_posts, key=lambda i: i['views'])

    return render(request, 'port/home.html', {'form': form,
                                              'info': all_posts,
                                              'date_start': date_start,
                                              'end_time': end_time,
                                              'count_post': count_post,
                                              'count_comments': count_comments,
                                              'count_likes': count_likes,
                                              'count_reposts': count_reposts,
                                              'count_views': count_views,
                                              'max_comments': max_comments,
                                              'max_likes': max_likes,
                                              'max_reposts': max_reposts,
                                              'max_views': max_views})
