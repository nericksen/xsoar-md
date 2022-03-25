import flask
from flask import request, jsonify 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/<ip>/json', methods=['GET'])
def api_all(ip):
    ip_info = {
        "anycast": True,
        "city": "Los Angeles",
        "country": "US",
        "hostname": "one.one.one.one",
        "ip": ip,
        "lat": 34.0522,
        "lng": -118.2437,
        "loc": "34.0522,-118.2437",
        "org": "AS13335 Cloudflare, Inc.",
        "postal": "90084",
        "readme": "https://ipinfo.io/missingauth",
        "region": "California",
        "timezone": "America/Los_Angeles"
    }
    return jsonify(ip_info)


app.run(host="0.0.0.0")
