from mongoengine import Document, EmbeddedDocument, fields, QuerySet
import datetime




class AllIndex(QuerySet):
    def get_data(self, pk):
        pipeline = [
        {
            "$project":{
                "CLOSE":1,
                "TICKER":1,
                "DTYYYYMMDD":1,
                
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

    def get_range(self,name,lte,gte):
        pipeline = [
            {
                "$match":{
                    name: {"$gte":int(gte), "$lte":int(lte)}
                }

            }
        ]
        return self.aggregate(*pipeline)

    def get_by_mil(self):
        pipeline = [
            {
                "$project":{
                "Date":{
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
                                        "OPEN":1,
                                        "HIGH":1,
                                        "LOW":1,
                                        "CLOSE":1,
                                        }
            }]
        return self.aggregate(*pipeline)



# Create your models here.
class indexstock(Document):
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




