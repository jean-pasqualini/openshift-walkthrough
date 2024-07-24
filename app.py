from flask import Flask, render_template
import random
import socket
import time

app = Flask(__name__)

exploding_kittens_cards = [
    {"name": "Nope", "image_url": "/static/images/nope.jpg"},
    {"name": "Defuse", "image_url": "/static/images/defuse.jpg"},
    {"name": "Garbage", "image_url": "/static/images/garbage.jpg"},
    {"name": "Personal attack", "image_url": "/static/images/personal-attack.jpg"},
    {"name": "Barking", "image_url": "/static/images/barking-kitten.jpg"},
    {"name": "Alter the future", "image_url": "/static/images/alter-the-future.jpg"},
    {"name": "See the Future", "image_url": "/static/images/see-the-future.jpg"}
]

@app.route('/card')
def get_card():
    card = random.choice(exploding_kittens_cards)
    hostname = socket.gethostname()
    return render_template('card.html', card=card, served_by=hostname)

# Route to consume memory
@app.route('/consume-memory')
def consume_memory():
    memory_hog = []
    try:
        for _ in range(100):  # Adjust the range for more or less memory consumption
            memory_hog.append(' ' * 10**6)  # Allocate 1 MB per iteration
        time.sleep(10)
    except MemoryError:
        return "Memory limit reached", 500
    return "Memory allocated successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
