from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def kalkulator():
    return render_template('kalkulator.html')

@app.route('/post', methods = ['POST'])
def hitung():
    bil1 = int(request.form['Bilangan1'])
    bil2 = int(request.form['Bilangan2'])
    if bil1<bil2:
        smaller = bil1
    else:
        smaller = bil2
    for i in range (1,smaller+1):
        if bil1%i==0 and bil2%i==0:
            fpb=i
    kpk=int((bil1 * bil2) /fpb)
    print(fpb)
    print(kpk)
    return redirect(url_for('hasil', FPB=fpb, KPK=kpk))

@app.route('/hasil/<int:FPB>/<int:KPK>')
def hasil(FPB, KPK):
    return render_template('hasil.html', FPB=str(FPB), KPK=str(KPK))

if __name__ == "__main__":
    app.run(debug=True)