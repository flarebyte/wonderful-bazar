###
Module dependencies.
###
express = require("express")
init = require("fb-custom-init")
nconf = require('nconf')
winston = require('winston')
routes = require("./routes")
api = require("./routes/api")
http = require("http")
path = require("path")
app = express()

# all environments
app.set "port", 17017
app.set "views", __dirname + "/views"
app.set "view engine", "jade"
app.use express.favicon()
app.use express.logger("dev")
app.use express.bodyParser()
app.use express.methodOverride()
app.use express.cookieParser("hGu$!jSlbjD7GwMjF3?hyQU)%1(JSO")
app.use express.session(secret: "mozillapersona")
app.use app.router
app.use require("stylus").middleware(__dirname + "/public")
app.use express.static(path.join(__dirname, "public"))

# development only
app.use express.errorHandler()  if "development" is app.get("env")
app.get '/', routes.index
app.get '/partials/:name', routes.partials

app.get '/api/name', api.name

http.createServer(app).listen app.get("port"), ->
  console.log "Express server listening on port " + app.get("port")
