from flask import Flask
from flask import jsonify

import docker
import json

client = docker.from_env()

app = Flask(__name__)
app.run(debug=True)

@app.route('/container/list')
def get_containers():
    container_list = []
    containers = client.containers.list()
    for container in containers:
        #print(container.stats(stream=False))
        app.logger.info('This is logger container stats %s', container.stats(stream=False))
        container_list.append({"name":container.name, "status": container.status, "id": container.id})
    return jsonify(container_list)

@app.route('/image/list')
def get_images():
    image_list = []
    images = client.images.list()
    for image in images:
        image_list.append({"id":image.id, "labels": image.labels})
    return jsonify(image_list)

@app.route('/network/list')
def get_networks():
    networks_list = []
    networks = client.networks.list()
    for network in networks:
        networks_list.append({"id":network.id, "name": network.name})
    return jsonify(networks_list)

@app.route('/volume/list')
def get_volumes():
    volume_list = []
    volumes = client.volumes.list()
    for volume in volumes:
        volume_list.append({"id":volume.id, "name": volume.name})
    return jsonify(volume_list)

    