#!/usr/bin/python
from flask import Flask, request, abort, jsonify
from ExtremeAutomation.Library.Utils.CloudConnect.CloudConnectRoutes import CloudConnectRoutes


app = Flask(__name__)
des3_key = \
    "/home/administrator/SQA_ROBOT_AUTOMATION/ExtremeAutomation/Library/Utils/CloudConnect/cloudconnect_selfsigned.key"
des3_cert = \
    "/home/administrator/SQA_ROBOT_AUTOMATION/ExtremeAutomation/Library/Utils/CloudConnect/cloudconnect_selfsigned.crt"
cc_route = CloudConnectRoutes()
device_ips = {}


########################################################################################################################
#   Server Routes   ####################################################################################################
########################################################################################################################
@app.route('/Clients/device/v1/discovery', methods=["GET"])
def init():
    # Reply with 404 to start CloudConnect on Client.
    abort(404)


@app.route('/Clients/device/v1/switch/<string:serial>/connect', methods=["PUT"])
def connect(serial):
    device_ips[serial] = request.remote_addr
    request.get_json()
    response = cc_route.connect(serial)
    if response:
        return jsonify(response)
    return abort(404)


@app.route('/Clients/device/v1/switch/<string:serial>/imageupgrade', methods=["PUT"])
def image_upgrade(serial):
    device_ips[serial] = request.remote_addr
    request.get_json()
    response = cc_route.image_upgrade(serial, request.json)
    if response:
        return jsonify(response)
    return abort(404)


@app.route('/Clients/device/v1/switch/<string:serial>/configuration', methods=["PUT"])
def configuration(serial):
    device_ips[serial] = request.remote_addr
    request.get_json()
    response = cc_route.configuration(serial, request.json)
    if response:
        return jsonify(response)
    return abort(404)


@app.route('/Clients/device/v1/switch/<string:serial>/event', methods=["POST"])
def event_notify(serial):
    device_ips[serial] = request.remote_addr
    request.get_json()
    if cc_route.event_notify(serial, request.json):
        return jsonify(success=True)
    return abort(404)


@app.route('/Clients/device/v1/switch/<string:serial>/stats', methods=["PUT"])
def stats_notify(serial):
    device_ips[serial] = request.remote_addr
    request.get_json()
    response = cc_route.stats_notify(serial, request.json)
    if response:
        return jsonify(response)
    return abort(404)


@app.route('/<path:filename>')
def catch_all_for_new_routes(filename):
    request.get_json()
    json_dict = request.json
    cc_route.logger.log_info("LOGGING: Got unexpected route from DUT:")
    cc_route.logger.log_info(filename)
    cc_route.logger.log_info([item for item in json_dict])
    return jsonify(success=True)


########################################################################################################################
#   Configuration Routes   #############################################################################################
########################################################################################################################
@app.route('/robot_config/allow_timeout', methods=["POST"])
def configure_timeout():
    request.get_json()
    if cc_route.configure_timeout(request.json):
        return jsonify(success=True)
    return abort(404)


@app.route('/robot_config/connect', methods=["POST"])
def configure_connect():
    request.get_json()
    if cc_route.configure_connect(request.json):
        return jsonify(success=True)
    return abort(404)


@app.route('/robot_config/upgrade', methods=["POST"])
def configure_upgrade():
    request.get_json()
    if cc_route.configure_upgrade(request.json):
        return jsonify(success=True)
    return abort(404)


@app.route('/robot_config/config', methods=["POST"])
def configure_config():
    request.get_json()
    if cc_route.configure_config(request.json):
        return jsonify(success=True)
    return abort(404)


@app.route('/robot_config/connect', methods=["GET"])
def inspect_connect():
    request.get_json()
    result = cc_route.inspect_connect(request.json)
    if result:
        return jsonify(result)
    return abort(404)


@app.route('/robot_config/upgrade', methods=["GET"])
def inspect_upgrade():
    request.get_json()
    result = cc_route.inspect_upgrade(request.json)
    if result:
        return jsonify(result)
    return abort(404)


@app.route('/robot_config/stats', methods=["POST"])
def configure_stats():
    request.get_json()
    if cc_route.configure_stats(request.json):
        return jsonify(success=True)
    return abort(404)


@app.route('/robot_config/device_states', methods=["GET"])
def get_device_states():
    request.get_json()
    result = cc_route.get_device_states(request.json)
    if result:
        return jsonify(result)
    return abort(404)


@app.route('/robot_config/clear_fsm_states', methods=["POST"])
def clear_fsm_states():
    request.get_json()
    result = cc_route.clear_fsm_states(request.json)
    if result:
        return jsonify(result)
    return abort(404)


@app.route('/robot_config/get_mgmt_ip', methods=["GET"])
def get_mgmt_ip():
    request.get_json()
    result = cc_route.get_mgmt_ip(request.json, device_ips)
    if result:
        return jsonify(result)
    return abort(404)


@app.route('/robot_config/get_device_assets', methods=["GET"])
def get_device_assests():
    request.get_json()
    result = cc_route.get_device_assests(request.json)
    if result:
        return jsonify(result)
    return abort(404)


########################################################################################################################
#   Main Function   ####################################################################################################
########################################################################################################################
if __name__ == '__main__':
    args = {"debug": True,
            "use_reloader": False,
            "host": "0.0.0.0",
            "port": 8443,
            "ssl_context": (des3_cert, des3_key)}

    app.run(**args)
