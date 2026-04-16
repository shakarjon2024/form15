from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form15', methods=['GET', 'POST'])
def form15():
    if request.method == 'POST':
        data = request.form.to_dict()
        data['qiziqishlar'] = request.form.getlist('qiziqish')
        return f"<h2>Barcha ma'lumotlar qabul qilindi!</h2><pre>{data}</pre><br><a href='/'>Orqaga</a>"
    return render_template('form15.html')

if __name__ == '__main__':
    app.run(debug=True)
