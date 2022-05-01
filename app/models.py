class Article:
    '''
    Article class to define articles
    '''
    def __init__(self,source,author,title,description,url,image,publishedAt,content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.publishedAt = publishedAt
        self.content = content



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
