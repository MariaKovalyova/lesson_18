# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from dao.director_dao import DirectorDAO
from dao.model.schemas import directors_schema, director_schema


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> list["Director"]:
        return directors_schema.dump(self.director_dao.get_all())

    def get_director(self, uid):
        return director_schema.dump(self.director_dao.get_one(uid))
