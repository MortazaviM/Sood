from mongoengine import Document, EmbeddedDocument, fields, QuerySet





class AllIndex(QuerySet):
    def get_data(self, pk):
        pipeline = [
        {
            "$project":{
                "CLOSE":1,
                "TICKER":1,
                
                }
        },
        {
            "$match":{
                "TICKER":pk
            }
        },
        {
            "$limit":100
        }]
        return self.aggregate(*pipeline)


# Create your models here.
class data(Document):
    TICKER=fields.StringField()
    DTYYYYMMDD=fields.IntField()
    OPEN=fields.FloatField()
    HIGH=fields.FloatField()
    LOW=fields.FloatField()
    CLOSE=fields.FloatField()
    VOL=fields.IntField()
    VALUE=fields.FloatField()
    TEDAD=fields.IntField()
    LAST=fields.IntField()
    meta = {'queryset_class': AllIndex}

