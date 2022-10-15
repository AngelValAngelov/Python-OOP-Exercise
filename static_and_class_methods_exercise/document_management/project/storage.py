from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def get_doc(documents, document_id):
        document = [d for d in documents if d.id == document_id]
        if document:
            return document[0]

    @staticmethod
    def get_topic(topics, topic_id):
        topic = [t for t in topics if t.id == topic_id]
        if topic:
            return topic[0]

    @staticmethod
    def get_category(categories, category_id):
        category = [c for c in categories if c.id == category_id]
        if category:
            return category[0]

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = Storage.get_category(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = Storage.get_topic(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = Storage.get_doc(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = Storage.get_category(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = Storage.get_topic(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = Storage.get_doc(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = Storage.get_doc(self.documents, document_id)
        return document

    def __repr__(self):
        result = '\n'.join([d.__repr__() for d in self.documents])
        return result


c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
