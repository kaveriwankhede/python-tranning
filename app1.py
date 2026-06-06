from flask import Flask , render_template ,request
app = Flask(__name__)
stud=[
    {
        'name':'John Doe',
        'roll_no':1001,
        'marks':90,
    },
    {
        'name':'Jane Smith',
        'roll_no':1002,
        'marks':22,
    },
    {
        'name':'Alice Johnson',
        'roll_no':1003,
        'marks':19,
    },
    {
        'name':'Bob Brown',
        'roll_no':1004,
        'marks':21,
    }
]
@app.route('/')
def Home():
    return render_template('Home.html',students=stud)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/students')
def students():
    return render_template('students.html', students=stud)

@app.route('/Subject')
def Subject():
    return render_template('Subject.html')

@app.route('/Theory')
def Theory():
    return render_template('Theory.html')

@app.route('/MCQ')
def MCQ():
    return render_template('MCQ.html')

@app.route('/Result')
def Result():
    score = 0

    # Correct Answers
    if request.form.get('q1') == "Programming Language":
        score += 1

    if request.form.get('q2') == "def":
        score += 1

    if request.form.get('q3') == "str":
        score += 1

    percentage = (score / 3) * 100

    return render_template(
        'result.html',
        score=score,
        percentage=percentage
    )
    #return render_template('Result.html')

if __name__ == '__main__':
    app.run(debug=True)

    