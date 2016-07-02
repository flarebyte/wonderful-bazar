express = require("express")
stylus = require("stylus")
fs = require("fs")
crypto = require('crypto')
___ = require("underscore")
___.mixin require("underscore.string")
controller = require("marketplace.generated.controller")
appsettings = require('flarebyte.settings')
web_hosting = appsettings.environment.web_hosting


#
# openssl genrsa -out private_market.pem 1024 
# openssl req -new -key private_market.pem -out certrequest.csr 
# openssl x509 -req -in certrequest.csr -signkey private_market.pem -out certificate_market.pem
#
ops_dir = "/Users/olivier/Dropbox/flarebyte.com-ltd/software development/node/ops"
ops_dir = process.env.FLAREBYTE_OPS
privateKey = fs.readFileSync("#{ops_dir}/marketplace/config/ssl/private_market.pem").toString();
certificate = fs.readFileSync("#{ops_dir}/marketplace/config/ssl/certificate_market.pem").toString();
credentials = crypto.createCredentials({key: privateKey, cert: certificate})
ssl_options = 
  key: privateKey
  cert: certificate

createMarketplaceServer = (port, options) ->
  
  if options
    app = express.createServer(options)
  else
    app = express.createServer()

  app.configure ->
    app.set "views", __dirname + "/views"
    app.set "view engine", "jade"
    app.use express.bodyParser()
    app.use express.methodOverride()
    app.use app.router
    app.use express.static(__dirname + "/public")
    app.use stylus.middleware(src: __dirname + "/public")

  app.configure "development", ->
    app.use express.errorHandler(
      dumpExceptions: true
      showStack: true
    )

  app.configure "production", ->
    app.use express.errorHandler()

  app.set "view engine", "jade"
  app.get "/", (req, res) ->
    res.render "index", title: "Express"
  controller.route(app)
  
  app.listen port
  console.log "Express server marketplace listening on port %d in %s mode", app.address().port, app.settings.env

#module.exports.publicMarketplaceApp = createMarketplaceServer(hosting.PORTS.HTTP,null)
#module.exports.privateMarketplaceApp = createMarketplaceServer(hosting.PORTS.HTTPS, ssl_options)

runServer= (space, edition, secure)->
  if secure
    createMarketplaceServer(web_hosting[space][edition].PORTS.HTTPS, ssl_options)
  else 
    createMarketplaceServer(web_hosting[space][edition].PORTS.HTTP,null)
    
module.exports=runServer


