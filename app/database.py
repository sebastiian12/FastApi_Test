from pymongo import MongoClient

conectionString= "mongodb+srv://Sebas:seba1234@cluster0.xtn4vi9.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"
client = MongoClient(conectionString)

db = client.test
benefits__collection = db.benefits