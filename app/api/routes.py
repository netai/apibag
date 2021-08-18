from .resources import api_test


def api_routes(blueprint):
    blueprint.add_url_rule('/test', endpoint='api_test', view_func=api_test, methods=["GET"])