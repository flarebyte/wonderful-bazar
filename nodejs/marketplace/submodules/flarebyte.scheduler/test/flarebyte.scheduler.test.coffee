scheduler = require("flarebyte.scheduler")
async = require("async")
___ = require("underscore")

exports.createMessage_should_work = (test) ->
  ctx = {"any":"stuff"}
  taskParams = {"messageType":"http-get"}
  task = (params)->
    return params
  message = scheduler.createMessage(ctx, taskParams, task)
  test.deepEqual(message.ctx,ctx)
  test.deepEqual(message.taskParams,taskParams)
  test.equal(message.task,task)
  test.done()

exports.createTask_should_work = (test) ->
  ctx = {"any":"stuff"}
  taskParams = [{"messageType":"http-get"},"arg2","arg3"]
  task = (ctx_local,arg1,arg2,arg3)->
    ctx_local["result1"]=arg1
    ctx_local["result2"]=arg2
    ctx_local["result3"]=arg3
  message = scheduler.createMessage(ctx, taskParams, task)
  createdTask = scheduler.createTask(message)
  test.ok(___.isFunction(createdTask))
  test.done()

exports.executeTask_should_work = (test) ->
  ctx = {"any":"stuff","journal":[]}
  taskParamsA = ["A_arg1","A_arg2","A_arg3"]
  taskA = (ctx_local,arg1,arg2,arg3, callback)->
    ctx_local["A"]=
      "_1":arg1
      "_2":arg2
      "_3":arg3
    ctx_local.journal.push("A")
    callback(null, "A")
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["A"])
    test.deepEqual(ctx.journal,["A"])
    test.deepEqual(ctx.any,"stuff")
    test.deepEqual(ctx.A,{"_1":"A_arg1","_2":"A_arg2","_3":"A_arg3"})
    test.done()
  messageA = scheduler.createMessage(ctx, taskParamsA, taskA)
  scheduler.executeTask(messageA, schedulerTask)

exports.createTasks_should_work = (test) ->
  ctx = {"any":"stuff","journal":[]}
  taskParamsA = ["A_arg1","A_arg2","A_arg3"]
  taskA = (ctx_local,arg1,arg2,arg3, callback)->
    ctx_local["A"]=
      "_1":arg1
      "_2":arg2
      "_3":arg3
    ctx_local.journal.push("A")
    callback(null, "A")
  taskParamsB = ["B_arg1","B_arg2"]
  taskB = (ctx_local,arg1,arg2, callback)->
    ctx_local["B"]=
      "_1":arg1
      "_2":arg2
    ctx_local.journal.push("B")
    callback(null, "B")
  taskParamsC = ["C_arg1","C_arg2","C_arg3","C_arg4"]
  taskC = (ctx_local,arg1,arg2,arg3, arg4, callback)->
    ctx_local["C"]=
      "_1":arg1
      "_2":arg2
      "_3":arg3
      "_4":arg4
    ctx_local.journal.push("C")
    callback(null, "C")
  messageA = scheduler.createMessage(ctx, taskParamsA, taskA)
  messageB = scheduler.createMessage(ctx, taskParamsB, taskB)
  messageC = scheduler.createMessage(ctx, taskParamsC, taskC)
  messages = [messageA,messageB,messageC]
  tasks = scheduler.createTasks(messages)
  test.deepEqual(tasks.length,3)
  test.ok(___.isFunction(tasks[0]))
  test.ok(___.isFunction(tasks[1]))
  test.ok(___.isFunction(tasks[2]))
  test.notEqual(tasks[0],tasks[1])
  test.notEqual(tasks[0],tasks[2])
  test.notEqual(tasks[1],tasks[2])
  test.done()
  


exports.executeParallelTasks_should_work = (test) ->
  ctx = {"any":"stuff","journal":[]}
  taskParamsA = ["A_arg1","A_arg2","A_arg3"]
  taskA = (ctx_local,arg1,arg2,arg3, callback)->
    ctx_local["A"]=
      "_1":arg1
      "_2":arg2
      "_3":arg3
    ctx_local.journal.push("A")
    callback(null, "A")
  taskParamsB = ["B_arg1","B_arg2"]
  taskB = (ctx_local,arg1,arg2, callback)->
    setTimeout (->
      ctx_local["B"]=
        "_1":arg1
        "_2":arg2
      ctx_local.journal.push("B")
      callback(null, "B")
    ), 25
  taskParamsC = ["C_arg1","C_arg2","C_arg3","C_arg4"]
  taskC = (ctx_local,arg1,arg2,arg3, arg4, callback)->
    ctx_local["C"]=
      "_1":arg1
      "_2":arg2
      "_3":arg3
      "_4":arg4
    ctx_local.journal.push("C")
    callback(null, "C")
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["A","B","C"])
    test.deepEqual(ctx.journal,["A","C","B"])
    test.deepEqual(ctx.any,"stuff")
    test.deepEqual(ctx.C,{"_1":"C_arg1","_2":"C_arg2","_3":"C_arg3","_4":"C_arg4"})
    test.deepEqual(ctx.B,{"_1":"B_arg1","_2":"B_arg2"})
    test.deepEqual(ctx.A,{"_1":"A_arg1","_2":"A_arg2","_3":"A_arg3"})
    test.done()
  messageA = scheduler.createMessage(ctx, taskParamsA, taskA)
  messageB = scheduler.createMessage(ctx, taskParamsB, taskB)
  messageC = scheduler.createMessage(ctx, taskParamsC, taskC)
  messages = [messageA,messageB,messageC]
  scheduler.executeParallelTasks(messages, schedulerTask)

exports.executeSerialTasks_should_work = (test) ->
  ctx = {"any":"stuff","journal":[]}
  taskParamsA = ["A_arg1","A_arg2","A_arg3"]
  taskA = (ctx_local,arg1,arg2,arg3, callback)->
    ctx_local["A"]=
      "_1":arg1
      "_2":arg2
      "_3":arg3
    ctx_local.journal.push("A")
    callback(null, "A")
  taskParamsB = ["B_arg1","B_arg2"]
  taskB = (ctx_local,arg1,arg2, callback)->
    setTimeout (->
      ctx_local["B"]=
        "_1":arg1
        "_2":arg2
      ctx_local.journal.push("B")
      callback(null, "B")
    ), 25
  taskParamsC = ["C_arg1","C_arg2","C_arg3","C_arg4"]
  taskC = (ctx_local,arg1,arg2,arg3, arg4, callback)->
    ctx_local["C"]=
      "_1":arg1
      "_2":arg2
      "_3":arg3
      "_4":arg4
    ctx_local.journal.push("C")
    callback(null, "C")
  schedulerTask = (err, results) ->
    test.equals(err, null)
    test.deepEqual(results,["A","B","C"])
    test.deepEqual(ctx.journal,["A","B","C"])
    test.deepEqual(ctx.any,"stuff")
    test.deepEqual(ctx.C,{"_1":"C_arg1","_2":"C_arg2","_3":"C_arg3","_4":"C_arg4"})
    test.deepEqual(ctx.B,{"_1":"B_arg1","_2":"B_arg2"})
    test.deepEqual(ctx.A,{"_1":"A_arg1","_2":"A_arg2","_3":"A_arg3"})
    test.done()
  messageA = scheduler.createMessage(ctx, taskParamsA, taskA)
  messageB = scheduler.createMessage(ctx, taskParamsB, taskB)
  messageC = scheduler.createMessage(ctx, taskParamsC, taskC)
  messages = [messageA,messageB,messageC]
  scheduler.executeSerialTasks(messages, schedulerTask)

