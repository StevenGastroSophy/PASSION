$(document).ready(function(){

	var val = 1;

  $(".nav-bar").click(function(){


  	if (val == 1) {

	  	$("header nav").animate({
	    	'left' : '0'
	    });
		$(".nav-bar i").toggleClass("fa fa-bars").toggleClass("fa fa-close");
	    val = 0;
  	}else{
  		val = 1;
  		$("header nav").animate({
		    'left' : '-100%'
		});
		$(".nav-bar i").toggleClass("fa fa-close").toggleClass("fa fa-bars");
  	}



    return false;
  });
  
  $(window).resize(function() {
        wdth=$(window).width();
		if (wdth > 800) {
		$("header nav").animate({
	    	'left' : '0'
	    });
	}else {
        $("header nav").animate({
		    'left' : '-100%'
		});
		val = 1;
    }
	    var navclass = $(".nav-bar i").attr("class");
		if (navclass == "fa fa-close") {
		$(".nav-bar i").toggleClass("fa fa-close").toggleClass("fa fa-bars");
	}
    });
  
  // submenu
  $('.sub-menu').click(function(){
  	$(this).children('.children').slideToggle();
  })

}); 