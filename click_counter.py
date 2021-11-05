import requests
from urllib import parse


def shorten_link(url: str,
                 headers: dict) -> str:
    """Makes the link shorter using bitly's API

    :param url: url entered by user
    :param headers: headers including Token, which will be loaded into request
    :return: short url
    string 'Here is your shorten link: {short_link}'

    :example:

    url = https://google.com
    headers = headers = {"Authorization": f"Bearer {BITLY_TOKEN}"}
    returns: Here is your shorten link: bit.ly/3mFwWQ2
    """

    if parse.urlparse(url).scheme not in ("http", "https"):
        return 'please add http:// or https:// to your address'

    address = "https://api-ssl.bitly.com/v4/bitlinks"
    json = {"long_url": url}
    response = requests.post(address, headers=headers, json=json)
    if not response.ok:
        return f"some errors in your link, status code: {response.status_code}"
    short_link = response.json()['id']
    return f'Here is your shorten link: {short_link}'


def count_clicks(url: str,
                 headers: dict) -> str:
    """Сounts the number of clicks on the link using bitly's API

    :param url: url entered by user
    :param headers: headers including Token, which will be loaded into request
    :return: string "some errors in your link, status code: {status_code}"
    with code of the mistake or
    string 'f"Number of clicks: {num_of_clicks}'

    :example:

    url =  bit.ly/3mFwWQ2
    headers = headers = {"Authorization": f"Bearer {BITLY_TOKEN}"}
    returns: Number of clicks: 1
    """
    if parse.urlparse(url).scheme == "https":
        url = parse.urlparse(url).netloc
    address = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks"
    payload = {
        "unit": "month",
        "units": "-1"
    }
    response = requests.get(address, headers=headers, params=payload)
    if not response.ok:
        return f"some errors in your link, status code: {response.status_code}"

    num_of_clicks = response.json()['link_clicks'][0]['clicks']
    return f"Number of clicks: {num_of_clicks}"


def is_bitlink(url: str) -> bool:
    """Determines if a link has been shortened

    :param url: url entered by user with or without bit.ly
    :return: True or False, depends on the presence of 'bit.ly' in the url.

    :example:

    url = bit.ly/3mFwWQ2
    returns: True
    """
    if "bit.ly" not in url:
        return False
    return True


def run_script(url: str,
               headers: dict):
    """Running the script

    :param url: url entered by user
    :param headers: headers including Token, which will be loaded into request
    :return: short link or number of clicks

    :example:

    url = bit.ly/3mFwWQ2
    returns: Number of clicks: 1
    """
    if is_bitlink(url):
        return count_clicks(url, headers)
    return shorten_link(url, headers)
