
###
Module dependencies.
###
init = require("fb-custom-init")
nconf = require('nconf')
winston = require('winston')
express = require("express")
routes = require("./routes")
ws = require("./routes/webservice")
http = require("http")
path = require("path")
app = express()
magma_rendering = require('magma-rendering')

# all environments
app.set "port", 23088
app.set "views", __dirname + "/views"
app.set "view engine", "jade"
app.disable('x-powered-by')
app.use express.logger("dev")
app.use express.bodyParser()
app.use express.methodOverride()
#app.use express.cookieParser("your secret here")
#app.use express.session()
app.use app.router
app.use express.static(path.join(__dirname, "public"))

# development only
app.use express.errorHandler()  if "development" is app.get("env")

app.get "/", routes.index
app.get "/f/view.get/:id",magma_rendering.checkRequisite,
  magma_rendering.checkUserAuthorisation, ws.viewget
app.put "/f/view.put/:id",ws.viewput
app.post "/f/view.post/:id",ws.viewpost
app.delete "/f/view.del/:id",ws.viewdel


http.createServer(app).listen app.get("port"), ->
  console.log "Magma listening on port " + app.get("port")
