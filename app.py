from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Завантаження секретного ключа
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY', 'some_secret_key')

# Дані для різних розділів
collections_data = [
    {'name': 'Осінь-Зима 2024', 'designer': 'Samar Yarik', 'description': 'Колекція в стилі ретро з сучасним відтінком'},
    {'name': 'Весна-Літо 2024', 'designer': 'Kuznetsov Vladis', 'description': 'Легкі матеріали та яскраві кольори'},
    {'name': 'Класика', 'designer': 'Git Champ Kostya', 'description': 'Елегантна колекція з акцентом на класичні форми'},
    {'name': 'Спортивний стиль', 'designer': 'Буруля Василь', 'description': 'Комфорт та стиль для активного способу життя'},
]

designers_data = [
    {'name': 'Gucci', 'country': 'Італія', 'description': 'Відомий італійський бренд з екстравагантними дизайнами'},
    {'name': 'Chanel', 'country': 'Франція', 'description': 'Французький модний дім, що асоціюється з класичною елегантністю'},
    {'name': 'Prada', 'country': 'Італія', 'description': 'Італійський бренд, відомий своїми мінімалістичними дизайнами'},
]

shows_data = [
    {'name': 'Paris Fashion Week', 'date': '2024-10-10', 'location': 'Париж, Франція'},
    {'name': 'New York Fashion Week', 'date': '2024-09-15', 'location': 'Нью-Йорк, США'},
    {'name': 'Milan Fashion Week', 'date': '2024-09-20', 'location': 'Мілан, Італія'},
]

reviews_data = [
    {'brand': 'Louis Vuitton', 'review': 'Елегантні та якісні аксесуари для будь-якого сезону'},
    {'brand': 'Dior', 'review': 'Вражаючий дизайн та бездоганна якість'},
    {'brand': 'Prada', 'review': 'Сміливі кольори та унікальні форми у кожній колекції'},
]

# Маршрути для відображення даних
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/designers')
def designers():
    return render_template('designers.html', designers=designers_data)


@app.route('/collections')
def collections():
    return render_template('collections.html', collections=collections_data)


@app.route('/shows')
def shows():
    return render_template('shows.html', shows=shows_data)


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', reviews=reviews_data)


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/consultation')
def consultation():
    return render_template('consultation.html')


# Ендпойнт для отримання повідомлення з консультації (REST API)
@app.route('/api/consultation', methods=['POST'])
def api_consultation():
    data = request.get_json()  # Отримуємо JSON дані від користувача
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone_number = data.get('phone_number')

    # Виводимо інформацію в термінал
    print(f"Консультація запит від: {first_name} {last_name}, Номер телефону: {phone_number}")

    return jsonify({'status': 'success', 'message': 'Ваше повідомлення отримано!'})

@app.route('/api/designers', methods=['POST'])
def api_add_designer():
    data = request.get_json()  # Отримуємо JSON дані від користувача
    name = data.get('name')
    bio = data.get('bio')
    image = data.get('image')

    # Додаємо інформацію про дизайнера в список
    designers_data.append({
        'name': name,
        'bio': bio,
        'image': image  # Переконайтеся, що цей ключ завжди є
    })

    return jsonify({'status': 'success', 'message': 'Дизайнера успішно додано!'})

@app.route('/api/designers/<string:name>', methods=['DELETE'])
def api_delete_designer(name):
    global designers_data
    designers_data = [designer for designer in designers_data if designer['name'] != name]

    return jsonify({'status': 'success', 'message': 'Дизайнера успішно видалено!'})

if __name__ == '__main__':
    app.run(debug=True)
