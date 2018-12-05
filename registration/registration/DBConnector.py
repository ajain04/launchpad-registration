import boto3

class DBConnector:
    """This class will provide connection and CRUD operations on database"""
    def __init__(self,dburl=None):
        self._dburl=dburl

    def create_connection(self):
        try:
            if self._dburl is None:
                dynamodb_client = boto3.client('dynamodb')
            else:
                dynamodb_client = boto3.client('dynamodb',endpoint_url=self._dburl)
            return dynamodb_client
        except:
            return "Error in creating connection"

    def list_tables(self):
        try:
            conn = self.create_connection()
            results = conn.list_tables()
            return results
        except:
            return "error in connection"
    def insert(self,tablename,item):
        try:
            conn = self.create_connection()
            result = conn.put_item(TableName=tablename, Item=item)
            return result
        except Exception as e:
            return str(e)