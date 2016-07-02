express = require("express")
___ = require("underscore")
___.mixin require("underscore.string")
mockcommunities = require("mockcommunities").mock
fs = require('fs');
domains = mockcommunities.domains
core = mockcommunities.core

Space = (spacename) ->
  @name = spacename
  @server_public_data = "http://localhost:3000"
  @server_private_data = "http://localhost:3000"
  @server_public_web = "http://localhost:3000"
  @server_private_web = "http://localhost:3000"
  @server_public_media = "http://localhost:3001"
  @public_id = @server_public_data + "/" + spacename + "/id"
  @public_history = @server_public_data + "/" + spacename + "/history"
  @public_schema = @server_public_data + "/" + spacename + "/schema"
  @public_data = @server_public_data + "/" + spacename + "/data"
  @public_media = @server_public_media + "/" + spacename
  @public_view = @server_public_data + "/" + spacename + "/view"
  @public_web = @server_public_web + "/" + spacename
  @private_history = @server_private_data + "/" + spacename + "/protected/history"
  @private_schema = @server_private_data + "/" + spacename + "/protected/schema"
  @private_data = @server_private_data + "/" + spacename + "/protected/data"
  @private_media = @server_private_data + "/" + spacename + "/protected/media"
  @private_view = @server_private_data + "/" + spacename + "/protected/view"
  @private_web = @server_private_web + "/" + spacename

ctx = space: new Space("flarebyte-marketplace")
public_id = "/" + ctx.space.name + "/id/"
public_data = "/" + ctx.space.name + "/data/"

#Main application
app = module.exports = express.createServer()

app.configure ->
  app.set "views", __dirname + "/views"
  app.set "view engine", "jade"
  app.use express.bodyParser()
  app.use express.methodOverride()
  app.use app.router
  app.use express.static(__dirname + "/public")

app.configure "development", ->
  app.use express.errorHandler(
    dumpExceptions: true
    showStack: true
  )

app.configure "production", ->
  app.use express.errorHandler()

app.listen 3000
console.log "Express server listening on port %d in %s mode", app.address().port, app.settings.env

#End main application

#Media application
mediaApp = module.exports.mediaApp = express.createServer()

mediaApp.configure ->
  mediaApp.set "views", __dirname + "/views"
  mediaApp.set "view engine", "jade"
  mediaApp.use express.bodyParser()
  mediaApp.use express.methodOverride()
  mediaApp.use mediaApp.router

mediaApp.configure "development", ->
  mediaApp.use express.errorHandler(
    dumpExceptions: true
    showStack: true
  )

mediaApp.configure "production", ->
  mediaApp.use express.errorHandler()

mediaApp.listen 3001
console.log "Express server listening on port %d in %s mode", mediaApp.address().port, mediaApp.settings.env

#End Media application

register303 = (domain) ->
  app.get public_id + domain + "/:id", (req, res) ->
    id = req.params.id
    res.writeHead 303,
      Location: public_data + domain + "/" + id + ".rdf"
      Vary: "Accept"

    res.end()

  app.get public_id + domain + "/:id/:subaction", (req, res) ->
    id = req.params.id
    subaction = req.params.subaction
    res.writeHead 303,
      Location: public_data + domain + "/" + id + "/" + subaction + ".rdf"
      Vary: "Accept"

    res.end()

  app.get public_id + domain, (req, res) ->
    res.writeHead 303,
      Location: public_data + domain + ".rdf"
      Vary: "Accept"

    res.end()

registerRdf = (domain) ->
  app.get public_data + domain.name + "/:id.rdf", (req, res) ->
    id = req.params.id
    r = domain.action_one(ctx, domain, id)
    res.contentType "application/json"
    res.send r

  app.get public_data + domain.name + "/" + domain.name + ":id/:subaction.rdf", (req, res) ->
    id = req.params.id
    subaction = req.params.subaction
    r = domain.action_sub[subaction](ctx, domain, id)
    res.contentType "application/json"
    res.send r

  app.get public_data + domain.name + ".rdf", (req, res) ->
    r = domain.action_many(ctx, domain)
    res.contentType "application/json"
    res.send r


app.get "/", (req, res) ->
  res.render "index",
    title: "Mock Marketplace"

i = 0
while i < domains.length
  register303 domains[i].name
  i++
i = 0

while i < domains.length
  registerRdf domains[i]
  i++

#Alias for DC subjects
#Expects http://localhost:30xx/:space/id/subject/?url=http://dbpedia.org/resource/Journal

app.get public_data + ":domain(alias)" + "/", (req, res) ->
  domain = req.params.domain
  subject = req.query.subject
  domain_obj = {"name":domain}
  r = {}
  r = core(r, ctx, domain_obj, Math.floor(Math.random() * 200))
  if subject
    r["subject"]=[subject]
    label = ___(subject).strRightBack("/")
    r["label"]=label
  res.contentType "application/json"
  res.send r

#Media app
mediaApp.get "/", (req, res) ->
  res.render "index",
    title: "Mock Media Marketplace"

mediaApp.get "/:space(flarebyte-marketplace)/markup/:category(all|default)/:id.md", (req, res) ->
  path = "./public/markup/ipsum.md"
  img = fs.readFileSync(path)
  res.writeHead(200, {'Content-Type': 'text/x-markdown' })
  res.end(img, 'binary')

#Nikon D200: aspect ratio 3:2
mediaApp.get "/:space(flarebyte-marketplace)/image/:category(all|default)/:id/:width_x_height(16x16|22x22|32x32|48x48|150x150|75x50|50x75|150x100|300x200|100x150|200x300|150x50)/:version.:extension(png)", (req, res) ->
  category=req.params.category
  id=req.params.id
  width_x_height=req.params.width_x_height
  version=req.params.version
  extension=req.params.extension
  imgname = "tree-diagramm"
  imgname = "samourai" if width_x_height in ["50x75","100x150","200x300"]
  imgname = "japan-head" if width_x_height in ["75x50","150x100","300x200"]
  imgname = "fb.logo" if id == "00001"
  path = "./public/images/mock/#{width_x_height}/#{imgname}.png"
  img = fs.readFileSync(path)
  res.writeHead(200, {'Content-Type': 'image/png' })
  res.end(img, 'binary')
