import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import io

from app.processing.helper import filter_data_set_by_year, filter_matches_by_team, filter_matches_by_200


def clean_data():
    player_info_df = pd.read_csv("D:/Machine_Learning/Datasets/IPL/IPL/Players_Info_2024.csv")
    player_info_df.info()
    player_info_df = player_info_df.dropna(subset=['IPL Debut'])
    player_info_df['IPL Debut'] = player_info_df['IPL Debut'].astype(int)
    return player_info_df

def ipl_player_debuts_over_year():
    player_info_df = clean_data()
    val_count = player_info_df['IPL Debut'].value_counts()  # Sort by IPL Debut year
    val_count = val_count.sort_index()
    # Create a count plot using the sorted dataframe
    sns.countplot(x="IPL Debut", data=player_info_df)
    # Rotate x-axis labels for better readability with many years
    plt.xticks(rotation=45)  # Adjust rotation as needed

    # Add labels and title
    plt.xlabel("IPL Debut Year")
    plt.ylabel("Number of Players")
    plt.title("Player Debuts in IPL")

    # Annotate count on top of each bar using enumerate and offset
    for i, (year, count) in enumerate(val_count.items()):
        plt.text(i, count + 0.1, str(count), ha='center', va='center', fontsize=12)  # Adjust ha and va as needed

    # Show the plot
    #plt.show()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Clear the plot to release memory
    plt.close()
    # Show the plot
    # plt.show()
    return buffer
def ipl_player_debut_by_year_team(year):
    player_info_df = clean_data()
    # Filter players who debuted in 2008
    filtered_data = player_info_df[player_info_df['IPL Debut'] == int(year)]

    # Check if there's any data for 2008 debut
    if filtered_data.empty:
        print("No players found who debuted in IPL 2008.")
    else:
        # Choose the plot type (consider options and data suitability)
        # Option 1: Scatter plot (shows individual data points)
        # sns.scatterplot(x="Team Name", y="Player Nationality", data=filtered_data)

        # Option 2: Bar chart (shows team-wise distribution)
        sns.countplot(x="Team Name", hue="Player Nationality", data=filtered_data)

        # Customize the plot (optional)
        plt.xlabel("Team Name")
        plt.ylabel("Player count")  # Adjust based on plot type
        title = "Players Debuting in IPL "+year
        plt.title(title)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        # Clear the plot to release memory
        plt.close()
        # Show the plot
        #plt.show()
        return buffer

def ipl_debutant_players_name_by_year(year):
    player_info_df = clean_data()
    players_2008 = player_info_df[player_info_df['IPL Debut'] == int(year)]  # Filter players
    # Check if there's any data for 2008 debut
    if players_2008.empty:
        print("No players found who debuted in IPL 2008.")
    else:
        # Choose a plot type (consider data suitability)

        # Option 1: Bar chart with informative tooltip (using hvplot - optional)
        # If you have hvplot installed, uncomment this section

        # p = (players_2008.hvplot.bar(
        #   x="Team Name", y="Player Name", hover_data=["Player Name", "Team Name"], title="IPL 2008 Debuts"
        # ))
        # p.opts(tools="hover")  # Enable hover tool for tooltip display
        # hvplot.show(p)

        # Option 2: Customized scatter plot with team colors and legend
        sns.set_style("whitegrid")  # Set background style (optional)
        plt.figure(figsize=(10, 6))  # Adjust figure size (optional)
        team_colors = {
            'CSK': 'yellow', 'DC': 'blue', 'MI': 'skyblue', 'GT': 'teal',
            'LSG': 'orange', 'RCB': 'red', 'KKR': 'purple', 'PBKS': 'red',  # Consider a different red shade for PBKS
            'RR': 'pink', 'SRH': 'orange'
        }  # Define team colors (replace with actual team names and colors)
        sns.scatterplot(
            x="Team Name",
            y="Player Name",
            hue="Team Name",
            palette=team_colors,  # Apply team colors
            data=players_2008,
            size="IPL Debut",  # Adjust point size based on debut year (optional)
            alpha=0.7,  # Set transparency (optional)
        )
        plt.xlabel("Team Name")
        plt.ylabel("Player Name")
        plt.title(f"IPL {year} Debuts")
        plt.legend(title="Team")  # Add legend for team colors

        # Rotate player names for better readability (optional)
        plt.xticks(rotation=45)

        # Show the plot
        plt.tight_layout()  # Adjust spacing between elements (optional)
        #plt.show()
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        # Clear the plot to release memory
        plt.close()
        # Show the plot
        # plt.show()
        return buffer

def ipl_teams_win_record_over_years(team):
    ipl_team_perf_df = pd.read_csv("D:/Machine_Learning/Datasets/IPL/IPL/team_performance_dataset_2008to2024.csv")
    fin_dict = {}
    #print(ipl_team_perf_df.info())
    for year in range(2008,2024):

        year_df = filter_data_set_by_year(ipl_team_perf_df,year)

        df_copy = filter_matches_by_team(year_df.copy(),team)
        team_wins_case_insensitive = (df_copy['Match_Winner'].str.lower() == team.lower()).sum()
        fin_dict[str(year)] = str(team_wins_case_insensitive)

    ##fin_dict['team_name'] = team
    print(fin_dict)
    return fin_dict

def ipl_teams_200_score_matches_first_innings():
    ipl_team_perf_df  = pd.read_csv("D:/Machine_Learning/Datasets/IPL/IPL/team_performance_dataset_2008to2024.csv")
    fin_dict={}
    for year in range(2008,2024):
        year_df = filter_data_set_by_year(ipl_team_perf_df,year)
        matches_200_score = filter_matches_by_200(year_df,'First_Innings_Score')
        fin_dict[str(year)] = str(matches_200_score)

    return fin_dict

def ipl_teams_200_score_matches_second_innings():
    ipl_team_perf_df  = pd.read_csv("D:/Machine_Learning/Datasets/IPL/IPL/team_performance_dataset_2008to2024.csv")
    fin_dict={}
    ipl_team_perf_df['Second_Innings_Score'] = ipl_team_perf_df['Second_Innings_Score'].fillna("0")
    for year in range(2008,2024):
        year_df = filter_data_set_by_year(ipl_team_perf_df,year)
        matches_200_score = filter_matches_by_200(year_df,"Second_Innings_Score")
        fin_dict[str(year)] = str(matches_200_score)

    return fin_dict
