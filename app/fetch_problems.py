import constants
import utils

from lxml.html import document_fromstring
import requests

import datetime


def main():
    results = fetch_homepage()
    assert results, 'No results found!'
    result_str = '\n'.join(results)
    
    write_path = utils.get_expected_problem_filepath()
    log('Writing results...')
    with open(write_path, 'w') as fl:
        fl.write(result_str)
    log('Done!')


def fetch_homepage():
    res = get(f'{constants.CODINGBAT_DOMAIN}/python')
    dom = document_fromstring(res.text)
    problem_sets = dom.xpath('//div[contains(@class, "summ")]//a[contains(@href, "python")]/@href')

    all_problem_urls = []
    for prob in problem_sets:
        url = constants.CODINGBAT_DOMAIN + prob
        problem_urls = fetch_ps(url)
        all_problem_urls.extend(problem_urls)

    return all_problem_urls


def fetch_ps(url):
    log(f'Fetching url... {url}')
    res = get(url)
    dom = document_fromstring(res.text)
    problem_urls = dom.xpath('//a[contains(@href, "prob")]/@href')
    return [constants.CODINGBAT_DOMAIN + url for url in problem_urls]


def get(url):
    return requests.get(
        url, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        }
    )    


def log(msg):
    ts = datetime.datetime.now().strftime('[%Y-%m-%d %H:%S]')
    print(f'{ts}: {msg}')


if __name__ == '__main__':
    main()
