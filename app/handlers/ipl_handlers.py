from app.processing.ipl_processing import \
    ipl_player_debut_by_year_team, \
    ipl_player_debuts_over_year, \
    ipl_debutant_players_name_by_year, ipl_teams_200_score_matches_first_innings, \
    ipl_teams_200_score_matches_second_innings


def hello_world():
    return 'Hello, World from my_handlers!'

def another_route():
    return 'This is another route from my_handlers!'

def get_ipl_player_debut_by_year_team(year):
    return ipl_player_debut_by_year_team(year)

def get_ipl_player_debuts_over_year():
    return ipl_player_debuts_over_year()

def get_ipl_debutant_players_name_by_year(year):
    return ipl_debutant_players_name_by_year(year)

def get_ipl_matches_with_200_score_first_innings():
    return ipl_teams_200_score_matches_first_innings()
def get_ipl_matches_with_200_score_second_innings():
    return ipl_teams_200_score_matches_second_innings()