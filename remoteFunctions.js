function switchPanel(panelID) {
	$('.panel').addClass('hidden');
	$(panelID).removeClass('hidden');
}

var remote = {
	'setBackgroundColor' : function(args) {
		var argParts = args.split(" ");
		var r = parseInt(argParts[0]);
		var g = parseInt(argParts[1]);
		var b = parseInt(argParts[2]);
		var a = parseInt(argParts[3]);
		var time = parseInt(argParts[4]);
	
		$('body').animate({
			backgroundColor: 'rgba(' + r + ', ' + g + ', ' + b + ', ' + a + ')',
		}, time);
	},
	'setGlow' : function(args) {
		var argParts = args.split(" ");
		var size = parseFloat(argParts[0]);
		var rgba = 'rgba(' + parseInt(argParts[1]) + ', ' + parseInt(argParts[2]) + ', ' + parseInt(argParts[3]) + ', ' + parseInt(argParts[4]) + ')';
		var time = parseInt(argParts[5]);
		
		switchPanel("#glowPanel");
	
		$('#glowPanel').stop().animate({
			backgroundColor: rgba,
			width: size * $('body').width(),
			height: size * $('body').height(),
			boxShadow: '0 0 ' + size * 80 + 'px ' + size * 60 + 'px ' + rgba
		}, time);
	},
	'playSong' : function(args) {
		switchPanel("#audioPanel");
		remote['stopVideo']();
		
		var player = $('#audioPlayer').get(0);
		player.pause();
		player.src = args;
		player.load();
		player.play();
	},
	'pauseMusic' : function pauseMusic(args) {
		var player = $('#audioPlayer').get(0);
		player.pause();
	},
	'playYoutubeVideo' : function(args) {
		switchPanel("#videoPanel");
		remote['pauseMusic']();
		
		var argParts = args.split(" ");
		jQuery("#youtube-player-container").tubeplayer("play", {
			id: argParts[0],
			time: parseInt(argParts[1])
		});
	},
	'stopVideo' : function(args) {
		jQuery("#youtube-player-container").tubeplayer("stop");
	},
};
