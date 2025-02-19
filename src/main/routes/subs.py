from flask import Blueprint, jsonify, request


subs_route_bp = Blueprint("subs_route", __name__)

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.http_types.http_request import HttpRequest

from src.controllers.subscribers.subscribers_creator import SubscribeCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

@subs_route_bp.route("/subscriber", methods=["POST"])
def create_new_sub():
    subscribers_creator_validator(request)
    http_request = HttpRequest(
        body = request.json 
    )
    subs_repo = SubscribersRepository()
    subs_creator = SubscribeCreator(subs_repo)
    
    http_response = subs_creator.create(http_request)
    
    return jsonify(http_response.body), http_response.status_code