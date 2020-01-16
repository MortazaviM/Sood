from mongoengine import Document, EmbeddedDocument, fields,QuerySet
import datetime






class AllIndex(QuerySet):
    def get_by_mil(self, pk):
        pipeline = [
            {
                "$match":{
                    "TICKER":pk,
                    }
                    },
                    {
                "$project":{
                "x":{
                    "$subtract" : [{
                        "$convert":{
                            "input":{
                                "$dateFromString":{
                                    "dateString":{
                                        "$toString":"$DTYYYYMMDD"
                                        },
                                        "format": "%Y%m%d"
                                        }},
                                        "to":"date"
                                        }}, datetime.datetime(1970,1,1)
                                        ]},
                                        "y":"$CLOSE",
                                        "_id":0,
                                        }
            },{
                '$limit': 264,
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
    COMPANY = fields.StringField()
    CODE=fields.StringField()
    meta = {'queryset_class': AllIndex}

