# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from dao.genre_dao import GenreDAO
from dao.model.schemas import genres_schema, genre_schema


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self) -> list["Genre"]:
        return genres_schema.dump(self.genre_dao.get_all())

    def get_genre(self, uid):
        return genre_schema.dump(self.genre_dao.get_one(uid))
