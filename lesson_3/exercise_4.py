from uuid import uuid4
import hashlib

salt = uuid4().hex
cache_dct = {}


def check_url(url):
    if cache_dct.get(url):
        print(f"Хэш {url} - {cache_dct[url]}")
    else:
        hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_dct[url] = hash_url
    return cache_dct


if __name__ == "__main__":
    print(check_url("https://gb.ru/"))
    print(check_url("https://gb.ru/"))
    print(check_url("https://mail.ru/"))
    print(check_url("https://mail.ru/"))
