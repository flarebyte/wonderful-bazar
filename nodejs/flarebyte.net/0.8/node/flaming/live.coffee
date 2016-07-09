###
GENERATED - DO NOT EDIT - Tue Jan 14 2014 22:25:31 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
###

'use strict'

###
Module dependencies.
###
express = require("express")
init = require("fb-custom-init")
nconf = require("nconf")
winston = require("winston")
routes = require("./routes")
api = require("./routes/api")
http = require("http")
path = require("path")
_ = require("lodash")
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


# Boolean value - true/false
RE_BOOLEAN_VALUE= /[TF]/
# Routing

app.get '/api/profile', (req, res)->
  # List all profiles for the current user
  if _.isEmpty req.query
    api.doListAllProfile(req, res)
    return
  res.send(404)
app.get '/api/login', (req, res)->
  # List all login options for the current user
  if _.isEmpty req.query
    api.doListAllLoginOptions(req, res)
    return
  res.send(404)
app.get '/api/compose', (req, res)->
  # List all compose templates for the current user
  if _.isEmpty req.query
    api.doListAllComposeTemplates(req, res)
    return
  res.send(404)
app.get '/api/to-read', (req, res)->
  # List all messages to read for the current user
  if _.isEmpty req.query
    api.doListAllMessagesToRead(req, res)
    return
  res.send(404)
app.get '/api/to-do', (req, res)->
  # List all tasks to do for the current user
  if _.isEmpty req.query
    api.doListAllTasksToDo(req, res)
    return
  res.send(404)
app.get '/api/important', (req, res)->
  # List all important messages for the current user
  if _.isEmpty req.query
    api.doListAllImportantMessages(req, res)
    return
  res.send(404)
app.get '/api/recent', (req, res)->
  # List all recent messages for the current user
  if _.isEmpty req.query
    api.doListAllRecentMessages(req, res)
    return
  res.send(404)
app.get '/api/shared', (req, res)->
  # List all shared messages for the current user
  if _.isEmpty req.query
    api.doListAllSharedMessages(req, res)
    return
  res.send(404)
app.get '/api/all', (req, res)->
  # List all messages for the current user
  if _.isEmpty req.query
    api.doListAllMessages(req, res)
    return
  res.send(404)
app.get '/api/news', (req, res)->
  # List all news for the current user
  if _.isEmpty req.query
    api.doListAllNews(req, res)
    return
  res.send(404)
app.get '/api/trash', (req, res)->
  # List all trash for the current user
  if _.isEmpty req.query
    api.doListAllTrash(req, res)
    return
  res.send(404)
app.get '/api/dashboard', (req, res)->
  # List all dashboards of the current user
  if _.isEmpty req.query
    api.doListAllDashboards(req, res)
    return
  res.send(404)
app.get '/api/contacts', (req, res)->
  isImportant= RE_BOOLEAN_VALUE.test(req.query.important)
  isSpam= RE_BOOLEAN_VALUE.test(req.query.spam)
  isAccepted= RE_BOOLEAN_VALUE.test(req.query.accepted)
  # List a selection of contacts of the current user
  if isImportant and isSpam and isAccepted
    api.doListASelectionOfContacts(req, res)
    return
  # List all contacts of the current user
  if _.isEmpty req.query
    api.doListAllContacts(req, res)
    return
  res.send(404)
app.get '/api/settings', (req, res)->
  # List all settings of the current user
  if _.isEmpty req.query
    api.doListAllSettings(req, res)
    return
  res.send(404)
app.get '/api/help', (req, res)->
  # List all help items of the current user
  if _.isEmpty req.query
    api.doListAllHelpItems(req, res)
    return
  res.send(404)
app.get '/api/faq', (req, res)->
  # List all faq items of the current user
  if _.isEmpty req.query
    api.doListAllFaqItems(req, res)
    return
  res.send(404)
app.get '/api/privacy', (req, res)->
  # List all privacy items of the current user
  if _.isEmpty req.query
    api.doListAllPrivacyItems(req, res)
    return
  res.send(404)
app.get '/api/terms', (req, res)->
  # List all terms for the current user
  if _.isEmpty req.query
    api.doListAllTerms(req, res)
    return
  res.send(404)


http.createServer(app).listen app.get("port"), ->
  console.log "Express server listening on port " + app.get("port")

