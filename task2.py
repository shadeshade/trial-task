from pathlib import Path

import requests

CUR_DIR = Path(__file__).resolve().parent


def normalize_url(url):
    if 'http://' not in url and 'https://' not in url:
        url = 'http://' + url
    return url


def get_html_str(url):
    url = normalize_url(url)
    try:
        source = requests.get(url)
    except requests.exceptions.Timeout:
        print("The request timed out")
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects")
    except requests.exceptions.RequestException:
        print("There was an ambiguous exception that occurred while handling your request")
    else:
        soup = source.content
        return str(soup)


def save_html_file(filename, html_str):
    folder_path = CUR_DIR / "files"
    with open(f"{folder_path / filename}.html", "w") as f:
        f.write(html_str)


def save_to_disk(url_list: list):
    url_count = len(url_list)

    for url in url_list:
        html_str = get_html_str(url)
        if html_str:
            save_html_file(url, html_str)
        else:
            url_count -= 1
    print(f"{url_count} files created")


if __name__ == '__main__':
    url = ['www.google.ru']
    u_list = ['www.google.ru', 'www.mail.ru', 'www.ya.ru']
    u_list2 = ['www.goog1e.ru', 'www.mail.ru', 'www.ya.ru']
    save_to_disk(u_list)
