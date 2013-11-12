from google.appengine.ext import db
from google.appengine.api.users import User

class Post(db.Model):
    title = db.StringProperty(required=True)
    body = db.TextProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    creator = db.UserProperty(required = False)
    
    def __unicode__(self):
        return self.title
