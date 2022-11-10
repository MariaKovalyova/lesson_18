from flask import request

from dao.model.models import Director
from utils import pagination


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 5))
        query = pagination(self.session.query(Director), page, page_size)
        return query.all()

    def get_one(self, uid):
        return self.session.query(Director).get(uid)
