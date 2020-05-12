from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

extension = '.html'


@app.route('/')
def home():
    return render_template('index' + extension)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name + extension)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        ##turns retrieved data from POST into a dictionary
        data = request.form.to_dict()
        return redirect('/thankyou')

    else:
        return 'Something went wrong'
