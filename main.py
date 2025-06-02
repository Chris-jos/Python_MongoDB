import pprint
from db_operations import *

printer = pprint.PrettyPrinter()
l_data = [("Ali", 32, "Surat"), ("Kumar", 45, "Punjab"), ("Lohit", 32, "Pune"), ("Tom", 21, "Kochi")]
l_docs = [
    {
        "name": name,
        "age": age,
        "location": location,
    }
    for name, age, location in l_data
]

# insert_multiple_document(collection="person", l_document=l_docs)
person = find_one(collection="person")
printer.pprint(person)

columns = {"_id":0, "name": 1, "location": 1}
age_32_person = find_all(collection="person", filter={"age": 32}, columns=columns)
printer.pprint(list(age_32_person))

count = count_of_docs(collection="person")
print(count)

