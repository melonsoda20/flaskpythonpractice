from flask import Flask, render_template, url_for, request


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
        data = request.form.to_dict()
        print(data)
        return 'Form submitted!'

    else:
        return 'Something went wrong'

