from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Moka',
        'title': 'Why I love sitting on the garden bed',
        'content': '''Sitting on the raised garden bed makes me feel like queen
                      of the back yard''',
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password',
                  'danger')
    return render_template('login.html', title='Login', form=form)
