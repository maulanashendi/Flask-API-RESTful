from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__) # object flask
api = Api(app) # object flask_restful
CORS(app)

identitas = {}

class MembuatAPI(Resource):
    def get(self):
        # response = {"pesan" : "Aku lagi belajar membuat API"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form['umur']
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil dimasukkan"}
        return response

api.add_resource(MembuatAPI, "/api", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True,port=5005)