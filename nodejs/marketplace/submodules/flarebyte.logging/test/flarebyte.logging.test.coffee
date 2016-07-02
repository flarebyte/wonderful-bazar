logger = require("flarebyte.logging")

exports.logger_should_work = (test) ->
  logger.info("flarebyte.ldrest","method1","message1")
  logger.warn("flarebyte.recurser","method2","message2")
  logger.error("flarebyte.scheduler","method3","message3")
  logger.security("flarebyte.ldrest","method4","message4",{"issue":12})
  test.done()

