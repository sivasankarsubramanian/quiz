from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

answers = {}

# 👉 Start route (optional but useful)
@app.route('/')
def home():
    return redirect(url_for('q1'))

# 💖 Questions

@app.route('/q1', methods=['GET','POST'])
def q1():
    if request.method == 'POST':
        answers['q1'] = request.form.get('q1')
        return redirect(url_for('q2'))
    return render_template('q1.html')

@app.route('/q2', methods=['GET','POST'])
def q2():
    if request.method == 'POST':
        answers['q2'] = request.form.get('q2')
        return redirect(url_for('q3'))
    return render_template('q2.html')

@app.route('/q3', methods=['GET','POST'])
def q3():
    if request.method == 'POST':
        answers['q3'] = request.form.get('q3')
        return redirect(url_for('q4'))
    return render_template('q3.html')

@app.route('/q4', methods=['GET','POST'])
def q4():
    if request.method == 'POST':
        answers['q4'] = request.form.get('q4')
        return redirect(url_for('q5'))
    return render_template('q4.html')

@app.route('/q5', methods=['GET','POST'])
def q5():
    if request.method == 'POST':
        answers['q5'] = request.form.get('q5')
        return redirect(url_for('q6'))
    return render_template('q5.html')

@app.route('/q6', methods=['GET','POST'])
def q6():
    if request.method == 'POST':
        answers['q6'] = request.form.get('q6')
        return redirect(url_for('q7'))
    return render_template('q6.html')

@app.route('/q7', methods=['GET','POST'])
def q7():
    if request.method == 'POST':
        answers['q7'] = request.form.get('q7')
        return redirect(url_for('q8'))
    return render_template('q7.html')

@app.route('/q8', methods=['GET','POST'])
def q8():
    if request.method == 'POST':
        answers['q8'] = request.form.get('q8')
        return redirect(url_for('q9'))
    return render_template('q8.html')

@app.route('/q9', methods=['GET','POST'])
def q9():
    if request.method == 'POST':
        answers['q9'] = request.form.get('q9')
        return redirect(url_for('q10'))
    return render_template('q9.html')

@app.route('/q10', methods=['GET','POST'])
def q10():
    if request.method == 'POST':
        answers['q10'] = request.form.get('q10')
        return redirect(url_for('result'))
    return render_template('q10.html')

# 💌 Result page
@app.route('/result')
def result():
    return render_template('result.html', answers=answers)

# 💍 Proposal page (FINAL)
@app.route('/proposal')
def proposal():
    return render_template('proposal.html')

# ▶️ Run app
if __name__ == '__main__':
    app.run(debug=True)