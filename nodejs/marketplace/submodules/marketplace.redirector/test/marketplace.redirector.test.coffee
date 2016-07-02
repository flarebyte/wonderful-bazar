redirector = require("marketplace.redirector")
appsettings = require('flarebyte.settings')
data_hosting = appsettings.environment.data_hosting
web_hosting = appsettings.environment.web_hosting
marketplace = web_hosting["flarebyte-marketplace"].gbr

exports.webpage_valid_http = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = false
  uri = "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering0"
  slug = "offering-8-or-any-good-alternative."
  result = redirector.webpage(space, edition, secure, uri, slug)
  test.deepEqual(result,"#{marketplace.server_name}/gbr/offers/offering-8-or-any-good-alternative./offering0")
  test.done()

exports.webpage_valid_http_no_slug = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = false
  uri = "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering0"
  result = redirector.webpage(space, edition, secure, uri, null)
  test.deepEqual(result,"#{marketplace.server_name}/gbr/offers/offering0")
  test.done()

exports.webpage_valid_https = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = true
  uri = "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering0"
  slug = "offering-8-or-any-good-alternative."
  result = redirector.webpage(space, edition, secure, uri, slug)
  test.deepEqual(result,"#{marketplace.secure_server_name}/gbr/offers/offering-8-or-any-good-alternative./offering0")
  test.done()

exports.webpage_invalid_space = (test) ->
  space = "invalid-space"
  edition = "gbr"
  secure = false
  uri = "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering0"
  slug = "offering-8-or-any-good-alternative."
  f1= ->
    result = redirector.webpage(space, edition, secure, uri, slug)
  test.throws(f1)
  try
    result = redirector.webpage(space, edition, secure, uri, slug)
  catch e
     test.ok(e.message.indexOf("E974353028")>=0,"E974353028 expected, not "+e.message)
  test.done()

exports.webpage_invalid_edition = (test) ->
  space = "flarebyte-marketplace"
  edition = "invalid-edition"
  secure = false
  uri = "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering0"
  slug = "offering-8-or-any-good-alternative."
  test.throws ->
    result = redirector.webpage(space, edition, secure, uri, slug)
  try
    result = redirector.webpage(space, edition, secure, uri, slug)
  catch e
    test.ok(e.message.indexOf("E408197915")>=0,"E408197915 expected, not "+e.message)
  test.done()

#TODO: different spaces should deal with external websites
#TODO: interlink all flarebyte spaces
exports.webpage_valid_http_different_space = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = false
  uri = "#{data_hosting.HTTP_ID}/diff-space/id/offering/offering-8-or-any-good-alternative./offering0"
  slug = "offering-8-or-any-good-alternative."
  result = redirector.webpage(space, edition, secure, uri, slug)
  test.deepEqual(result,"#{marketplace.server_name}/gbr/diff-space/id/offering/offering-8-or-any-good-alternative./offering0")
  test.done()

exports.webpage_valid_http_different_space_no_slug = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = false
  uri = "#{data_hosting.HTTP_ID}/diff-space/id/offering/offering0"
  result = redirector.webpage(space, edition, secure, uri, null)
  test.deepEqual(result,"#{marketplace.server_name}/gbr/diff-space/id/offering/offering0")
  test.done()

exports.editionpage_shoul_be_valid = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  result = redirector.editionpage(space, edition)
  test.deepEqual(result,"#{marketplace.server_name}/gbr")
  test.done()

exports.history_should_be_valid = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = false
  uri = "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering0"
  result = redirector.history(space, edition, secure, uri)
  test.deepEqual(result,"#{marketplace.server_name}/history/gbr/offers/offering0")
  test.done()

exports.history_valid_different_space = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = false
  uri = "#{data_hosting.HTTP_ID}/diff_space/id/offering/offering0"
  result = redirector.history(space, edition, secure, uri)
  test.deepEqual(result,"#{marketplace.server_name}/history/gbr/diff_space/id/offering/offering0")
  test.done()

exports.webpageConcat_should_be_valid = (test) ->
  space = "flarebyte-marketplace"
  edition = "gbr"
  secure = false
  domain = "offers"
  uri = "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering0"
  slug = "offering-8-or-any-good-alternative."
  id ="1234"
  result = redirector.webpageConcat(space, edition, secure, domain, slug, id)
  test.deepEqual(result,"#{marketplace.server_name}/gbr/offers/offering-8-or-any-good-alternative./1234")
  test.done()

exports.idpageConcat_should_be_valid = (test) ->
  result = redirector.idpageConcat("space", "domain", "id")
  test.deepEqual(result,"#{data_hosting.HTTP_ID}/space/id/domain/id")
  test.done()
