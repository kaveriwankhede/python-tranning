from flask import Flask , render_template ,request ,flash ,redirect ,url_for
from Database import get_db, init_db
app = Flask(__name__)
app.secret_key='linkkiwi2026' #needed for flashing message
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

@app.route('/Add_Students', methods=['GET', 'POST'])
def Add_Students():

    if request.method == "POST":

        roll = request.form.get('roll_name')
        name = request.form.get('student_name')
        marks = request.form.get('marks')


        if not name or not marks:
            flash('Please provide both name and marks', 'danger')
            return render_template("Add_students.html")
        
        conn = get_db()
        conn.execute('''INSERT INTO SCORE
                     (ID,Student_name,total_marks) VALUES(?,?,?)''',
                     (roll, name, int(marks))
                     )
        conn.commit()
        conn.close()

        new_student = {
            'name':name,
            'roll_no':roll,
            'marks':int(marks),
        }

        stud.append(new_student)
        #flash massage display        flash(f"Student name : {name} Added successfully!","success")
        print(f"Received Student: {name}")
        print(f"Updated Student List: {stud}")
        return redirect(url_for('students'))

    return render_template('Add_students.html')



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

@app.route('/MCQ_C_lang', methods=['POST'])
def MCQ_C_lang():
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')

    score = 0

    if q1 == "Dennis Ritchie":
        score += 1

    if q2 == ";":
        score += 1

    if q3 == "printf()":
        score += 1

    return render_template("result.html", score=score)

@app.route('/MCQ_Cpp_lang', methods=['POST'])
def MCQ_Cpp_lang():

    score = 0

    if request.form.get('q1') == "Programming Language":
        score += 1

    if request.form.get('q2') == "Bjarne Stroustrup":
        score += 1

    if request.form.get('q3') == "::":
        score += 1

    return render_template("result.html", score=score)

@app.route('/MCQ_Java', methods=['POST'])
def MCQ_Java():

    score = 0

    if request.form.get('q1') == "Programming Language":
        score += 1

    if request.form.get('q2') == "main()":
        score += 1

    if request.form.get('q3') == "new":
        score += 1

    return render_template('result.html', score=score)

@app.route('/MCQ_Python', methods=['POST'])
def MCQ_Python():

    score = 0

    if request.form.get('q1') == "Programming Language":
        score += 1

    if request.form.get('q2') == "def":
        score += 1

    if request.form.get('q3') == "str":
        score += 1

    return render_template('result.html', score=score)

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
    init_db()
    app.run(debug=True)

    