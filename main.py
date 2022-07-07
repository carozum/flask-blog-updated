from operator import indexOf
from flask import Flask, render_template, request
import requests
import smtplib


data_url = "https://api.npoint.io/f209a61f7d71c019f3da"
blog_response = requests.get(data_url)
all_posts = blog_response.json()

app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template('index.html')

@app.route('/blog')
def get_blog():    
    return render_template('blog.html',
                           all_posts = all_posts)
    
@app.route('/post/<int:post_index>')
def get_post(post_index):
    return render_template('post.html', 
                           all_posts = all_posts,
                           post_id = post_index )

@app.route('/contact', methods=['POST', 'GET'])
def get_contact():
    msg_sent = False
    if request.method == 'POST':
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['phone'])
        print(request.form['message'])
        msg_sent= True
    return render_template('contact.html', msg_sent = msg_sent)

# @app.route('/form-entry', methods=['POST'])
# def receive_data():
#     print(request.form['name'])
#     print(request.form['email'])
#     print(request.form['phone'])
#     print(request.form['message'])
#     return render_template('form-entry.html')

def send_email(name, email, phone, message):
    # see day 32 of 100 days of code
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login('bla@hotmail.fr','password' )
        connection.sendmail('bla@hotmail.fr', email , email_message)

@app.route('/datas')
def get_datas():
    return render_template('datas.html')


if __name__ == '__main__':
    app.run(debug=True)