recurser = require("flarebyte.recurser")
scheduler = require("flarebyte.scheduler")
___ = require("underscore")

exports.executeTask_exit_should_work = (test) ->
  ctx = {"any":"stuff","journal":[],"processing":[]}
  startTaskParams = ["A_arg1","A_arg2","A_arg3"]
  startTask = (ctx_local,arg1,arg2,arg3, callback)->
    setTimeout (->
      ctx_local["start"]=
        "_1":arg1
        "_2":arg2
        "_3":arg3
      ctx_local.journal.push("start")
      callback(null, "A")
    ), 25

  processingTaskParams = ["P_arg1","P_arg2"]
  processingTask = (ctx_local,arg1,arg2, callback)->
    setTimeout (->
      ctx_local.processing.push({"arg1":arg1, "arg2":arg2})
      ctx_local["P"]=
        "_1":arg1
        "_2":arg2
      ctx_local.journal.push("P")
      callback(null, "P")
    ), 25
    
  endTaskParams = ["B_arg1","B_arg2","B_arg3"]
  endTask = (ctx_local,arg1,arg2,arg3)->
    setTimeout (->
      ctx_local["end"]=
        "_1":arg1
        "_2":arg2
        "_3":arg3
      ctx_local.journal.push("end")
      test.deepEqual(ctx.journal,[ 'start','scheduler','dispatcher','P','P','scheduler','end' ])
      test.done()
    ), 2
  dispatcherTask = (ctx_local,recurser_name,schedulerTask)->
    setTimeout (->
      ctx_local.journal.push("dispatcher")
      processingMessage1 = scheduler.createMessage(ctx, ["Alpha","Bravo"], processingTask)
      processingMessage2 = scheduler.createMessage(ctx, ["Charlie","Delta"], processingTask)
      ctx_local[recurser_name].exit=true
      scheduler.executeParallelTasks([processingMessage1,processingMessage2],schedulerTask)
    ), 5
  startMessage = scheduler.createMessage(ctx, startTaskParams, startTask)
  endMessage = scheduler.createEndMessage(ctx, endTaskParams, endTask)
  dispatcherMessage = scheduler.createDispatcherMessage(ctx, dispatcherTask,10)
  recurser.runRecurser("test_recurser",startMessage,endMessage, dispatcherMessage)

exports.executeTask_killcount_should_work = (test) ->
  ctx = {"any":"stuff","journal":[],"processing":[]}
  startTaskParams = ["A_arg1","A_arg2","A_arg3"]
  startTask = (ctx_local,arg1,arg2,arg3, callback)->
    setTimeout (->
      ctx_local["start"]=
        "_1":arg1
        "_2":arg2
        "_3":arg3
      ctx_local.journal.push("start")
      callback(null, "A")
    ), 25

  processingTaskParams = ["P_arg1","P_arg2"]
  processingTask = (ctx_local,arg1,arg2, callback)->
    setTimeout (->
      ctx_local.processing.push({"arg1":arg1, "arg2":arg2})
      ctx_local["P"]=
        "_1":arg1
        "_2":arg2
      ctx_local.journal.push("P")
      callback(null, "P")
    ), 25
    
  endTaskParams = ["B_arg1","B_arg2","B_arg3"]
  endTask = (ctx_local,arg1,arg2,arg3)->
    setTimeout (->
      ctx_local["end"]=
        "_1":arg1
        "_2":arg2
        "_3":arg3
      ctx_local.journal.push("end")
      expected = [ 'start',
        'scheduler',
        'dispatcher',
        'P',
        'P',
        'scheduler',
        'dispatcher',
        'P',
        'P',
        'scheduler',
        'dispatcher',
        'P',
        'P',
        'scheduler',
        'dispatcher',
        'P',
        'P',
        'scheduler',
        'end' ]
      
      test.deepEqual(ctx.journal,expected)
      test.done()
    ), 2
  dispatcherTask = (ctx_local,recurser_name,schedulerTask)->
    setTimeout (->
      ctx_local.journal.push("dispatcher")
      processingMessage1 = scheduler.createMessage(ctx, ["Alpha","Bravo"], processingTask)
      processingMessage2 = scheduler.createMessage(ctx, ["Charlie","Delta"], processingTask)
      ctx_local[recurser_name].exit=false
      scheduler.executeParallelTasks([processingMessage1,processingMessage2],schedulerTask)
    ), 5
  startMessage = scheduler.createMessage(ctx, startTaskParams, startTask)
  endMessage = scheduler.createEndMessage(ctx, endTaskParams, endTask)
  dispatcherMessage = scheduler.createDispatcherMessage(ctx, dispatcherTask,4)
  recurser.runRecurser("test_recurser",startMessage,endMessage, dispatcherMessage)

