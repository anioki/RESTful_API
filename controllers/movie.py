from flask import jsonify, make_response

from ast import literal_eval

from models.actor import Actor
from models.movie import Movie
from settings.constants import MOVIE_FIELDS
from .parse_request import get_request_data


def get_all_movies():
    """
    Get list of all records
    """
    all_movies = Movie.query.all()
    movies = []
    for movie in all_movies:
        act = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        movies.append(act)
    return make_response(jsonify(movies), 200)

def get_movie_by_id():
    """
    Get record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'][0])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Movie.query.filter_by(id=row_id).first()
        try:
            movie = {k: v for k, v in obj.__dict__.items() if k in MOVIE_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(movie), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def add_movie():
    """
    Add new actor
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    print(data)
    # use this for 200 response code
    if 'name' in data.keys() and 'year' in data.keys() and 'genre' in data.keys():
        try:
            data_movie = {'name': data['name'][0], 'genre': data['genre'][0],
                          'year': int(data['year'][0])}
        except:
            err = 'Something is wrong in your data'
            return make_response(jsonify(error=err), 400)
        new_record = Movie.create(**data_movie)
        new_movie = {k: v for k, v in new_record.__dict__.items() if k in MOVIE_FIELDS}
        return make_response(jsonify(new_movie), 200)
    ### END CODE HERE ###
    else:
        err = 'No data specified'
        return make_response(jsonify(error=err), 400)


def update_movie():
    """
    Update actor record by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    if 'name' in data.keys() and 'year' in data.keys() and 'genre' in data.keys():
        try:
            data_movie = {'name': data['name'][0], 'genre': data['genre'][0],
                          'year': int(data['year'][0])}
        except:
            err = 'Something is wrong in your data'
            return make_response(jsonify(error=err), 400)
        # use this for 200 response code
        if 'id' in data.keys():
            try:
                upd_record = Movie.update(data['id'][0], **data_movie)
            except:
                err = 'Record with such id does not exist or movie with such name was already exist'
                return make_response(jsonify(error=err), 400)
            upd_movie = {k: v for k, v in upd_record.__dict__.items() if k in MOVIE_FIELDS}
            return make_response(jsonify(upd_movie), 200)
        else:
            err = 'No id specified'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No data specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def delete_movie():
    """
    Delete movie by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    if 'id' in data.keys():
    # use this for 200 response code
        try:
            Movie.delete(data['id'][0])
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
        msg = 'Record successfully deleted'
        return make_response(jsonify(message=msg), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def add_movie_relations():
    """
    Add a movie to actor's filmography
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    # use this for 200 response code
    if 'id' in data.keys() and 'relation_id' in data.keys():
        try:
            actor = Actor.query.filter_by(id=data['relation_id'][0]).first()
            movie = Movie.add_relation(data['id'][0], actor)# add relation here
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
        rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        rel_movie['cast'] = str(movie.cast)
        return make_response(jsonify(rel_movie), 200)
    else:
        err = 'No data specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def movie_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    # use this for 200 response code
    if 'id' in data.keys():
        try:
            movie = Movie.clear_relations(data['id'][0])# clear relations here
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
        rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        rel_movie['cast'] = str(movie.cast)
        return make_response(jsonify(rel_movie), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###