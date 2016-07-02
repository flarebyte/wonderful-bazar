___ = require("underscore")
___.mixin require("underscore.string")
models = require("marketplace.models")
slugdata = require("marketplace.i18n.slugdata")

isDefined= (value) ->
  r =  ___.isNull(value) or ___.isUndefined(value) or ___.isBlank(value)
  return not r
  
validateEdition= (test, edition) ->
  missings = []
  for name, domain of models
    dashname = ___.dasherize(name)
    existence = isDefined(edition.domain_to_slug[dashname])
    missings.push(dashname) if not existence
    test.ok(existence,'The domain #{dashname} is not defined !')
  if not ___.isEmpty(missings)
    console.log("Please define the following domains: </p>")
    for missing in missings
      console.log("'#{missing}': '#{missing}' </p>")

exports.gbr_should_work = (test) ->
  validateEdition(test, slugdata.gbr)
  test.done()
