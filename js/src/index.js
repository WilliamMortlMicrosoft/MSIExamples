var http = require('http');
const KeyVault = require('azure-keyvault');
const msRestAzure = require("ms-rest-azure");
const port = 8080;
const vaultUri = "https://testflaskservicekv.vault.azure.net/";

http.createServer(function (request, response) {

    // login and get secret
    msRestAzure.loginWithMSI({resource: "https://vault.azure.net"}).then(function(credentials) {
        keyVaultClient = new KeyVault.KeyVaultClient(credentials);
        keyVaultClient.getSecret(vaultUri, "hellomessage", "").then(function(secretVal) {

            // build JSON
            jsonResponseObj = {secret: secretVal.value};
            jsonResponseStr = JSON.stringify(jsonResponseObj);

            // send the JSON
            response.writeHead(200, {'Content-Type': 'application/json'});
            response.end(JSON.stringify(jsonResponseStr));
        });
    });
}).listen(port);

console.log("Server running at http://localhost:%d", port);
