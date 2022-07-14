var admin = require("firebase-admin");

var serviceAccount = require("/Users/seonghwa/Downloads/realcoding.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

module.exports = admin;