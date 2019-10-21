import requests
from urllib import request
import sys
import os

folder = 'F:\\vk_bot\\main\\photo\\'
group_name = input('input group name:\t')


def download_photo(photo_url, photo_id):
    """ This function download photo """
    path_to_download = folder + group_name + '\\'
    try:
        request.urlretrieve(photo_url, path_to_download + str(photo_id) + '.jpg')
    except:
        return 'download error: {}'.format(sys.exc_info())
    return 'done'


def get_photo_url(items):
    """ Here taking all urls of photo most big resolution """
    """ and call function 'download_photo', which to giving url and id, for download """
    links = []

    for item in items:
        try:
            for att in item['attachments']:
                for photo in att['photo']['sizes']:
                    if photo['type'] == 'z':
                        photo_id = att['photo']['id']
                        photo_url = photo['url']
                        links.append(photo_url)
                        print(download_photo(photo_url, photo_id))
        except:
            print('error')
            pass
    return links


def get_post(domain, count=100):
    """ This function get response from the wall group that you give in the function """
    url = 'https://api.vk.com/method/wall.get'
    access_token = '2949bad42949bad42949bad4122924d73c229492949bad474ec05c908e127c920034d67'
    version = '5.84'
    offset = 0
    items = []
    group = domain

    if not(os.path.exists(folder + domain)):
        os.mkdir(folder + domain)

    while offset < 100:
        response = requests.get(
            url,
            params={
                'access_token': access_token,
                'v': version,
                'domain': domain,
                'count': count,
                'offset': offset,
            }
        )
        items.extend(response.json()['response']['items'])
        offset += 100
    # Here happens call to function 'get_photo_url', in that to giving array with items
    url = get_photo_url(items)
    return url, print('downloading complete. All file: {}'.format(len(url)))


response = get_post(group_name)
input('exit')
