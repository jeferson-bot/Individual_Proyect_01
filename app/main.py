from fastapi import FastAPI
import pandas as pd


app = FastAPI()


@app.get("/function/{desarrollador}")
def developer(desarrollador: str):

    df_steam_games_clean = pd.read_csv('datasets/df_steam_games_clean.csv', usecols=[
                                       "release_date", "developer", "price"])

    df_games_developer = df_steam_games_clean[(
        df_steam_games_clean['developer'] == desarrollador)]

    df_free_games = df_games_developer[(df_games_developer['price'] == 0.00)]

    df_agrupacion = df_games_developer.groupby('release_date').count()

    df_agrupacion = df_agrupacion.reset_index()

    df_result = pd.DataFrame(
        columns=["Año", "Cantidad de items", "Contenido free"])

    df_result["Año"] = df_agrupacion["release_date"]

    df_result["Cantidad de items"] = df_agrupacion["developer"]

    for year in df_result["Año"]:

        try:
            free_content = df_free_games.groupby(
                'release_date').groups[year].shape[0]

            total_content = df_games_developer.groupby(
                'release_date').groups[year].shape[0]

            df_result.loc[df_result["Año"] == year,
                          "Contenido free"] = f"{round(free_content / total_content * 100, 2)}%"
        except:
            df_result.loc[df_result["Año"] == year, "Contenido free"] = "0%"

    return df_result.to_dict("list")


# @app.get("/best_developers/{year}")
# def best_developer_year(year: str):

# df_games = pd.read_csv("datasets/df_steam_games_clean.csv", columns=['release_date', 'id', 'developer'])
# df_user_reviews = pd.read_csv("datasets/df_user_reviews_clean.csv", columns=['user_id', 'item_id', 'recommend'])

# df = df_user_reviews.merge(df_games, left_on='item_id', right_on='id', how='inner')
# df = df[(df['release_date'] == year) & df['recommend']]
# top_developers = df.groupby('developer').size()

# # Check for errors
# if len(top_developers) < 3:
#     return {"error": f"Less than 3 developers published games in the year {year}."}
# if df.empty:
#     return {"error": f"No reviews found for the year {year}."}

# # Get top three developers
# top_developers = top_developers.nlargest(3).reset_index()

# # Create a list of dictionaries
# top_3 = [{f'Position {i+1}': dev} for i, dev in enumerate(top_developers['developer'])]

# return top_3


@app.get("/best_developers/{year}")
def best_developer_year(year: str):
    try:
        df_games = pd.read_csv(
            "datasets/df_steam_games_clean.csv", columns=['release_date', 'id', 'developer'])
        df_user_reviews = pd.read_csv(
            "datasets/df_user_reviews_clean.csv", columns=['user_id', 'item_id', 'recommend'])
    except FileNotFoundError:
        return {"error": "Data files not found"}

    # Validate year
    if not year.isdigit() or int(year) < 1900 or int(year) > 2100:
        return {"error": "Invalid year"}

    df = df_user_reviews.merge(
        df_games, left_on='item_id', right_on='id', how='inner')
    df = df[(df['release_date'] == year) & df['recommend']]
    top_developers = df.groupby('developer').size()

    # Check for errors
    if len(top_developers) < 3:
        return {"error": f"Less than 3 developers published games in the year {year}."}
    if df.empty:
        return {"error": f"No reviews found for the year {year}."}

    # Get top three developers
    top_developers = top_developers.nlargest(3).reset_index()

    # Create a list of dictionaries
    top_3 = [{f'Position {i+1}': dev}
             for i, dev in enumerate(top_developers['developer'])]

    return top_3.to_dict("list")
