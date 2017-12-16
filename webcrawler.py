from flask import Flask,render_template
from db import DB

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#@app.route('/about')
#def about():
#    return render_template('index.html')

@app.route('/news')
def about():
    x = DB()
    news = x.read_news()
    return render_template('index.html', news=news)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)    

if __name__=='__main__':
    app.run()
