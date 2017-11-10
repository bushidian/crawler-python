class pageContent:
    def __init__(self, title, content, author='', tag='', cover = ''):
        self.title = title
        self.content = content
        self.author = author
        self.tag = tag
        self.cover = cover

    def toDict(self):

        entity = {'title': self.title, 'content': self.content, 'author': self.author, 'tag': self.tag, 'cover': self.cover}
        
        return entity
