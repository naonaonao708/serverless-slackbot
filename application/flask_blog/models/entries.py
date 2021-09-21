from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute

class Entry(Model):
    class Meta:
        table_name = "serverless_blog_entries"
        region = 'ap-northeast-1'
        aws_access_key_id = 'aws_access_key_id'
        aws_secret_access_key = 'aws_secret_access_key'
        host = "http://localhost:8000"

    id = NumberAttribute(hash_key=True, null=False)
    title = UnicodeAttribute(null=True)
    text = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default=datetime.now)
    
