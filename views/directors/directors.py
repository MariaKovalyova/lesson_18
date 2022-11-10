from flask_restx import Resource, Namespace

from implemented import director_service

directors_ns = Namespace('directors')

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return director_service.get_directors(), 200


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        return director_service.get_director(uid), 200



