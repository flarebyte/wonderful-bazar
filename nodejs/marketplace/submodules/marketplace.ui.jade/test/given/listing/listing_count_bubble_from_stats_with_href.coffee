given = 
  everything:
    title: "everything"
    href: "#there"
    statKey: "numberOfComments"
    item:
      _stats_:
        numberOfComments: 12
  no_item:
    title: "no_item"
    href: "#there"
    statKey: "numberOfComments"
  item_is_null:
    title: "items_is_null"
    href: "#there"
    statKey: "numberOfComments"
    item: null
  stats_is_null:
    title: "stats_is_null"
    href: "#there"
    statKey: "numberOfComments"
    item:
      _stats_: null
  no_statKey_value:
    title: "no_statKey_value"
    href: "#there"
    statKey: "numberOfComments"
    item:
      _stats_:
        numberOfReads: 12

module.exports=given
