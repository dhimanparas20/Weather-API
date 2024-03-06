from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from API import getWeather,getWeatherF

# Objects and imprtant variables
app = Flask(__name__)
api = Api(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
unitlst = ['C',"c","F","f"]

class Home(Resource):
    def get(self, city=None):
        query = request.args.get('city')
        current_domain = request.host_url
        if city:
            return (jsonify(getWeather(city=city)))
        if query:
            return (jsonify(getWeather(city=query)))
        return(jsonify({"message":"No city name Provided","syntax1":f"/api/weather/<City Name>","syntax2":f"/api/weather?city=<City Name>","Request Type":"GET","Examples":{"EG1":f"{current_domain}api/weather/Shimla","EG2":f"{current_domain}api/weather?city=Shimla","EG3":f"{current_domain}api/weatherf/171009","EG4":f"{current_domain}api/weatherf?city=171202"}}))
        
class HomeF(Resource):
    def get(self, city=None):
        query = request.args.get('city')
        current_domain = request.host_url
        if city:
            return (jsonify(getWeatherF(city=city)))
        if query:
            return (jsonify(getWeatherF(city=query)))
        return(jsonify({"message":"No city name Provided","syntax1":f"/api/weather/<City Name>","syntax2":f"/api/weather?city=<City Name>","Request Type":"GET","Examples":{"EG1":f"{current_domain}api/weather/Shimla","EG2":f"{current_domain}api/weather?city=Shimla","EG3":f"{current_domain}api/weatherf/171009","EG4":f"{current_domain}api/weatherf?city=171202"}}))
        
api.add_resource(HomeF, '/','/api/weather/','/api/weather/<city>',methods=['GET'])
api.add_resource(Home,'/api/weatherf/','/api/weatherf/<city>',methods=['GET'])

if __name__ == '__main__':
    app.run(debug=False,port=5000,host="0.0.0.0",threaded=True)
