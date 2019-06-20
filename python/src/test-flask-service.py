# --------------------------------------------------------------------------------------------------------------------
# <copyright file="test-flask-service.py" company="Microsoft">
#   2019 Microsoft Corporation
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
from flask import (Flask, jsonify, request, Response)
import json
import os
import sys
from azure.keyvault import KeyVaultClient
from msrestazure.azure_active_directory import MSIAuthentication, ServicePrincipalCredentials

#
# Flask variables and basic handlers
#
app = Flask(__name__)
keyVaultURL = os.environ["keyvaulturl"]

@app.errorhandler(500)
def error_handling(error):
    return "<html><body><h1>Danger Will Robinson!</h1><h2>%s</h2></body></html>" % str(error)

@app.errorhandler(404)
def error_handling(error):
    return "<html><body><h1>This is not the page you're looking for.</h1><h2>%s</h2></body></html>" % str(error)

@app.route("/hello", methods=["GET", "POST"])
def handleHello():
    try:

        # get credentials
        sys.stdout.write(keyVaultURL + "\n")
        credentials = MSIAuthentication(resource="https://vault.azure.net")

        # create a KeyVault client
        sys.stdout.write("before kv client\n")
        key_vault_client = KeyVaultClient(credentials)

        # get the secret
        sys.stdout.write("before secret\n")
        secret = key_vault_client.get_secret(
            keyVaultURL,    # Your KeyVault URL
            "hellomessage", # Name of your secret. If you followed the README 'secret' should exists
            ""              # The version of the secret. Empty string for latest
        )

        sys.stdout.write("after secret\n")
        message = secret.value
        res = jsonify({ "Message:" : message })

    except Exception as e:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        res = jsonify({ "Message:" : message})
        res.status_code = 500
    
    sys.stdout.flush()
    return res

#
# Server startup
#
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)