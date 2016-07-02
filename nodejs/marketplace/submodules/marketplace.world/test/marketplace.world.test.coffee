WorldFactory = require("marketplace.world").WorldFactory

exports.webpage_valid_http = (test) ->
  endCallback = (err, browser, status) ->
     test.deepEqual(status,200)
     test.done()
  World = new WorldFactory
  World.visitPublicMarketplace("/gbr/offers/offering-6771-or-any-good-alternative./6771",endCallback)

