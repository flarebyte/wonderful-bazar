browser = require("marketplace.browser")
___ = require("underscore")
___.mixin require("underscore.string")

#TODO: unhardcode path

ID_URL="http://localhost:3000/flarebyte-marketplace/id"

exports.dispatchRoot_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "recurser": { "downloads":[]}
    "data":
      "root":"#{ID_URL}/offering/offering0"
         
  endTask = (err, results)->
    test.deepEqual(ctx.data._root_.about,ctx.data.root)
    test.done()
  browser.dispatchRoot(ctx,"recurser",endTask)

exports.dispatchFirstFew_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "recurser": { "downloads":[]}
    "data":
      "root":"#{ID_URL}/offering/offering0"
      "_root_":
        type: "http://localhost:3000/flarebyte-marketplace/schema/types#Offering"
        availableAtOrFrom: "#{ID_URL}/business/business0",
        body: "http://localhost:3001/flarebyte-marketplace/markup/all/0.md",
        comments: "#{ID_URL}/offering/offering0/comments",
        creator: "#{ID_URL}/people/people0",
        hasWarrantyPromise: "#{ID_URL}/warranty/warranty0",
        history: "#{ID_URL}/offering/offering0/history",
        image: "http://localhost:3001/flarebyte-marketplace/image/all/0",
        inbounds: "#{ID_URL}/offering/offering0/inbounds",
        outbounds: "#{ID_URL}/offering/offering0/outbounds",
        stats: "#{ID_URL}/offering/offering0/stats",
        subject: ["http://dbpedia.org/resource/Computer_science","http://dbpedia.org/resource/Journal"],
        includesObject: [
          {typeOfGood: "#{ID_URL}/product-or-service/product1"},
          {typeOfGood: "#{ID_URL}/product-or-service/product2"},
          {typeOfGood: "#{ID_URL}/product-or-service/product3"},
          {typeOfGood: "#{ID_URL}/product-or-service/product4"},
        ]
          
          
  endTask = (err, results)->
    test.deepEqual(ctx.data._root_._availableAtOrFrom_.about,ctx.data._root_.availableAtOrFrom)
    test.deepEqual(ctx.data._root_._comments_.type,"http://localhost:3000/flarebyte-marketplace/schema/types#Offering")
    test.deepEqual(ctx.data._root_._comments_.results[0].type,"http://localhost:3000/flarebyte-marketplace/schema/types#Post")
    test.deepEqual(ctx.data._root_._creator_.about,ctx.data._root_.creator)
    test.deepEqual(ctx.data._root_._hasWarrantyPromise_.about,ctx.data._root_.hasWarrantyPromise)
    test.deepEqual(ctx.data._root_._outbounds_.type,"http://localhost:3000/flarebyte-marketplace/schema/types#Outbounds")
    test.deepEqual(ctx.data._root_._stats_.type,"http://localhost:3000/flarebyte-marketplace/schema/types#Stats")
    test.deepEqual(ctx.data._root_.includesObject[0]._typeOfGood_.about,"http://localhost:3000/flarebyte-marketplace/id/product-or-service/product-or-service1")
    test.deepEqual(ctx.data._root_.includesObject[1]._typeOfGood_.about,"http://localhost:3000/flarebyte-marketplace/id/product-or-service/product-or-service2")
    test.deepEqual(ctx.data._root_.includesObject[2]._typeOfGood_.about,"http://localhost:3000/flarebyte-marketplace/id/product-or-service/product-or-service3")
    test.ok(not ctx.data._root_.includesObject[3]._typeOfGood_)
    test.ok(___.includes(ctx.data._root_._body_,"not considering the asterisk"))
    test.done()
  browser.dispatchFirstFew(ctx,"recurser",endTask)


