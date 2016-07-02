given = 
  everything:
    href: "#there"
    item:
      label__title: "everything"
      abstract: "any abstract"
      image: "http://flarebyte.com/logo"
      _stats_:
        numberOfReads: 10
        numberOfVotes: 4
  no_item:
    href: "#no_item"
  item_is_null:
    href: "#there"
    item: null
  no_stats:
    href: "#there"
    item:
      label__title: "no_stats"
      abstract: "any abstract"
      image: "http://flarebyte.com/logo"
  no_image:
    href: "#there"
    item:
      label__title: "no_image"
      abstract: "any abstract"
      _stats_:
        numberOfReads: 10
        numberOfVotes: 4
  no_title:
    href: "#there"
    item:
      abstract: "no_title"
      image: "http://flarebyte.com/logo"
      _stats_:
        numberOfReads: 10
        numberOfVotes: 4
  no_abstract:
    href: "#there"
    item:
      label__title: "no_abstract"
      image: "http://flarebyte.com/logo"
      _stats_:
        numberOfReads: 10
        numberOfVotes: 4

module.exports=given
