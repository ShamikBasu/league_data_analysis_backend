from app.processing.epl_processing import epl_most_wins_by_seasons, epl_season_data_by_team, epl_teams_list


def get_epl_most_wins_by_seasons():
    return epl_most_wins_by_seasons()

def get_epl_season_data_by_team(team):
    return epl_season_data_by_team(team)

def get_epl_teams_list():
    return epl_teams_list()