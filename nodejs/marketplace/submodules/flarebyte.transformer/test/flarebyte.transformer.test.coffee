transformer = require("flarebyte.transformer")
appsettings = require('flarebyte.settings')
data_hosting = appsettings.environment.data_hosting
web_hosting = appsettings.environment.web_hosting
marketplace = web_hosting["flarebyte-marketplace"].gbr

exports.dateify_unknown_field_should_be_ignored = (test) ->
  ctx =
    req:
      params:
        edition: "gbr"
  ctx_value = {}
  result = transformer.dateify(ctx, ctx_value,"unknown_field")
  test.deepEqual(ctx_value,{})
  test.done()

exports.dateify_field_with_invalid_date_should_raise_exception = (test) ->
  ctx =
    req:
      params:
        edition: "gbr"
  ctx_value = {"string_field":"string"}
  test.throws ->
    transformer.dateify(ctx, ctx_value,"string_field")
  test.done()

exports.dateify_valid_date_field_should_populate_additional_fields = (test) ->
  ctx =
    req:
      params:
        edition: "gbr"
  ctx_value = {"created":"2008-01-10T01:10:00Z"}
  result = transformer.dateify(ctx, ctx_value,"created")
  expected =
    created: '2008-01-10T01:10:00Z'
    created__weekday_name: 'Thursday'
    created__time: '01:10'
    created__year: 2008
    created__month_name: 'January'
    created__month: 1
    created__day: 10

  test.deepEqual(ctx_value,expected)
  test.done()

exports.webpageify_unknown_field_should_be_ignored = (test) ->
  ctx =
    req:
      params:
        space: "flarebyte-marketplace"
        edition: "gbr"
  ctx_value =
    about: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering8"
    label: "offering 8 or any good alternative."
  result = transformer.webpageify(ctx, ctx_value,"unknown_field","label")
  expected =
    about: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering8"
    label: "offering 8 or any good alternative."
    label__slug: "offering-8-or-any-good-alternative."

  test.deepEqual(ctx_value,expected)
  test.done()


exports.webpageify_valid_webpage_field_should_populate_additional_fields = (test) ->
  ctx =
    req:
      params:
        space: "flarebyte-marketplace"
        edition: "gbr"
  ctx_value =
    about: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering8"
    label: "offering 8 or any good alternative."
  result = transformer.webpageify(ctx, ctx_value,"about","label","")
  expected =
    about: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering8"
    label: "offering 8 or any good alternative."
    label__slug: "offering-8-or-any-good-alternative."
    about__view_page: "#{marketplace.server_name}/gbr/offers/offering-8-or-any-good-alternative./offering8"
    about__edit_page: "#{marketplace.secure_server_name}/gbr/offers/offering-8-or-any-good-alternative./offering8"

  test.deepEqual(ctx_value,expected)
  test.done()


exports.webpageify_unknown_label_field_should_still_populate_additional_fields = (test) ->
  ctx =
    req:
      params:
        space: "flarebyte-marketplace"
        edition: "gbr"
  ctx_value =
    about: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering8"
    label: "offering 8 or any good alternative."
  result = transformer.webpageify(ctx, ctx_value,"about","unknown_label","/comments")
  expected =
    about: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/id/offering/offering8"
    label: "offering 8 or any good alternative."
    about__view_page: "#{marketplace.server_name}/gbr/offers/offering8/comments"
    about__edit_page: "#{marketplace.secure_server_name}/gbr/offers/offering8/comments"

  test.deepEqual(ctx_value,expected)
  test.done()

exports.titleify_unknown_field_should_be_ignored = (test) ->
  ctx_value = {}
  result = transformer.titleify(ctx_value,"unknown_field")
  test.deepEqual(ctx_value,{})
  test.done()

exports.titleify_valid_title_field_should_populate_additional_fields = (test) ->
  ctx_value = {"label":"offering 8 or any good alternative."}
  result = transformer.titleify(ctx_value,"label")
  expected =
    label: 'offering 8 or any good alternative.'
    label__title: 'Offering 8 Or Any Good Alternative.'

  test.deepEqual(ctx_value,expected)
  test.done()

exports.slugify_unknown_field_should_be_ignored = (test) ->
  ctx_value = {}
  result = transformer.slugify(ctx_value,"unknown_field")
  test.deepEqual(ctx_value,{})
  test.done()

exports.slugify_valid_title_field_should_populate_additional_fields = (test) ->
  ctx_value = {"label":"offering 8, or any good alternative; (c) flarebyte.com"}
  result = transformer.slugify(ctx_value,"label")
  expected =
    label: 'offering 8, or any good alternative; (c) flarebyte.com'
    label__slug: 'offering-8,-or-any-good-alternative;-(c)-flarebyte.com'

  test.deepEqual(ctx_value,expected)
  test.done()

exports.typify_unknown_field_should_be_ignored = (test) ->
  ctx_value = {}
  result = transformer.typify(ctx_value,"unknown_field")
  test.deepEqual(ctx_value,{})
  test.done()

exports.typify_valid_camelcase_type_field_should_populate_additional_fields = (test) ->
  ctx_value = {type: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/schema/types#OfferingStuff"}
  result = transformer.typify(ctx_value,"type")
  expected =
    type: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/schema/types#OfferingStuff"
    type__title: "OfferingStuff"
    type__underscore: "offering_stuff"

  test.deepEqual(ctx_value,expected)
  test.done()

exports.typify_valid_dashcase_type_field_should_populate_additional_fields = (test) ->
  ctx_value = {type: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/schema/types#Offering-Stuff_more"}
  result = transformer.typify(ctx_value,"type")
  expected =
    type: "#{data_hosting.HTTP_ID}/flarebyte-marketplace/schema/types#Offering-Stuff_more"
    type__title: "Offering-Stuff_more"
    type__underscore: "offering_stuff_more"

  test.deepEqual(ctx_value,expected)
  test.done()


exports.statsAsMap_valid_stats_should_populate_additional_fields = (test) ->
  ctx_value =
    statItem: [ {dimension: "numberOfVotes", value: 60}, {dimension: "numberOfReads", value: 88315}]
  result = transformer.statsAsMap(null,ctx_value)
  expected =
    statItem: [ {dimension: "numberOfVotes", value: 60}, {dimension: "numberOfReads", value: 88315}]
    numberOfVotes: 60
    numberOfReads: 88315

  test.deepEqual(ctx_value,expected)
  test.done()
