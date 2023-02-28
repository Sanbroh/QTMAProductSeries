from flask import Flask, session, render_template, Response, request, request, url_for, flash, redirect

app = Flask(__name__)
appName = "QTMA Product Series"
pageName = ""

app.config['SECRET_KEY'] = 'AF92AF84692AE0661B1CE20B'

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'},
            {'title': 'Message Three',
             'content': 'Message Three Content'},
            ]

@app.route('/', methods=('GET', 'POST'))
def index():
    # if request.method == 'POST':
    #     if request.form.get('btn-fs') == 'FULL_STACK':
    #         pageName = "Full-Stack Development"
    #     elif request.form.get('btn-do') == 'DATA_OPTIMIZATION':
    #         pageName = "Data Optimization"
    #     else:
    #         pass
    # elif request.method == 'GET':
    #     return render_template('index.html', appName=appName)
    return render_template('index.html')

@app.route('/fullstack', methods=('GET', 'POST'))
def fullstack():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title and not content:
            flash('Title and content are empty!')
        elif not title:
            flash('Title is empty!')
        elif not content:
            flash('Content is empty!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('fullstack'))
    return render_template('fullstack.html', appName=appName, messages=messages)

@app.route('/dataop', methods=('GET', 'POST'))
def dataop():
    return render_template('dataop.html', appName=appName)

if __name__ == "__main__":
  app.run(debug=True)
