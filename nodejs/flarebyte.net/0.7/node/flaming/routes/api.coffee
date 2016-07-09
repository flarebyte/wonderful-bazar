###
GENERATED - DO NOT EDIT - Tue Jan 14 2014 22:25:31 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
###

'use strict'

client = require('flaming-magma-client')

getUserContext= (req)->
  uctx=
    ownerRef: "email:magma.test.u1.77225432@flarebyte.com"
    universeId: "magma:f/universe/testing",
    verified: true
  return uctx



# List all profiles for the current user
exports.doListAllProfile= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all login options for the current user
exports.doListAllLoginOptions= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all compose templates for the current user
exports.doListAllComposeTemplates= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all messages to read for the current user
exports.doListAllMessagesToRead= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all tasks to do for the current user
exports.doListAllTasksToDo= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all important messages for the current user
exports.doListAllImportantMessages= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all recent messages for the current user
exports.doListAllRecentMessages= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all shared messages for the current user
exports.doListAllSharedMessages= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all messages for the current user
exports.doListAllMessages= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all news for the current user
exports.doListAllNews= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all trash for the current user
exports.doListAllTrash= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all dashboards of the current user
exports.doListAllDashboards= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List a selection of contacts of the current user
exports.doListASelectionOfContacts= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all contacts of the current user
exports.doListAllContacts= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all settings of the current user
exports.doListAllSettings= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all help items of the current user
exports.doListAllHelpItems= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all faq items of the current user
exports.doListAllFaqItems= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all privacy items of the current user
exports.doListAllPrivacyItems= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

# List all terms for the current user
exports.doListAllTerms= (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data

