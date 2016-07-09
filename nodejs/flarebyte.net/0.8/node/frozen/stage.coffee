init = require("fb-custom-init")
nconf = require('nconf')
winston = require('winston')

http = require("http")
appli = require("frozen-appli")
staging = require("./routes/staging")

cloudLogger = winston.loggers.get('cloud')

app = appli.configure(12509,__dirname,"stage")

port = app.get("port")

p1 = ":bizkey([a-z0-9]{16})"
p2 = ":bizid(biz-[a-z0-9-]{3,30})"
p3= ":pjkey([a-z0-9]{16})"
p4= ":pjid(pjt-[0-9-]{7})"

app.get "/", staging.index
app.get "/#{p1}/#{p2}/#{p3}/#{p4}/:relurl(*)", staging.preview
http.createServer(app).listen port, ->
  cloudLogger.info("Frozen server (Stage) listening on port #{port}")
