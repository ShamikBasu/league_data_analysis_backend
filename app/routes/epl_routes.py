from flask import Blueprint, send_file, jsonify

from app.handlers.epl_handlers import get_epl_most_wins_by_seasons, get_epl_season_data_by_team, get_epl_teams_list

epl_routes = Blueprint('epl_routes', __name__, url_prefix='/epl/')

@epl_routes.get("/list_of_teams/")
def get_epl_teams_list_route():
    res =[]
    res = get_epl_teams_list()
    return res

@epl_routes.get("/most_wins_by_seasons/")
def get_epl_most_wins_by_seasons_route():
    res = {}
    res = get_epl_most_wins_by_seasons()
    #print("TEST JSNOIFY",jsonify(res))
    return res

@epl_routes.get("/season_data/<team>")
def get_epl_season_data_by_team_route(team):
    res = {}
    res = get_epl_season_data_by_team(team)
    #print("TEST JSNOIFY",jsonify(res))
    return res