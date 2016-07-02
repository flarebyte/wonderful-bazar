tester = require('./tester')

exports.divider_date_updated_span_should_work = (test) ->
  tester.verify(test, "divider/divider_date_updated_span")
  
exports.divider_date_should_work = (test) ->
  tester.verify(test, "divider/divider_date")

exports.divider_count_should_work = (test) ->
  tester.verify(test, "divider/divider_count")

exports.divider_title_should_work = (test) ->
  tester.verify(test, "divider/divider_title")
