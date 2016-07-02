given = 
  everything:
    pageKey: "webpage"
    item:
      webpage: "http://flarebyte.com"
      label__title: "everything"
      abstract: "any abstract"
      image: "http://flarebyte.com/logo"
      _stats_:
        numberOfReads: 10
        numberOfVotes: 4
  no_item:
    pageKey: "webpage"
  item_is_null:
    pageKey: "webpage"
    item: null
  no_stats:
    pageKey: "webpage"
    item:
      webpage: "http://flarebyte.com"
      label__title: "no_stats"
      abstract: "any abstract"
      image: "http://flarebyte.com/logo"
  no_image:
    pageKey: "webpage"
    item:
      webpage: "http://flarebyte.com"
      label__title: "no_image"
      abstract: "any abstract"
      _stats_:
        numberOfReads: 10
        numberOfVotes: 4
  no_title:
    pageKey: "webpage"
    item:
      webpage: "http://flarebyte.com"
      abstract: "no_title"
      image: "http://flarebyte.com/logo"
      _stats_:
        numberOfReads: 10
        numberOfVotes: 4
  no_abstract:
    pageKey: "webpage"
    item:
      webpage: "http://flarebyte.com"
      label__title: "no_abstract"
      image: "http://flarebyte.com/logo"
      _stats_:
        numberOfReads: 10
        numberOfVotes: 4

module.exports=given
