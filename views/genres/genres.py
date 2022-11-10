from flask_restx import Resource, Namespace

from implemented import genre_service

genres_ns = Namespace('genres')

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genre_service.get_genres(), 200


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        return genre_service.get_genre(uid), 200

