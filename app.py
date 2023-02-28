from flask import Flask, session, render_template, Response, request, request, url_for, flash, redirect

app = Flask(__name__)
appName = "QTMA Product Series"

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        logo = request.form['logo']
        length = request.form['length']

        if not prompt:
            flash('Prompt is required!')
        elif not logo:
            flash('Logo is required!')
        elif not length:
            flash('Time is required!')
        else:
            length = int(re.search(r'\d+', length).group())
            length = (length - 2) * 40

            script = make_script(prompt, length, api_key)
            slides = get_slide_points(script, api_key)
            long_script = write_script_to_single_page(script)
            img_url = generate_logo(logo, api_key)
            print("Processing")
            return render_template('product.html', appName=appName, slides=slides, script=script, long_script=long_script, img_url=img_url)

    elif request.method == 'GET':
        return render_template('index.html', appName=appName)

    return render_template('index.html')

@app.route('/product/', methods=('GET', 'POST'))
def product():
    return render_template('product.html', appName=appName, slides=slides, script=script, long_script=long_script, img_url=img_url)

if __name__ == "__main__":
  app.run(debug=True)
