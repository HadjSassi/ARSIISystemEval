from pymongo import MongoClient
from mongo_setup import URL


class CommentaireService:
    def __init__(self):
        self.client = MongoClient(URL)
        self.database = self.client['Lancers']
        self.collection = self.database['Commentaire']

    def read_all(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # get comments by email of commentator
    def get_comments_by_email(self, email):
        documents = self.collection.find({"email": email})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # get comments by email of commentator and date
    def get_comments_by_email_and_date(self, email, date):
        documents = self.collection.find({"email": email, "dateComment": date})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # get comments by id of Service
    def get_comments_by_service_id(self, service_id):
        documents = self.collection.find({"idService": service_id})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get comments by id of Service and date

    def get_comments_by_service_id_and_date(self, service_id, date):
        documents = self.collection.find({"idService": service_id, "dateComment": date})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get comments by id of Service and email of commentator
    def get_comments_by_service_id_and_email(self, service_id, email):
        documents = self.collection.find({"idService": service_id, "email": email})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get comments by id of Service and email of commentator and date
    def get_comments_by_service_id_and_email_and_date(self, service_id, email, date):
        documents = self.collection.find(
            {"idService": service_id, "email": email, "dateComment": date})
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
