#
# * Serve JSON to our AngularJS client
#
'use strict'

client = require('flaming-magma-client')

getUserContext= (req)->
  uctx=
    ownerRef: "email:magma.test.u1.77225432@flarebyte.com"
    universeId: "magma:f/universe/testing",
    verified: true
  return uctx


exports.name = (req, res) ->
  viewModel= client.g.lookup('magma:f/view.get/744550486')
  ctx=
    my: getUserContext req
    view: viewModel
    qs:
      path: "contacts"

  client.httpRequest ctx, (err, data)->
    res.send data
