___ = require("underscore")
___.mixin require("underscore.string")
scheduler = require("flarebyte.scheduler")
ldrest = require("flarebyte.ldrest")
#TODO: unhardcode localhost or mock
exports.createGetJsonMessage_should_work = (test) ->
  ctx = {"any":"stuff","journal":[],"data": {}}
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["http://localhost:3000/flarebyte-marketplace/id/offering/offering0"])
    test.deepEqual(ctx.journal[0],["ok","getJsonUri","200","url: http://localhost:3000/flarebyte-marketplace/id/offering/offering0"])
    test.deepEqual(ctx.any,"stuff")
    test.deepEqual(ctx.data._root_.about,"http://localhost:3000/flarebyte-marketplace/id/offering/offering0")
    test.done()
  downloadJsonMessage = ldrest.createGetJsonMessage(ctx,"$.data","_root_","http://localhost:3000/flarebyte-marketplace/id/offering/offering0")
  scheduler.executeTask(downloadJsonMessage, schedulerTask)

exports.createGetTextMarkupMessage_should_work = (test) ->
  ctx = {"any":"stuff","journal":[], "data": {}}
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["http://localhost:3001/flarebyte-marketplace/markup/all/0.md"])
    test.deepEqual(ctx.journal[0],["ok","getTextMarkupUri","200","url: http://localhost:3001/flarebyte-marketplace/markup/all/0.md"])
    test.deepEqual(ctx.any,"stuff")
    test.ok(___.includes(ctx.data._root_,"not considering the asterisk"))
    test.done()
  downloadTextMarkupMessage = ldrest.createGetTextMarkupMessage(ctx,"$.data","_root_","http://localhost:3001/flarebyte-marketplace/markup/all/0.md")
  scheduler.executeTask(downloadTextMarkupMessage, schedulerTask)

exports.createGetJsonMessage_invalid_url_should_be_tolerated = (test) ->
  ctx = {"any":"stuff","journal":[],"data": {}}
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["http://localhost:5000/flarebyte-marketplace/id/offering/offering0"])
    test.deepEqual(ctx.journal[0],["ko","getJsonUri","0","url: http://localhost:5000/flarebyte-marketplace/id/offering/offering0"])
    test.deepEqual(ctx.any,"stuff")
    test.deepEqual(ctx.data._root_,null)
    test.done()
  downloadJsonMessage = ldrest.createGetJsonMessage(ctx,"$.data","_root_","http://localhost:5000/flarebyte-marketplace/id/offering/offering0")
  scheduler.executeTask(downloadJsonMessage, schedulerTask)

exports.createGetJsonMessage_404_url_should_be_tolerated = (test) ->
  ctx = {"any":"stuff","journal":[],"data": {}}
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["http://localhost:3000/flarebyte-marketplace/id/Zoffering/offering0"])
    test.deepEqual(ctx.journal[0],["ko","getJsonUri","404","url: http://localhost:3000/flarebyte-marketplace/id/Zoffering/offering0"])
    test.deepEqual(ctx.any,"stuff")
    test.deepEqual(ctx.data._root_,null)
    test.done()
  downloadJsonMessage = ldrest.createGetJsonMessage(ctx,"$.data","_root_","http://localhost:3000/flarebyte-marketplace/id/Zoffering/offering0")
  scheduler.executeTask(downloadJsonMessage, schedulerTask)

exports.createGetTextMarkupMessage_invalid_url_should_be_tolerated = (test) ->
  ctx = {"any":"stuff","journal":[], "data": {}}
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["http://localhost:5001/flarebyte-marketplace/markup/all/0.md"])
    test.deepEqual(ctx.journal[0],["ko","getTextMarkupUri","0","url: http://localhost:5001/flarebyte-marketplace/markup/all/0.md"])
    test.deepEqual(ctx.any,"stuff")
    test.deepEqual(ctx.data._root_,null)
    test.done()
  downloadTextMarkupMessage = ldrest.createGetTextMarkupMessage(ctx,"$.data","_root_","http://localhost:5001/flarebyte-marketplace/markup/all/0.md")
  scheduler.executeTask(downloadTextMarkupMessage, schedulerTask)

exports.createGetTextMarkupMessage_404_url_should_be_tolerated = (test) ->
  ctx = {"any":"stuff","journal":[], "data": {}}
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["http://localhost:3001/flarebyte-marketplace/Zmarkup/all/0.md"])
    test.deepEqual(ctx.journal[0],["ko","getTextMarkupUri","404","url: http://localhost:3001/flarebyte-marketplace/Zmarkup/all/0.md"])
    test.deepEqual(ctx.any,"stuff")
    test.deepEqual(ctx.data._root_,null)
    test.done()
  downloadTextMarkupMessage = ldrest.createGetTextMarkupMessage(ctx,"$.data","_root_","http://localhost:3001/flarebyte-marketplace/Zmarkup/all/0.md")
  scheduler.executeTask(downloadTextMarkupMessage, schedulerTask)

exports.createGetJsonMessagesFromFilter_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "data":
      "_root_":
        "availableAtOrFrom": "http://flarebyte.com/001"
        "hasWarrantyPromise": "http://flarebyte.com/002"
        "comments": ["http://flarebyte.com/003","http://flarebyte.com/004"]
        "outbounds":null
        "body":"http://flarebyte.com/005"
        
  jpathFilterTable = [
    ["$.data._root_.availableAtOrFrom","json"],
    ["$.data._root_.hasWarrantyPromise","json"],
    ["$.data._root_.stats","json"],
    ["$.data._root_.comments","json"],
    ["$.data._root_.outbounds","json"],
    ["$.data._root_.creator","json"],
    ["$.data._root_.typeOfGood","json"],
    ["$.data._root_.body","markup"],
    ]
  
  downloadMessages = ldrest.createGetMessagesFromFilter(ctx,jpathFilterTable)
  test.ok(downloadMessages.length==5)
  test.deepEqual(downloadMessages[0].taskParams,["$.data._root_","_availableAtOrFrom_","http://flarebyte.com/001"])
  test.deepEqual(downloadMessages[1].taskParams,["$.data._root_","_hasWarrantyPromise_","http://flarebyte.com/002"])
  test.deepEqual(downloadMessages[2].taskParams,["$.data._root_._comments_",0,"http://flarebyte.com/003"])
  test.deepEqual(downloadMessages[3].taskParams,["$.data._root_._comments_",1,"http://flarebyte.com/004"])
  test.deepEqual(downloadMessages[4].taskParams,["$.data._root_","_body_","http://flarebyte.com/005"])
  test.done()

