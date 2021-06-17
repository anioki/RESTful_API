from flask import jsonify, make_response

from datetime import datetime as dt

from models.actor import Actor
from models.movie import Movie
from settings.constants import ACTOR_FIELDS  # to make response pretty
from .parse_request import get_request_data


def get_all_actors():
    """
    Get list of all records
    """
    all_actors = Actor.query.all()
    actors = []
    for actor in all_actors:
        act = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        actors.append(act)
    return make_response(jsonify(actors), 200)


def get_actor_by_id():
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

        obj = Actor.query.filter_by(id=row_id).first()
        try:
            actor = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def add_actor():
    """
    Add new actor
    """

    data = get_request_data()
    if 'name' in data.keys() and 'gender' in data.keys() and 'date_of_birth' in data.keys():
        try:
            data_actor = {'name': data['name'][0], 'gender': data['gender'][0],
                          'date_of_birth': dt.strptime(data['date_of_birth'][0], '%d.%m.%Y').date()}
        except:
            err = 'Something is wrong in your data'
            return make_response(jsonify(error=err), 400)
        new_record = Actor.create(**data_actor)
        new_actor = {k: v for k, v in new_record.__dict__.items() if k in ACTOR_FIELDS}
        return make_response(jsonify(new_actor), 200)
    else:
        err = 'No data specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def update_actor():
    """
    Update actor record by id
    """
    ### YOUR CODE HERE ###
    data = get_request_data()
    for key in data.keys():
        if key != 'id' and key != 'name' and key != 'gender' and key != 'date_of_birth':
            err = 'Some of your key are wrong'
            return make_response(jsonify(error=err), 400)
    if 'id' in data.keys():
        try:
            actor = Actor.query.filter_by(id=data['id'][0]).first()
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
        if 'name' in data.keys():
            try:
                data_actor = {'name': data['name'][0], 'gender': actor.gender,
                              'date_of_birth': actor.date_of_birth}
            except:
                err = 'Something is wrong in your data'
                return make_response(jsonify(error=err), 400)
            try:
                upd_record = Actor.update(data['id'][0], **data_actor)
            except:
                err = 'Actor with such name was already exist'
                return make_response(jsonify(error=err), 400)
        if 'gender' in data.keys():
            try:
                data_actor = {'name': actor.name, 'gender': data['gender'][0],
                              'date_of_birth': actor.date_of_birth}
            except:
                err = 'Something is wrong in your data'
                return make_response(jsonify(error=err), 400)
            try:
                upd_record = Actor.update(data['id'][0], **data_actor)
            except:
                err = 'Something is wrong'
                return make_response(jsonify(error=err), 400)
        if 'date_of_birth' in data.keys():
            try:
                data_actor = {'name': actor.name, 'gender': actor.gender,
                              'date_of_birth': dt.strptime(data['date_of_birth'][0], '%d.%m.%Y').date()}
            except:
                err = 'Something is wrong in your data'
                return make_response(jsonify(error=err), 400)
            try:
                upd_record = Actor.update(data['id'][0], **data_actor)
            except:
                err = 'Something is wrong'
                return make_response(jsonify(error=err), 400)
        try:
            upd_actor = {k: v for k, v in upd_record.__dict__.items() if k in ACTOR_FIELDS}
            return make_response(jsonify(upd_actor), 200)
        except:
            err = 'No data specified'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No data specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def delete_actor():
    """
    Delete actor by id
    """
    ### YOUR CODE HERE ###
    data = get_request_data()
    if 'id' in data.keys():
    # use this for 200 response code
        try:
            Actor.delete(data['id'][0])
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
        msg = 'Record successfully deleted'
        return make_response(jsonify(message=msg), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def add_actor_relations():
    """
    Add a movie to actor's filmography
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    # use this for 200 response code
    if 'id' in data.keys() and 'relation_id' in data.keys():
        try:
            movie = Movie.query.filter_by(id=data['relation_id'][0]).first()
            actor = Actor.add_relation(data['id'][0], movie) # add relation here
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
        rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        rel_actor['filmography'] = str(actor.filmography)
        return make_response(jsonify(rel_actor), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def actor_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    # use this for 200 response code
    if 'id' in data.keys():
        try:
            actor = Actor.clear_relations(data['id'][0])# clear relations here
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
        rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        rel_actor['filmography'] = str(actor.filmography)
        return make_response(jsonify(rel_actor), 200)
    else: 
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###