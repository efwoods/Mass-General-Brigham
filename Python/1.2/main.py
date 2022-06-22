import string, sys, argparse, bs4, requests
import bs4, requests

url = 'https://www.twitch.tv/vixxxie'
tags = []

def extract(url, tags):
    res = requests.get(url);
    res.raise_for_status();
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
#    elems = soup.select(tags)
#    print(elems[0].text.strip())

if __name__ == '__main__':
#    parser = argparse.ArgumentParser(description='Extract')
#    parser.add_argument('url', type=string)
#    args = parser.parse_args()
    extract(url,tags);

