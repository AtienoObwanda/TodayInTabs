import unittest

from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will be called when before every test
        '''

        self.new_article= Article()
        pass