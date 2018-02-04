import requests
from bs4 import BeautifulSoup, NavigableString, Tag

from project.apps.rulers.models import Ruler
from project.settings.base.wikipedia_parser import SUCCESSOR_PATTERN, AUSTRIA_PATTERN, IMPERIAL_PATTERN, FIRST_URL
import logging


logger = logging.getLogger('django')


def get_ruler_name_from_infobox(infobox: Tag):
    names_content = infobox.contents[0]
    names = names_content.text.split('\n')
    names = list(filter(''.__ne__, names))
    return names[0]


def is_infobox_child_with_successor(infobox_child: Tag):
    result = False
    th = infobox_child.find('th')
    if th and th(text=SUCCESSOR_PATTERN):
        result = True
    return result


def get_successor_url_from_infobox_child(infobox_child: Tag):
    successor_url = None
    a_tag = infobox_child.find('td').find('a')
    if a_tag:
        successor_url = a_tag.get('href')
        successor_url = 'https://ru.wikipedia.org' + successor_url
    return successor_url


def get_successor_url_from_infobox(infobox: Tag):
    in_austria_section = False
    in_imperial_section = False
    austria_next_url = None
    imperial_next_url = None
    for infobox_child in infobox.children:
        if not isinstance(infobox_child, NavigableString):
            if not in_austria_section and infobox_child(text=AUSTRIA_PATTERN):
                in_austria_section = True
                continue
            if not in_imperial_section and infobox_child(text=IMPERIAL_PATTERN):
                in_imperial_section = True
                continue
            if in_austria_section:
                if is_infobox_child_with_successor(infobox_child):
                    austria_next_url = get_successor_url_from_infobox_child(infobox_child)
                    if austria_next_url:
                        break
                    else:
                        in_austria_section = False
                        continue
            if in_imperial_section:
                if is_infobox_child_with_successor(infobox_child):
                    imperial_next_url = get_successor_url_from_infobox_child(infobox_child)
                    in_imperial_section = False
    return austria_next_url or imperial_next_url


def update_all_rulers():
    url = FIRST_URL
    previous_ruler = None
    succession_order = 0
    while url:
        request = requests.get(url)
        html = request.text

        soup = BeautifulSoup(html, 'html5lib')
        infobox = soup.find('table', {'class': 'infobox'})

        if infobox:
            infobox = infobox.find('tbody')
            name = get_ruler_name_from_infobox(infobox)
            ruler, is_create = Ruler.objects.update_or_create(url=url,
                                                              defaults={'name': name,
                                                                        'succession_order': succession_order,
                                                                        'predecessor': previous_ruler})
            if is_create:
                logger.info('Austria ruler {ruler} was created'.format(ruler=str(ruler)))
            else:
                logger.info('Austria ruler {ruler} was updated'.format(ruler=str(ruler)))
            previous_ruler = ruler
            url = get_successor_url_from_infobox(infobox)
            succession_order += 1
        else:
            url = None
