from flask import Flask, request, render_template
from weather import get_current_weather
from waitress import serve

app = Flask(__name__) #Creates a flask app

""" @app.route("/") """ #Defines the route for the home page
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/weather.html")
def weather():
    city = request.args.get("city") #Gets the city from the query string and removes leading and trailing spaces
    weather_data = get_current_weather(city)
    #City not found by API
    if weather_data["cod"] != 200:
        return render_template(
            "./not_found.html", 
        )
    return render_template(
        ",/weather.html", 
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data["main"]["temp"]:.1f}",
        feels_like=f"{weather_data["main"]["feels_like"]:.1f}"
    )

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000) #Runs the app on port 8000 in Dev mode
    serve(app, host="0.0.0.0", port=8000)
    """ app.run(debug=True) """