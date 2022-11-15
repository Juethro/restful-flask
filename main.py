from flask import Flask, request
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

Kalimat = ["Makan patty itu! Spongebob", "Ayo Spongebob, berdansalah selagi bisa", "Lari Patrick!",
           "Jangan menangis Spongebob", "Aku pergi bekerja Patrick", "Pemujaan yang berlebihan itu tidak baik, Spongebob",
           "Patrick, kenapa harus ada matahari tenggelam di hari yang sempurna?", "Ternyata semua yang berkilau belum tentu emas, Spongebob",
           "Jangan makan kue pie itu, Spongebob!", "Patrick! hari ini aku akan mengalahkanmu!" ]

def randomkali(kali):
    return random.choice(Kalimat)

class Home(Resource):
    def get(self):
        return randomkali(Kalimat), 200
    
    def post(self):
        if request.get_json() == None:
            return randomkali(Kalimat), 200
        elif request.get_json() != None:
            json = request.get_json()
            Nama = json["nama"]
            return "Selamat datang, {}, anda berhasil masuk ke Puja Kerang Ajaib".format(Nama.capitalize()), 200
        else:
            return "error", 400


class Login(Resource):
    def get(self, name):
        kalii = randomkali(Kalimat)
        if kalii.find("Patrick") != -1:
            final_kali = kalii.replace("Patrick", name.capitalize())
            return final_kali, 200
        elif kalii.find("Spongebob") != -1:
            final_kali = kalii.replace("Spongebob", name.capitalize())
            return final_kali, 200


api.add_resource(Home, '/')
api.add_resource(Login, '/<name>')

if __name__ == "__main__":
    app.run(host='0.0.0.0')