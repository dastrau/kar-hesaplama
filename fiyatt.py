from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    alis_fiyati = float(request.form['alis_fiyati'])
    satis_fiyati = float(request.form['satis_fiyati'])
    kargo_maliyeti = 30
    posetleme_maliyeti = 10
    reklam_maliyeti = 50

    # Komisyon ve hizmet bedeli oranlarını tanımlayın sadhg
    komisyon_orani = 0.23
    hizmet_bedeli_orani = 0.08

    # Kar hesaplama formülü
    kar = (satis_fiyati * (1 - komisyon_orani - hizmet_bedeli_orani)) - alis_fiyati - kargo_maliyeti - posetleme_maliyeti - reklam_maliyeti

    kar_yuzdesi = (kar / alis_fiyati) * 100

    # Sonucu ekrana yazdırın
    return render_template('index.html', kar=kar, kar_yuzdesi=kar_yuzdesi)

if __name__ == '__main__':
    app.run(debug=True)
