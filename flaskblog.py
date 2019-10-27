from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Moka',
        'title': 'Why I love sitting on the garden bed',
        'content': '''Sitting on the raised garden bed makes me feel like queen of the back yard''',
        'date_posted': '2019-10-27'
    },
    {
        'author': 'Moka',
        'title': 'What I think about the dog park',
        'content': '''I love the dark park because I can run around until
                      I get tired, while munching on leaves''',
        'date_posted': '2019-10-27'
    },
    {
        'author': 'Moka',
        'title': 'Why I bark at Karolina',
        'content': "Would you like her if she got duck poop on your bed?",
        'date_posted': '2019-10-27'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About Moka')


if __name__ == '__main__':
    app.run(debug=True)
