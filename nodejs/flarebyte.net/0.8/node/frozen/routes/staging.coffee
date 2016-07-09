flash = require("frozen-flash")
renderer = require("frozen-renderer")

exports.index = (req, res) ->
  flash.httpGetStageUrl "stage.flarebyte.com", (statusCode, json) ->
    renderer.render(req,res,statusCode,json)
         
exports.preview = (req, res) ->
  bizkey=req.params.bizkey
  bizid=req.params.bizid
  pjkey=req.params.pjkey
  pjid=req.params.pjid
  relurl=req.params.relurl

  flash.httpGetStageProjectUrl(
    bizkey
    bizid
    pjkey
    pjid
    relurl, (statusCode, json) ->
      renderer.render(req,res,statusCode,json)
    )