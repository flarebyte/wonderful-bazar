___ = require("underscore")
___.mixin require("underscore.string")
jpath = require("flarebyte.jpath")

json =
  first:
    second:
      about: "http://localhost:3000/flarebyte-marketplace/id/offering/offering0"
      isPartOf: "http://localhost:3000/flarebyte-marketplace/id/dataset/offering"
      label: "offering 0 or any good alternative."
      creator: "http://localhost:3000/flarebyte-marketplace/id/people/people0"
      subject: [ "http://dbpedia.org/resource/Computer_science", "http://dbpedia.org/resource/Journal" ]
      created: "2008-01-10T01:10:00Z"
      language: "en"
      inbounds: "http://localhost:3000/flarebyte-marketplace/id/offering/offering0/inbounds"
      body: "http://localhost:3001/flarebyte-marketplace/markup/all/0.md"
      image: "http://localhost:3001/flarebyte-marketplace/image/all/0"
      includesObject: [
        typeOfGood: "http://localhost:3000/flarebyte-marketplace/id/product-or-service/product0"
        hasUnitOfMeasurement: "C62"
        amountOfThisGood: 1
        type: "TypeAndQuantityNode"
      ,
        typeOfGood: "http://localhost:3000/flarebyte-marketplace/id/product-or-service/product1"
        hasUnitOfMeasurement: "C65"
        amountOfThisGood: 2
        type: "TypeAndQuantityNode"
       ]
  
exports.extractIndex_should_work = (test) ->
  test.deepEqual(jpath.extractIndex("value[10]"),10)
  test.done()

exports.extractBase_should_work = (test) ->
  test.deepEqual(jpath.extractBase("value[10]"),"value")
  test.done()

exports.containsIndex_should_work = (test) ->
  test.ok(jpath.containsIndex("value[10]"))
  test.ok(not jpath.containsIndex("value"))
  test.done()

exports.splitLast_should_work = (test) ->
  test.deepEqual(jpath.splitLast("$.data._root_.creator"),["$.data._root_","creator"])
  test.deepEqual(jpath.splitLast("$/data/_root_/creator"),[null,null])
  test.deepEqual(jpath.splitLast(null),[null,null])
  test.done()

exports.get_should_work = (test) ->
  test.deepEqual(jpath.get(json,"$.first"),json.first)
  test.deepEqual(jpath.get(json,"$.first.second"),json.first.second)
  test.deepEqual(jpath.get(json,"$.first.second.about"),json.first.second.about)
  test.deepEqual(jpath.get(json,"$.first.second.includesObject"),json.first.second.includesObject)
  test.deepEqual(jpath.get(json,"$.first.second.includesObject[0]"),json.first.second.includesObject[0])
  test.deepEqual(jpath.get(json,"$.first..hasUnitOfMeasurement"),["C62","C65"])  
  test.deepEqual(jpath.get(json,"$.first..includesObject[?(@.amountOfThisGood>1)]"),json.first.second.includesObject[1])  
  test.deepEqual(jpath.get(json,"$.first..includesObject[?(@.amountOfThisGood==2)]"),json.first.second.includesObject[1])  
  test.deepEqual(jpath.get(json,"$.first..includesObject[?(@.hasUnitOfMeasurement=='C65')]"),json.first.second.includesObject[1])  
  test.done()

exports.getUrls_should_work = (test) ->
  test.deepEqual(jpath.getUrls(json,"$.first.second.no_url"),null)
  test.deepEqual(jpath.getUrls(json,"$.first.whatever.no_url"),null)
  test.deepEqual(jpath.getUrls(json,"$.first.second.creator"),["http://localhost:3000/flarebyte-marketplace/id/people/people0"])
  test.deepEqual(jpath.getUrls(json,"$.first.second.subject"),[ "http://dbpedia.org/resource/Computer_science", "http://dbpedia.org/resource/Journal" ])
  test.done()

exports.get_on_null_should_raise_error = (test) ->
  test.throws ->
    jpath.get(null,"$.first")
  test.done()

exports.checkUrl_should_raise_error = (test) ->
  test.throws ->
    jpath.checkUrl("not a url")
  test.done()

exports.checkUrl_should_not_raise_error = (test) ->
  test.doesNotThrow ->
    jpath.checkUrl("http://marketplace.flarebyte.com/flarebyte-marketplace/data/offering/offering0.rdf")
  test.doesNotThrow ->
    jpath.checkUrl("http://localhost:3000/flarebyte-marketplace/data/offering/offering0.rdf")
  test.done()

exports.checkUrl_should_raise_error = (test) ->
  test.throws ->
    jpath.checkUrls(["http://marketplace.flarebyte.com/flarebyte-marketplace/data/offering/offering0.rdf","not a url"])
  test.done()

exports.set_simple_key_should_work = (test) ->
  actual =
    first:
      second:
        reviews: []
        third:
          title: "How to Steal a Million"
  expected =
    first:
      second:
        stars: ["Audrey Hepburn","Peter O'Toole"]
        reviews: ["good","bad","ugly"]
        third:
          title: "How to Steal a Million"
  
  jpath.set(actual,"$.first.second","stars",["Audrey Hepburn","Peter O'Toole"])
  jpath.set(actual,"$.first.second.reviews","2","ugly")
  jpath.set(actual,"$.first.second.reviews","0","good")
  jpath.set(actual,"$.first.second.reviews","1","bad")
  test.deepEqual(actual,expected)
  test.done()

exports.set_on_null_should_raise_error = (test) ->
  test.throws ->
    jpath.set(null,"$.first.second","stars",["Audrey Hepburn","Peter O'Toole"])
  test.done()

