#! python3

import requests
import os
import bs4

BASE_URL = "http://xkcd.com"
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok = True)


def get_prev_url(soup):
    """Returns url of previous comic.
    """
    prev_link = soup.select('a[rel="prev"]')[0]
    url = BASE_URL + prev_link.get("href")
    return url


def save_image_file(comic_url):
    image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()


while not url.endswith("#"):
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")

    comic = soup.select("#comic img")
    if comic == []:
        print("Could not find comic image.")
    else:
        try:
            comic_url = "http:" + comic[0].get("src")
            print("Downloading image...")
            res = requests.get(comic_url)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            url = get_prev_url(soup)
            continue

    save_image_file(comic_url)

    # Get the Prev button's url.
    url = get_prev_url(soup)

print("Done.")
