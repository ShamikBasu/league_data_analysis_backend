import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import io
import json
def get_winner(row):
    """
    This function takes a row from the dataframe and returns the winner or "draw".
    """
    home_goals = row["FTHG"]
    away_goals = row["FTAG"]
    if home_goals > away_goals:
        return row["HomeTeam"]
    elif home_goals < away_goals:
        return row["AwayTeam"]
    else:
        return "Draw"

def epl_teams_list():
    epl_results_df = pd.read_csv("D:/Machine_Learning/Datasets/epl/results.csv", encoding='windows-1252')
    unique_home_teams = epl_results_df['HomeTeam'].unique()
    # Convert the Series to a list
    home_team_list = unique_home_teams.tolist()
    # Print the list of unique home teams
    print(home_team_list)
    return home_team_list

def epl_most_wins_by_seasons():
    epl_results_df = pd.read_csv("D:/Machine_Learning/Datasets/epl/results.csv", encoding='windows-1252')
    epl_results_df["winner"] = epl_results_df.apply(get_winner, axis=1)
    filtered_df = epl_results_df[epl_results_df['winner'] != 'Draw']

    # Group by season and sort by wins in descending order
    season_winners = (filtered_df.groupby('Season')['winner']
                      .value_counts()
                      .to_frame(name='wins')
                      .reset_index()
                      .sort_values(by=['Season', 'wins'], ascending=[True, False]))

    # Get winners with most wins each season
    top_winners_per_season = season_winners.groupby('Season').apply(lambda x: x.iloc[0])

    # Convert to dictionary
    season_wins = top_winners_per_season.to_dict('records')

    # Print the JSON output
    print(json.dumps(season_wins))
    return season_wins

def epl_season_data_by_team(team):
    epl_results_df = pd.read_csv("D:/Machine_Learning/Datasets/epl/results.csv", encoding='windows-1252')
    epl_results_df["winner"] = epl_results_df.apply(get_winner, axis=1)
    team_df = epl_results_df[
        (epl_results_df['HomeTeam'] == team) | (epl_results_df['AwayTeam'] == team)]

    # Group by season and calculate counts
    season_stats = (team_df.groupby('Season')
                    .size()
                    .to_frame(name='played')
                    .reset_index())
    season_stats['wins'] = team_df[team_df['winner'] == team].groupby('Season').size().reset_index(
        drop=True)
    season_stats['draws'] = team_df[team_df['winner'] == 'Draw'].groupby('Season').size().reset_index(
        drop=True)
    season_stats['losses'] = season_stats['played'] - season_stats['wins'] - season_stats['draws']

    # Convert to dictionary
    season_stats_dict = season_stats.to_dict('records')

    # Print the JSON output
    print(json.dumps(season_stats_dict))
    return season_stats_dict