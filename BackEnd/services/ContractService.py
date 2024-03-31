from pymongo import MongoClient
from mongo_setup import URL


class ContractService:
    def __init__(self):
        self.client = MongoClient(URL)
        self.database = self.client['Lancers']
        self.collection = self.database['Contract']

    def read_all(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by id
    def get_contracts_by_demandeur_id(self, id):
        document = self.collection.find_one({"id": id})
        if document:
            output = {item: document[item] for item in document if item != '_id'}
            return output
        else:
            return {'Status': 'Contract not found.'}

    # Get contracts by email of demandeur
    def get_contracts_by_demandeur_email(self, email):
        documents = self.collection.find({"email": email})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by email of demandeur and etat
    def get_contracts_by_demandeur_email_and_etat(self, email, etat):
        documents = self.collection.find({"email": email, "Etat": etat})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by email of demandeur and date
    def get_contracts_by_demandeur_email_and_date(self, email, date):
        documents = self.collection.find({"email": email, "dateDebut": date})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by id of Service
    def get_contracts_by_service_id(self, service_id):
        documents = self.collection.find({"idService": service_id})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by id of Service and date
    def get_contracts_by_service_id_and_date(self, service_id, date):
        documents = self.collection.find({"idService": service_id, "dateDebut": date})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by id of Service and etat
    def get_contracts_by_service_id_and_etat(self, service_id, etat):
        documents = self.collection.find({"idService": service_id, "Etat": etat})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by id of Service and email of demandeur
    def get_contracts_by_service_id_and_demandeur_email(self, service_id, email):
        documents = self.collection.find({"idService": service_id, "email": email})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by id of Service and email of demandeur and date
    def get_contracts_by_service_id_and_demandeur_email_and_date(self, service_id, email, date):
        documents = self.collection.find({"idService": service_id, "email": email, "dateDebut": date})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    # Get contracts by id of Service and email of demandeur and etat
    def get_contracts_by_service_id_and_demandeur_email_and_etat(self, service_id, email, etat):
        documents = self.collection.find({"idService": service_id, "email": email, "Etat": etat})
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

