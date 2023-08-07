from flask import Flask, render_template, request, redirect, url_for, flash

'''
Это сайт интернет магазина секс товаров для взрослых.
'''

app = Flask(__name__)
#создаём главную страницу
@app.route('/')
def home():
    menu_items = [
        {'label': 'Главная', 'url': '/'},
        {'label': 'О нас', 'url': '/about'},
        {'label': 'Контакты', 'url': '/contact'}
    ]
    return render_template('home.html', title='Моя веб-страница', menu_items=menu_items)



if __name__ == '__main__':
    app.run(debug= True, host = '127.0.0.1', port = 5000)