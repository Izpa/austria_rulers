from django.test import TestCase

from project.apps.rulers.wikipedia_parser_utils import *


class GetSuccessorURLFromInfoboxTest(TestCase):
    def setUp(self):
        self.ruler_url = 'google.com'
        html = """"
                <table class="infobox">
                <tbody>
                <tr>
                <th>
                <table>
                <tbody><tr>
                <td>маркграф Австрии</td>
                </tr>
                </tbody></table>
                </th>
                </tr>
                <tr>
                <th>Преемник:</th>
                <td><a href="{ruler_url}">Генрих I</a></td>
                </tr>
                </tbody></table>
                """.format(ruler_url=self.ruler_url)
        soup = BeautifulSoup(html, 'html5lib')
        self.infobox_with_austria_ruler = soup.find('table', {'class': 'infobox'}).find('tbody')

    def test_simple_infobox(self):
        next_url = get_successor_url_from_infobox(self.infobox_with_austria_ruler)
        self.assertEqual(next_url, WIKIPEDIA_URL + self.ruler_url)


class GetSuccessorURLFromInfoboxChild(TestCase):
    def test_without_url(self):
        url = '/ruler'
        html = """"
                <table class="infobox">
                <tbody><tr>
                <td>Титул упразднён</td>
                </tr>
                </tbody>
                </table>
                """.format(url=url)
        soup = BeautifulSoup(html, 'html5lib').find('table', {'class': 'infobox'}).find('tbody')
        self.assertIsNone(get_successor_url_from_infobox_child(soup))

    def test_with_url(self):
        url = '/ruler'
        html = """"
                <table class="infobox">
                <tbody><tr>
                <td><a href="{url}"></a></td>
                </tr>
                </tbody>
                </table>
                """.format(url=url)
        soup = BeautifulSoup(html, 'html5lib').find('table', {'class': 'infobox'}).find('tbody')
        self.assertEqual(get_successor_url_from_infobox_child(soup), WIKIPEDIA_URL+url)


class IsInfoboxChildWithSuccessor(TestCase):
    def test_with_successor(self):
        html = """"
        <table class="infobox">
        <tbody><tr>
        <th>Преемник:</th>
        </tr>
        </tbody>
        </table>
        """
        soup = BeautifulSoup(html, 'html5lib').find('table', {'class': 'infobox'}).find('tbody')
        self.assertTrue(is_infobox_child_with_successor(soup))

    def test_without_successor(self):
        html = """"
            <table class="infobox">
            <tbody><tr>
            <th>Предшественник:</th>
            </tr>
            </tbody>
            </table>
            """
        soup = BeautifulSoup(html, 'html5lib').find('table', {'class': 'infobox'}).find('tbody')
        self.assertFalse(is_infobox_child_with_successor(soup))


class GetRulerNameFromInfoboxTest(TestCase):
    def setUp(self):
        self.ruler_name = 'Леопольд I'
        html = """"
            <table class="infobox">
            <tbody><tr>
                <td>{ruler_name}
            </td>
            </tr>
            </tbody>
            </table>
        """.format(ruler_name=self.ruler_name)
        soup = BeautifulSoup(html, 'html5lib')
        self.infobox_with_austria_ruler_name = soup.find('table', {'class': 'infobox'}).find('tbody')

    def test_simple_name(self):
        ruler_name = get_ruler_name_from_infobox(self.infobox_with_austria_ruler_name)
        self.assertEqual(ruler_name, self.ruler_name)
