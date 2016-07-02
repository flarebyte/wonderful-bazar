given = 
  everything:
    title: "everything"
    pageKey: "webpage"
    statKey: "numberOfComments"
    item:
      webpage: "http://flarebyte.com"
      _stats_:
        numberOfComments: 12
  no_item:
    title: "no_item"
    pageKey: "webpage"
    statKey: "numberOfComments"
  item_is_null:
    title: "items_is_null"
    pageKey: "webpage"
    statKey: "numberOfComments"
    item: null
  stats_is_null:
    title: "stats_is_null"
    pageKey: "webpage"
    statKey: "numberOfComments"
    item:
      webpage: "http://flarebyte.com"
      _stats_: null
  no_statKey_value:
    title: "no_statKey_value"
    pageKey: "webpage"
    statKey: "numberOfComments"
    item:
      webpage: "http://flarebyte.com"
      _stats_:
        numberOfReads: 12

  no_pageKey_value:
    title: "no_pageKey_value"
    pageKey: "webpage"
    statKey: "numberOfComments"
    item:
      web: "http://flarebyte.com"
      _stats_:
        numberOfReads: 12

module.exports=given
