from pymongo import MongoClient
from mongo_setup import URL


class RestrictionService:
    def __init__(self):
        self.client = MongoClient(URL)
        self.database = self.client['Lancers']
        self.collection = self.database['Restricition']

    def read_all(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def get_Restriction_by_id(self, id):
        id = int(id)
        document = self.collection.find_one({"idRestriction": id})
        if document:
            output = {item: document[item] for item in document if item != '_id'}
            return output
        else:
            return {'Status': 'Restriction not found.'}

    def get_projects_by_lancer_email(self, email):
        documents = self.collection.find({"lancerEmail": email})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def get_projects_by_lancer_email_and_date(self, email, date):
        documents = self.collection.find({"lancerEmail": email, "debut": date})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, new_document):
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted', 'Document_ID': str(response.inserted_id)}
        return output

    def update(self, filt, updated_data):
        response = self.collection.update_one(filt, {"$set": updated_data})
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, filt):
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
