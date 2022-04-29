class Article:
    '''
    Article class to define articles
    '''
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content



class Source:
    """
    Source class to define News Sources
    """
    def __init__(self,id,name,description,url,category):
        self.id= id
        self.name = name
        self.description = description
        self.url= url
        self.category = category
        