exports.add_simple_key_should_work = (test) ->
  actual =
    first:
      second:
        stars: ["Audrey Hepburn"]
        third:
          title: "How to Steal a Million"
  expected =
    first:
      second:
        stars: ["Audrey Hepburn","Peter O'Toole"]
        third:
          title: "How to Steal a Million"
  
  rpath = jpath.add(actual,"$.first.second","stars","Peter O'Toole")
  test.deepEqual(actual,expected)
  test.done()

exports.add_on_null_should_raise_error = (test) ->
  test.throws ->
    jpath.add(null,"$.first.second","stars","Peter O'Toole")
  test.done()

exports.add_from_null_should_work = (test) ->
  actual =
    first:
      second:
        third:
          title: "How to Steal a Million"
  expected =
    first:
      second:
        stars: ["Peter O'Toole"]
        third:
          title: "How to Steal a Million"
  
  rpath = jpath.add(actual,"$.first.second","stars","Peter O'Toole")
  test.deepEqual(actual,expected)
  test.done()

exports.transform_single_should_work = (test) ->
  actual =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        third:[
            {title: "How to Steal a Million"},
            {title: "Bringing Up Baby (1938)"},
            {title: "Blade Runner (1982)"},
            {title: "Annie Hall (1977)"}
          ]
  expected =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        upper: "BONNIE AND CLYDE (1967)"
        third:[
            {title: "How to Steal a Million"},
            {title: "Bringing Up Baby (1938)"},
            {title: "Blade Runner (1982)"},
            {title: "Annie Hall (1977)"}
          ]
  
  upperc= (ctx, value) ->
    if value["title"]
      value["upper"] = value["title"].toUpperCase()
    
  selections = jpath.transform(actual,"$.first.second", [upperc])
  test.deepEqual(actual,expected)
  test.done()

exports.transform_none_should_work = (test) ->
  actual =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        third:[
            {title: "How to Steal a Million"},
            {title: "Bringing Up Baby (1938)"},
            {title: "Blade Runner (1982)"},
            {title: "Annie Hall (1977)"}
          ]
  expected =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        third:[
            {title: "How to Steal a Million"},
            {title: "Bringing Up Baby (1938)"},
            {title: "Blade Runner (1982)"},
            {title: "Annie Hall (1977)"}
          ]
  
  upperc= (ctx, value) ->
    if value["title"]
      value["upper"] = value["title"].toUpperCase()
    
  selections = jpath.transform(actual,"$.absent.second", [upperc])
  test.deepEqual(actual,expected)
  test.done()

exports.transform_array_should_work = (test) ->
  actual =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        third:[
            {title: "How to Steal a Million"},
            {title: "Bringing Up Baby (1938)"},
            {title: "Blade Runner (1982)"},
            {title: "Annie Hall (1977)"}
          ]
  expected =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        third:[
            {title: "How to Steal a Million", upper: "HOW TO STEAL A MILLION"},
            {title: "Bringing Up Baby (1938)", upper: "BRINGING UP BABY (1938)"},
            {title: "Blade Runner (1982)", upper: "BLADE RUNNER (1982)"},
            {title: "Annie Hall (1977)", upper: "ANNIE HALL (1977)"},
          ]
  
  upperc= (ctx, value) ->
    if value["title"]
      value["upper"] = value["title"].toUpperCase()
    
  selections = jpath.transform(actual,"$.first.second.third", [upperc])
  test.deepEqual(actual,expected)
  test.done()

exports.transform_all_titles_should_work = (test) ->
  actual =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        third:[
            {title: "How to Steal a Million"},
            {title: "Bringing Up Baby (1938)"},
            {title: "Blade Runner (1982)"},
            {title: "Annie Hall (1977)"}
          ]
  expected =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        upper: "BONNIE AND CLYDE (1967)"
        third:[
            {title: "How to Steal a Million", upper: "HOW TO STEAL A MILLION"},
            {title: "Bringing Up Baby (1938)", upper: "BRINGING UP BABY (1938)"},
            {title: "Blade Runner (1982)", upper: "BLADE RUNNER (1982)"},
            {title: "Annie Hall (1977)", upper: "ANNIE HALL (1977)"},
          ]
  
  upperc= (ctx, value) ->
    if value["title"]
      value["upper"] = value["title"].toUpperCase()
  
  #First title seems to be ignored. Bug ?  
  selections = jpath.transform(actual,"$..*[?(@.title)]", [upperc])
  test.deepEqual(actual,expected)
  test.done()

exports.transform_many_should_work = (test) ->
  actual =
    first:
      title: "Duck Soup (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        third:[
            {title: "How to Steal a Million"},
            {title: "Bringing Up Baby (1938)"},
            {title: "Blade Runner (1982)"},
            {title: "Annie Hall (1977)"}
          ]
  expected =
    first:
      title: "Duck Soup (1933)"
      upper: "DUCK SOUP (1933)"
      second:
        title: "Bonnie And Clyde (1967)"
        upper: "BONNIE AND CLYDE (1967)"
        third:[
            {title: "How to Steal a Million", upper: "HOW TO STEAL A MILLION"},
            {title: "Bringing Up Baby (1938)", upper: "BRINGING UP BABY (1938)"},
            {title: "Blade Runner (1982)", upper: "BLADE RUNNER (1982)"},
            {title: "Annie Hall (1977)", upper: "ANNIE HALL (1977)"},
          ]
  
  upperc= (ctx, value) ->
    if value["title"]
      value["upper"] = value["title"].toUpperCase()
  
  #First title seems to be ignored. Bug ?  
  selections = jpath.transformMany(actual,["$.first.second.third","$.first.second","$.first"], [upperc])
  test.deepEqual(actual,expected)
  test.done()
