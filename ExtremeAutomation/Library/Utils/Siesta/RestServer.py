import os
import ssl
import logging
import platform
import subprocess
from flask_cors import CORS
from RestServerConfig import RestServerConfig
from flask import Flask, request, abort, jsonify


########################################################################################################################
#   Configuration Variables   ##########################################################################################
########################################################################################################################
# Whether HTTPS should be used or not.
if isinstance(RestServerConfig.HTTPS, bool):
    HTTPS = RestServerConfig.HTTPS
else:
    HTTPS = False

# Private key location (only needed if HTTPS = True).
if hasattr(RestServerConfig, "PRIVATE_KEY_LOCATION"):
    PRIVATE_KEY_LOCATION = RestServerConfig.PRIVATE_KEY_LOCATION
else:
    PRIVATE_KEY_LOCATION = "ssl.key"

# Certificate location (only needed if HTTPS = True).
if hasattr(RestServerConfig, "CERTIFICATE_LOCATION"):
    CERTIFICATE_LOCATION = RestServerConfig.CERTIFICATE_LOCATION
else:
    CERTIFICATE_LOCATION = "ssl.cert"

########################################################################################################################
#   Global Variables   #################################################################################################
########################################################################################################################
LOG_LIST = ["test",
            "a",
            "b",
            "c"]


########################################################################################################################
#   API Versions   #####################################################################################################
########################################################################################################################
API_VERSION_1 = "v1"


########################################################################################################################
#   REST Server   ######################################################################################################
########################################################################################################################
app = Flask(__name__)

CORS(app)
OS = platform.system().lower()


########################################################################################################################
#   Server Routes   ####################################################################################################
########################################################################################################################
@app.route("/robot/<string:version>/install_netsight", methods=["POST"])
def install_netsight(version):
    if version == API_VERSION_1:
        if request.get_json() is None:
            abort(404, "Invalid JSON provided.")

        netsight_version = request.json["version"]

        output, error = start_netsight_install(netsight_version)

        app.logger.debug("Stdout from install: \n" + output)
        app.logger.debug("Stderr from install: \n" + error)
        app.logger.debug(request.remote_addr + " -> " + request.method + " -> " + request.full_path[:-1] + "\n")

        return jsonify({"output": output, "error": error})
    else:
        abort(404, "Invalid API version.")


@app.route("/robot/<string:version>/restart_netsight_and_redeploy_war_file", methods=["POST"])
def restart_netsight_and_redeploy_war_file(version):
    if version == API_VERSION_1:

        output, error = start_reset_deploy()

        app.logger.debug("Stdout from reset: \n" + output)
        app.logger.debug("Stderr from reset: \n" + error)
        app.logger.debug(request.remote_addr + " -> " + request.method + " -> " + request.full_path[:-1] + "\n")

        return jsonify({"output": output, "error": error})
    else:
        abort(404, "Invalid API version.")


@app.route("/robot/<string:version>/netsight_script_copy", methods=["POST"])
def netsight_script_copy(version):
    if version == API_VERSION_1:
        if request.get_json() is None:
            abort(404, "Invalid JSON provided.")

        script_name = request.json["script_name"]
        server_ip = request.json["server_ip"]
        script_directory = request.json["script_directory"]
        username = request.json["username"]
        password = request.json["password"]

        output, error = start_script_copy(server_ip, script_directory, script_name, username, password)

        app.logger.debug("Stdout from script copy: \n" + output)
        app.logger.debug("Stderr from script copy: \n" + error)
        app.logger.debug(request.remote_addr + " -> " + request.method + " -> " + request.full_path[:-1] + "\n")

        return jsonify({"output": output, "error": error})
    else:
        abort(404, "Invalid API version.")


@app.route("/robot/<string:version>/netsight_log_copy", methods=["POST"])
def netsight_log_copy(version):
    if version == API_VERSION_1:
        if request.get_json() is None:
            abort(404, "Invalid JSON provided.")

        guid = request.json['guid']
        test_engine_ip = request.json['test_engine_ip']
        test_engine_username = request.json['test_engine_username']
        test_engine_pw = request.json['test_engine_pw']
        log_name = request.json["log_name"]

        output, error = start_log_copy(guid, test_engine_ip, test_engine_username, test_engine_pw, log_name)

        app.logger.debug("Stdout from log copy: \n" + output)
        app.logger.debug("Stderr from log copy: \n" + error)
        app.logger.debug(request.remote_addr + " -> " + request.method + " -> " + request.full_path[:-1] + "\n")

        return jsonify({"output": output, "error": error})
    else:
        abort(404, "Invalid API version.")


