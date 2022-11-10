from flask import request

from dao.model.models import Movie
from utils import pagination


class MovieDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 5))
        query = pagination(self.session.query(Movie), page, page_size)
        return query.all()

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def post_one(self, posted_movie):
        self.session.add(Movie(**posted_movie))
        self.session.commit()

    def del_one(self, uid):
        movie = self.get_one(uid)
        self.session.delete(movie)
        self.session.commit()

    def put_one(self, uid, req_json):
        movie = self.get_one(uid)
        movie.title = req_json.get('title')
        movie.description = req_json.get('description')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')
        self.session.add(movie)
        self.session.commit()

    def get_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()




