$(document).ready(function(){

	$( ".clip" ).attr( "data-clipboard-text", "" + window.location.host + "/careers/#panel1" );
	$( ".clip2" ).attr( "data-clipboard-text", "" + window.location.host + "/careers/#panel2" );
	$( ".clip3" ).attr( "data-clipboard-text", "" + window.location.host + "/careers/#panel3" );
	$( ".clip4" ).attr( "data-clipboard-text", "" + window.location.host + "/careers/#panel4" );
    $( ".clip5" ).attr( "data-clipboard-text", "" + window.location.host + "/careers/#panel5" );

	var clipboard = new Clipboard('.clipboard');

	clipboard.on('success', function(e) {
		$(e.trigger).children().show();
		$('.copied').delay(500).fadeOut('slow');
		e.clearSelection();
	});


	$('.panel-collapse').on('show.bs.collapse',function(){
	    $(this).prev('.panel-heading').addClass("active");
	});

	$('.panel-collapse').on('hide.bs.collapse',function(){
	    $(this).prev('.panel-heading').removeClass("active");
	});

	var str2 = window.location.hash;
	$(str2).children(".panel-collapse").addClass('in').removeClass('collapse').prev(".panel-heading").toggleClass('active');

	var str = location.href.toLowerCase();
	$('li.active').removeClass("active");
	$('.nav li a').filter(function() {return this.href.toLowerCase() == str; }).parents('li').addClass('active');
     
          
});