@app.route("/robot/<string:version>/add_log", methods=["POST"])
def add_log(version):
    if version == API_VERSION_1:
        if request.get_json() is None:
            abort(404, "Invalid JSON provided.")

        log = request.json.get("log", None)

        if log:
            LOG_LIST.append(log)
            return jsonify(log)
        else:
            abort(404, "Invalid JSON provided.")
    else:
        abort(404, "Invalid API version.")


@app.route("/robot/<string:version>/read_log", methods=["GET"])
def read_log(version):
    if version == API_VERSION_1:
        if len(LOG_LIST) > 0:
            log = LOG_LIST.pop(0)
            return log
        return "log_empty"
    else:
        abort(404, "Invalid API version.")


@app.route("/robot/<string:version>/read_log_all", methods=["GET"])
def read_log_all(version):
    if version == API_VERSION_1:
        return jsonify(LOG_LIST)
    else:
        abort(404, "Invalid API version.")


@app.route("/robot/<string:version>", methods=["GET"])
def test_route(version):
    if version == API_VERSION_1:
        return jsonify("All good")
    return jsonify("Bad version, please use v1.")


########################################################################################################################
#   Netsight Utilities   ###############################################################################################
########################################################################################################################
def start_netsight_install(netsight_version):
    cmd = "python ../NetSightUtilities/NetSightInstaller.py " + netsight_version

    return start_sub_proc(cmd)


def start_reset_deploy():
    cmd = "python ../NetSightUtilities/NetSightResetRedeploy.py"

    return start_sub_proc(cmd)


def start_script_copy(server_ip, script_directory, script_name, username, password):
    cmd = ("python ../NetSightUtilities/NetSightScriptCopy.py " + server_ip + " " + script_directory + " " +
           script_name + " " + username + " " + password)

    return start_sub_proc(cmd)


def start_log_copy(guid, test_engine_ip, test_engine_username, test_engine_pw, log_name):
    cmd = ("python ../NetSightUtilities/NetSightLogCopy.py " + guid + " " + test_engine_ip + " " +
           test_engine_username + " " + test_engine_pw + " " + log_name)

    return start_sub_proc(cmd)


########################################################################################################################
#   Utilities   ########################################################################################################
########################################################################################################################
def string_to_boolean(boolean_string, default=True):
    """
    Converts boolean strings to a python boolean.
    Example "True" and "true" would be converted to True.
    The default option is used to set the boolean value when the passed string
    does not contain "True", "true", "False", or "false".

    """
    if str(type(boolean_string)) == "<type 'unicode'>":
        boolean_string = boolean_string.encode('utf8')

    if isinstance(boolean_string, str):
        if boolean_string.lower() == "true":
            boolean = True
        elif boolean_string.lower() == "false":
            boolean = False
        else:
            boolean = default
    elif isinstance(boolean_string, bool):
        boolean = boolean_string
    else:
        boolean = default

    return boolean


def configure_logger():
    if os.path.isfile("RestServer.log"):
        try:
            os.remove("RestServer.log")
        except OSError:
            pass

    formatter = logging.Formatter("%(asctime)s %(levelname)s; %(message)s")

    file_handler = logging.FileHandler("RestServer.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)


def get_shell():
    return False if platform.platform() == "windows" else True


def start_sub_proc(cmd):
    proc = subprocess.Popen(cmd, universal_newlines=True, shell=get_shell(),
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout = proc.stdout.read()
    stderr = proc.stderr.read()

    if "pydev" in stderr:
        stderr = "".join(stderr.splitlines()[1::])

    return stdout, stderr


########################################################################################################################
#   Main Function   ####################################################################################################
########################################################################################################################
if __name__ == '__main__':
    args = {"debug": True,
            "use_reloader": False,
            "host": "0.0.0.0"}

    if HTTPS:
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        try:
            context.load_cert_chain(CERTIFICATE_LOCATION, PRIVATE_KEY_LOCATION)
        except IOError:
            path = os.path.dirname(__file__)
            context.load_cert_chain(os.path.join(path, CERTIFICATE_LOCATION), os.path.join(path, PRIVATE_KEY_LOCATION))
        args["ssl_context"] = context
    configure_logger()
    app.run(**args)
