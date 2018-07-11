from flask import Flask
from flask import jsonify
import docker

from resources.container import Container
from resources.volume import Volume
from resources.network import Network
from resources.image import Image


client = docker.from_env()
app = Flask(__name__)
app.run(debug=True)

@app.route('/container/list')
def get_containers():
    try:
        container = Container(client)
        container_list = container.all()
        return jsonify(container_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
@app.route('/image/list')
def get_images():
    try:
        image = Image(client)
        image_list = image.all()
        return jsonify(image_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/network/list')
def get_networks():
    try:
        network = Network(client)
        network_list = network.all()
        return jsonify(network_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/volume/list')
def get_volumes():
    try:
        volume = Volume(client)
        volume_list = volume.all()
        return jsonify(volume_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500