exports.dispatchFirstMany_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "recurser": { "downloads":[]}
    "data":
      "root":"#{ID_URL}/offering/offering0"
      "_root_":
        type: "http://localhost:3000/flarebyte-marketplace/schema/types#Offering"
        availableAtOrFrom: "#{ID_URL}/business/business0",
        body: "http://localhost:3001/flarebyte-marketplace/markup/all/0.md",
        comments: "#{ID_URL}/offering/offering0/comments",
        creator: "#{ID_URL}/people/people0",
        hasWarrantyPromise: "#{ID_URL}/warranty/warranty0",
        history: "#{ID_URL}/offering/offering0/history",
        image: "http://localhost:3001/flarebyte-marketplace/image/all/0",
        inbounds: "#{ID_URL}/offering/offering0/inbounds",
        outbounds: "#{ID_URL}/offering/offering0/outbounds",
        stats: "#{ID_URL}/offering/offering0/stats",
        subject: ["http://dbpedia.org/resource/Computer_science","http://dbpedia.org/resource/Journal"],
        includesObject: [
          {typeOfGood: "#{ID_URL}/product-or-service/product1"},
          {typeOfGood: "#{ID_URL}/product-or-service/product2"},
          {typeOfGood: "#{ID_URL}/product-or-service/product3"},
          {typeOfGood: "#{ID_URL}/product-or-service/product4"},
        ]
          
          
  endTask = (err, results)->
    test.deepEqual(ctx.data._root_._availableAtOrFrom_.about,ctx.data._root_.availableAtOrFrom)
    test.ok(not ctx.data._root_._comments_)
    test.deepEqual(ctx.data._root_._creator_.about,ctx.data._root_.creator)
    test.ok(not ctx.data._root_._hasWarrantyPromise_)
    test.ok(not ctx.data._root_._outbounds_)
    test.deepEqual(ctx.data._root_._stats_.type,"http://localhost:3000/flarebyte-marketplace/schema/types#Stats")
    test.deepEqual(ctx.data._root_.includesObject[0]._typeOfGood_.about,"http://localhost:3000/flarebyte-marketplace/id/product-or-service/product-or-service1")
    test.deepEqual(ctx.data._root_.includesObject[1]._typeOfGood_.about,"http://localhost:3000/flarebyte-marketplace/id/product-or-service/product-or-service2")
    test.deepEqual(ctx.data._root_.includesObject[2]._typeOfGood_.about,"http://localhost:3000/flarebyte-marketplace/id/product-or-service/product-or-service3")
    test.ok(not ctx.data._root_.includesObject[3]._typeOfGood_)
    test.ok(not ctx.data._root_._body_)
    test.done()
  browser.dispatchFirstMany(ctx,"recurser",endTask)

exports.dispatchSecondFew_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "recurser": { "downloads":[]}
    "data":
      "root":"#{ID_URL}/offering/offering0"
      "_root_":
        type: "http://localhost:3000/flarebyte-marketplace/schema/types#Offering"
        _availableAtOrFrom_:
          stats: "#{ID_URL}/business/business0/stats",
        _creator_:
          stats: "#{ID_URL}/people/people0/stats",
          
  endTask = (err, results)->
    test.deepEqual(ctx.data._root_._availableAtOrFrom_._stats_.type,"http://localhost:3000/flarebyte-marketplace/schema/types#Stats")
    test.deepEqual(ctx.data._root_._creator_._stats_.type,"http://localhost:3000/flarebyte-marketplace/schema/types#Stats")
    test.done()
  browser.dispatchSecondFew(ctx,"recurser",endTask)


exports.dispatcherTask_root_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "recurser": { "downloads":[]}
    "data":
      "root":"#{ID_URL}/offering/offering0"
          
  endTask = (err, results)->
    test.deepEqual(ctx.data._root_.about,ctx.data.root)
    test.ok(ctx.recurser.root_done)
    test.ok(not ctx.recurser.first_done)
    test.ok(not ctx.recurser.second_done)
    test.ok(not ctx.recurser.exit)
    test.done()
  browser.dispatcherTask(ctx,"recurser",endTask)

exports.dispatcherTask_first_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "recurser": { "downloads":[],"root_done":true}
    "data":
      "root":"#{ID_URL}/offering/offering0"
      "_root_":
        type: "http://localhost:3000/flarebyte-marketplace/schema/types#Offering"
        "stuff":"bla"
          
  endTask = (err, results)->
    test.ok(ctx.recurser.root_done)
    test.ok(ctx.recurser.first_done)
    test.ok(not ctx.recurser.second_done)
    test.ok(not ctx.recurser.exit)
    test.done()
  browser.dispatcherTask(ctx,"recurser",endTask)

exports.dispatcherTask_second_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "recurser": { "downloads":[],"root_done":true, "first_done":true}
    "data":
      "root":"#{ID_URL}/offering/offering0"
      "_root_":
        type: "http://localhost:3000/flarebyte-marketplace/schema/types#Offering"
        "stuff":"bla"
          
  endTask = (err, results)->
    test.ok(ctx.recurser.root_done)
    test.ok(ctx.recurser.first_done)
    test.ok(ctx.recurser.second_done)
    test.ok(not ctx.recurser.exit)
    test.done()
  browser.dispatcherTask(ctx,"recurser",endTask)

exports.dispatcherTask_exit_should_work = (test) ->
  ctx = 
    "any":"stuff"
    "journal":[]
    "recurser": { "downloads":[],"root_done":true, "first_done":true, "second_done":true}
    "data":
      "root":"#{ID_URL}/offering/offering0"
      "_root_":
        type: "http://localhost:3000/flarebyte-marketplace/schema/types#Offering"
        "stuff":"bla"
          
  endTask = (err, results)->
    test.ok(ctx.recurser.root_done)
    test.ok(ctx.recurser.first_done)
    test.ok(ctx.recurser.second_done)
    test.ok(ctx.recurser.exit)
    test.done()
  browser.dispatcherTask(ctx,"recurser",endTask)

