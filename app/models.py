class Article:
    '''
    Article class to define articles
    '''
    def __init__(self,image,title,description,author,source,url,date):
        self.image = image
        self.title = title
        self.description = description
        self.author = author
        self.source = source
        self.url = url
        self.date = date


class Source:
    """
    Source class to define News Sources
    """
    def __init__(self,id,name,description,url,category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
