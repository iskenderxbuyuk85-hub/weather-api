from flask import Flask, jsonify, request

app = Flask(__name__)

sehirler = {
    "istanbul": {"sicaklik": 18, "durum": "Parçalı bulutlu"},
    "ankara": {"sicaklik": 16, "durum": "Açık"},
    "izmir": {"sicaklik": 24, "durum": "Güneşli"}
}

@app.route('/')
def ana():
    return {"api": "DEXRON Weather API", "developer": "@Dexronpy"}

@app.route('/hava')
def hava():
    sehir = request.args.get('sehir')
    if sehir and sehir.lower() in sehirler:
        veri = sehirler[sehir.lower()]
        return {
            "sehir": sehir.capitalize(),
            "sicaklik": veri["sicaklik"],
            "durum": veri["durum"],
            "developer": "@Dexronpy"
        }
    return {"hata": "Şehir bulunamadı", "developer": "@Dexronpy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
