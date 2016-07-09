flash = require("frozen-flash")
renderer = require("frozen-renderer")


exports.index = (req, res) ->
  fullurl = "#{req.host}#{req.params.relurl}"

  flash.httpGetLiveUrl fullurl, (statusCode, json) ->
    renderer.render(req,res,statusCode,json)
        