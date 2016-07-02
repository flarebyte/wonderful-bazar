dummy = require("marketplace.dummy")

exports.dateTimeFromInt_should_work = (test) ->
  test.deepEqual(dummy.dateTimeFromInt(12),"2008-04-22T04:22:00Z")
  test.done()

exports.extractNumbers_should_work = (test) ->
  test.deepEqual(dummy.extractNumbers("fabala12"),"12")
  test.done()

exports.ipsum_should_work = (test) ->
  test.deepEqual(dummy.ipsum("20"),"Lorem ipsum dolor si")
  test.done()
