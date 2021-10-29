from flask import Flask, render_template, jsonify, request, abort

from flask_wtf import FlaskForm
import requests
from wtforms import SubmitField, StringField

from Apis.secrets_info import SECRET_KEY
from Apis.routes import TheGuardian

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

class SearchForm(FlaskForm):
    topic = StringField('Topic')
    submit = SubmitField('Search')


sections = ['World','Politics','Business','Opinion','Tech','Science','Health','Sports','Arts','Books',
            'Style','Food','Travel','Magazine','Video']

@app.route('/', methods=['POST', 'GET'])
def index():
    tg = TheGuardian()
    form = SearchForm()
    
    if request.method == 'GET':
        data = tg.latest_news()
        # return jsonify(data['response']['results'])
        return render_template("index.html", form=form, sections=sections, data=data['response']['results'])
        
    elif request.method == 'POST':
        if form.validate_on_submit():
            data = tg.search_by_topic(form.topic.data)
            return render_template("index.html", form=form, sections=sections, data=data['response']['results'])

    else:
        abort(404)

if __name__=='__main__':
    app.run(debug=True)

