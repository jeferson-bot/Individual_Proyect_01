from fastapi import FastAPI
import pandas as pd
# from services import developer_service
# from services import router as routes_router
# import sys
# sys.path.insert(0, '.\app\services')


app = FastAPI()

# app.include_router(routes_router)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/function/{desarrollador}")
def developer(desarrollador: str):

    df_steam_games_clean = pd.read_csv('..\datasets\df_steam_games_clean.csv', usecols=[
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
# def get_developer_info(desarrollador: str):
#     return developer_service.developer(desarrollador)


# print(developer("Valve"))

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
