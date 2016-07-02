models = require("marketplace.models")
app_i18n = require("marketplace.i18n")
marketplace=app_i18n["flarebyte-marketplace"]

validateEdition= (test, edition) ->
  test.ok(edition.edition_name.length>4)

exports.gbr_should_work = (test) ->
  validateEdition(test, marketplace.gbr)
  test.done()
