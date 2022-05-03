import unittest
from app.models import Article, Source



class SourceTest(unittest.TestCase):
    '''
    Test Class to test source
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('Vogue','Vogue News','Vogue delivers Fashion news, trends, analysis, and video to the world','Vogue.com','general','France','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_source.id,'Vogue')
        self.assertEqual(self.new_source.name,'Vogue News')
        self.assertEqual(self.new_source.description,'Vogue delivers Fashion news, trends, analysis, and video to the world')
        self.assertEqual(self.new_source.url,'Vogue.com')
        self.assertEqual(self.new_source.category,'general')
        self.assertEqual(self.new_source.country,'France')
        self.assertEqual(self.new_source.language,'en')

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test Articles
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Vogue','Atieno Obwanda','The traditional African wear-A hit or a miss?','Dive deep into the Ankara history','vogue.com','vogue.com/54M55.png','2022-05-03T09:00')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_article.id,'Vogue')
        self.assertEqual(self.new_article.author,'Atieno Obwanda')
        self.assertEqual(self.new_article.title,'The traditional African wear-A hit or a miss?')
        self.assertEqual(self.new_article.description,'Dive deep into the Ankara history')
        self.assertEqual(self.new_article.url,'vogue.com')
        self.assertEqual(self.new_article.image,'vogue.com/54M55.png')
        self.assertEqual(self.new_article.date,'2022-05-03T09:00')

