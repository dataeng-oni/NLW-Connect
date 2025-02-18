from flask import Blueprint, jsonify, request


event_route_bp = Blueprint("event_route0", __name__)

from src.validators.events_creator_validator import events_creator_validator

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    events_creator_validator(request)
    http_request = HttpRequest(
        body = request.json 
    )
    
    http_response = HttpResponse(
        body= http_request.body,
        status_code= 201
    )
    return jsonify(http_response.body), http_response.status_code