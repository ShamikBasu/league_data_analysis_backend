import pandas as pd
def filter_data_set_by_year(df,year):
    #Converting date field to datetime type
    df['Date'] = pd.to_datetime(df['Date'])
    # Filter rows where the year in 'Date' is 2008
    df_year = df[df['Date'].dt.year == year]
    # Print the filtered DataFrame (optional)
    df_year.head()
    return df_year

def filter_matches_by_team(df,team):
  """Filters a DataFrame to include only matches where at least one team is 'Kolkata Knight Riders'.
  Args:
      df (pandas.DataFrame): The DataFrame containing match data.

  Returns:
      pandas.DataFrame: A new DataFrame containing only matches where KKR is a playing team.
  """
  # Split 'Teams' column into separate teams (assuming "vs" as separator)
  df[['Team1', 'Team2']] = df['Teams'].str.split(' vs ', expand=True)
  # Filter rows where at least one team is "Kolkata Knight Riders"
  team_matches = df[(df['Team1'].str.lower() == team.lower()) | (df['Team2'].str.lower() == team.lower())]
  return team_matches

def filter_matches_by_200(df,innings):
    df[innings+'INT'] = df[innings].astype(int)
    matches_200_score = df[(df[innings+'INT'] > 199)]
    return len(matches_200_score)