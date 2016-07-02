tester = require('./tester')

exports.listing_stats_span_views_likes_should_work = (test) ->
  tester.createExpected(test, "listing/listing_stats_span_views_likes")
  
exports.listing_thumbnail_with_href_should_work = (test) ->
  tester.createExpected(test, "listing/listing_thumbnail_with_href")

exports.listing_thumbnail_with_link_to_page_should_work = (test) ->
  tester.createExpected(test, "listing/listing_thumbnail_with_link_to_page")

exports.listing_count_bubble_from_stats_with_href_should_work = (test) ->
  tester.createExpected(test, "listing/listing_count_bubble_from_stats_with_href")

exports.listing_count_bubble_from_stats_with_link_to_page_should_work = (test) ->
  tester.createExpected(test, "listing/listing_count_bubble_from_stats_with_link_to_page")

