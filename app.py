from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    
    data = {}
    data[name] = []
    data[name].append({
    'age': age,
    'gender': gender
    })

    filename = name + '.txt'
    filepath = './data/' + filename
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile)

    return data

if __name__ == '__main__':
    app.run()