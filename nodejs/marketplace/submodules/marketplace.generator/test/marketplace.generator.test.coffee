redirector = require("marketplace.redirector")

exports.webpage_valid_http = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = false
  uri = "http://localhost:3000/flarebyte-marketplace/id/offering/offering0"
  slug = "offering-8-or-any-good-alternative."
  result = redirector.webpage(space, edition, secure, uri, slug)
  test.deepEqual(result,"http://localhost:3010/gbr/offers/offering-8-or-any-good-alternative./offering0")
  test.done()

