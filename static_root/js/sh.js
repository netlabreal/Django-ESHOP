function Message(mes){
	var tmpl = '<div class="container al"><div class="col-sm-offset-8 col-sm-4"><div class="alert alert-success"><button type="button" class="close" data-dismiss="alert">X</button><span>'+mes+'</span></div></div></div>';
	$('body').append(tmpl);
	$('.al').fadeIn();

    setTimeout(function(){
		$('.al').fadeOut();        			
    	}, 1500);
};


function CartCount(rurl){
  var m = $('#kol_cart');
  $.ajax({
    type:'GET',
    url:rurl,
    success:function(data){
      m.text(data.count);
    },
    error:function(error){}
  });
};


