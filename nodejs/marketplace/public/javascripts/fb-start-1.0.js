console.log("hello");

$('noscript[data-src]').each(function(){
  var src = screen.width >= 500 ? $(this).data('src')+"/150x150/i.png" : $(this).data('small')+"/48x48/i.png";
  $('<img src="' + src + '" alt="' + $(this).data('alt') + '" />').insertAfter($(this));
});