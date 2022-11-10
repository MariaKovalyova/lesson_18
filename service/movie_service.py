# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from flask import request

from dao.model.models import Movie
from dao.model.schemas import movie_schema, movies_schema
from dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self, request_body):
        director_id = request_body.args.get('director_id')
        genre_id = request_body.args.get('genre_id')
        year = request_body.args.get('year')
        if director_id:
            return movies_schema.dump(self.movie_dao.get_by_director_id(director_id))
        if genre_id:
            return movies_schema.dump(self.movie_dao.get_by_genre_id(genre_id))
        if year:
            return movies_schema.dump(self.movie_dao.get_by_year(year))
        return movies_schema.dump(self.movie_dao.get_all())

    def get_movie(self, uid):
        return movie_schema.dump(self.movie_dao.get_one(uid))

    def post_movie(self, req_json):
        self.movie_dao.post_one(req_json)
        return 'all is ok', 201

    def del_movie(self, uid):
        self.movie_dao.del_one(uid)
        return "all is ok", 204

    def put_movie(self, uid, req_json):
        self.movie_dao.put_one(uid, req_json)
        return "edited", 204
