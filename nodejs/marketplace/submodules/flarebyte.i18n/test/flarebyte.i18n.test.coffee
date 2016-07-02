i18n = require("flarebyte.i18n")
___ = require("underscore")

exports.swapMap_should_work = (test) ->
  actual =
    a: "AA"
    b: "BB"
    c: "CC"
  expected =
    "AA": "a"
    "BB": "b"
    "CC": "c"
  test.deepEqual(i18n.swapMap(actual),expected)
  test.done()

exports.swapMap_empty_should_work = (test) ->
  test.deepEqual(i18n.swapMap({}),{})
  test.deepEqual(i18n.swapMap(null),null)
  test.done()

exports.domainToSlug_should_work = (test) ->
  actual=
    gbr:
      domain_to_slug:
        offering: "offers"
  test.deepEqual(i18n.domainToSlug(actual,"gbr","offering"),"offers")
  test.done()

exports.domainToSlug_unknown_edition_should_raise_error = (test) ->
  actual=
    gbr:
      domain_to_slug:
        offering: "offers"
  test.throws ->
    i18n.domainToSlug(actual,"cz","offering")
  test.done()

exports.slugToDomain_should_work = (test) ->
  actual=
    gbr:
      slug_to_domain:
        offers: "offering"
  test.deepEqual(i18n.slugToDomain(actual,"gbr","offers"),"offering")
  test.done()

exports.slugToDomainFromReq_should_work = (test) ->
  actual=
    gbr:
      slug_to_domain:
        offers: "Offering That"
  req =
    params:
      domain_slug: "offers"
      edition: "gbr"
  expected =
    params:
      domain_slug: "offers"
      edition: "gbr"
      domain: "Offering That"
      domain_view: "offering_that"
  
  i18n.slugToDomainFromReq(actual,req)   
  test.deepEqual(req,expected)
  test.done()

exports.selectEdition_should_work = (test) ->
  actual =
    marketplace:
      gbr:
        a: "AA"
        b: "BB"
        c: "CC"
  expected =
    a: "AA"
    b: "BB"
    c: "CC"
  test.deepEqual(i18n.selectEdition(actual, "marketplace","gbr"),expected)
  test.done()

exports.extendFrom_should_work = (test) ->
  general =
    a: "AA"
    b: "BB"
    c: "CC"
    e: 
      f: "FF"
  specific =
    c: "new_c"
    d: "DD"
    e: 
      g: "GG"
  expected =
    a: "AA"
    b: "BB"
    c: "new_c"
    d: "DD"
    e: 
      f: "FF"
      g: "GG"
  test.deepEqual(i18n.extendFrom(specific,general),expected)
  test.done()
