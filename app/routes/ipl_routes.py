# app/routes/my_routes.py
from flask import Blueprint, send_file, jsonify
from app.handlers.ipl_handlers import hello_world, another_route, get_ipl_player_debut_by_year_team, \
    get_ipl_player_debuts_over_year, get_ipl_debutant_players_name_by_year, \
    get_ipl_matches_with_200_score_first_innings, get_ipl_matches_with_200_score_second_innings
from app.processing.ipl_processing import ipl_teams_win_record_over_years
import json
# Create a Blueprint
#ipl_routes = Blueprint('routes', __name__)
ipl_routes = Blueprint('ipl_routes', __name__, url_prefix='/ipl/')
@ipl_routes.route('/')
def hello_world_route():
    return hello_world()

@ipl_routes.route('/another')
def another_route_route():
    return another_route()
@ipl_routes.route('/get_debutants_by_year/')
@ipl_routes.route('/get_debutants_by_year/<year>')
def get_ipl_player_debut_by_year_team_route(year=None):
    #print(type(year))
    buffer = ""
    if year:
        buffer = get_ipl_player_debut_by_year_team(year)
    else:
        buffer = get_ipl_player_debuts_over_year()
    return send_file(buffer, mimetype='image/png')
@ipl_routes.route("/get_debutant_names_by_year/<year>")
def get_ipl_debutant_players_name_by_year_route(year):
    buffer = get_ipl_debutant_players_name_by_year(year)
    return send_file(buffer, mimetype='image/png')

@ipl_routes.route("/get_team_wins_over_year/<team>")
def ipl_teams_win_record_over_years_route(team):
    res = ipl_teams_win_record_over_years(team)
    #print("TEST JSNOIFY",jsonify(res))
    return res
@ipl_routes.route("/get_200_scores/<innings>")
def ipl_matches_with_200_score(innings):

    res = {}
    if innings == "first_innings":
        res = get_ipl_matches_with_200_score_first_innings()
    else:
        res = get_ipl_matches_with_200_score_second_innings()
    #print("TEST JSNOIFY",jsonify(res))
    return res
