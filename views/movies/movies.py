from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return movie_service.get_movies(request), 200

    def post(self):
        movie_service.post_movie(request.json)
        return "all is ok", 201


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        return movie_service.get_movie(uid), 200

    def delete(self, uid):
        movie_service.del_movie(uid)
        return "deleted", 204

    def put(self, uid):
        movie_service.put_movie(uid, request.json)
        return "edited", 204

