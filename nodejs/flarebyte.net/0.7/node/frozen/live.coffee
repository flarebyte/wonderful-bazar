init = require("fb-custom-init")
nconf = require('nconf')
winston = require('winston')
http = require("http")
appli = require("frozen-appli")
living = require("./routes/living")

cloudLogger = init.cloudLogger

app = appli.configure(13608,__dirname,"live")
port = app.get("port")

app.get "/:relurl(*)", living.index
http.createServer(app).listen port, ->
  cloudLogger.info(
    "app":"frozen"
    "variant":"live"
    "event":"EVT37987733"
    "msg":"Frozen server (live) listening on port #{port}"
    )
