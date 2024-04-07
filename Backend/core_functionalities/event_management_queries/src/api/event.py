from flask import Blueprint, jsonify
from ..queries.get_events import GetEventsQueryHandler
from ..queries.get_event import GetEventQueryHandler

event_blueprint = Blueprint('event', __name__)

@event_blueprint.route('/events', methods=['GET'])
def get_events():
    handler = GetEventsQueryHandler()
    events_data = handler.handle()
    return jsonify(events_data), 200

@event_blueprint.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    handler = GetEventQueryHandler()
    event_data = handler.handle(event_id)
    if not event_data:
        return jsonify({'error': 'Event not found'}), 404
    return jsonify(event_data), 200