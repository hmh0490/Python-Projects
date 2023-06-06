# flask, Django are web frameworks = managers of multiple web pages
from flask import Flask, render_template
import pandas as pd

# good practice to use __name__ special variable
app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

# the main website's url will end with /home or /
# @ symbol makes the line a decorator, it decorates the function below it
# web framework managing which htm is displayed and when via route method
@app.route("/")
def home():
    # under main folder there should be a templates folder
    return render_template("home.html", data=stations.to_html())

# put station, date variables in tags
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df[ '    DATE']== date][ '   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    # rest api should return dictionary or list by records
    result = df.to_dict(orient="records")
    return result

# "/api/v1/<station>/<year>" would be interpreted the same as
# "/api/v1/<station>/<date>" -> add yearly subdirectory
@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df[ '    DATE'].astype(str)
    # rest api should return dictionary or list by records
    result = df[df[ '    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result

"""
@app.route("/about/")
def about():
    # under main folder there should be a templates folder
    return render_template("about.html")
"""

# only run the website if script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
# we can see errors on the webpage
# if we are running multiple apps parallel and port 5000 is occupied,
# change the port number, eg. app.run(debug=True, port=5001)