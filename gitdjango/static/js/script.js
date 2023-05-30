//IFrame Player API の読み込み
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var ytPlayer = [];
var ytData = [
	{
		id: 'IFrrZ3j8hw4', //youtubeのID 
		area: 'IFrrZ3j8hw4', //youtubeを表示する場所
	},
	{
		id: 'zFVVHQ46xRA',
		area: 'zFVVHQ46xRA',
	},
    {
		id: 'WSrlFDzWcSc',
		area: 'WSrlFDzWcSc',
	}
];

//YouTubeの埋め込み
function onYouTubeIframeAPIReady() {
	for (var i = 0; i < ytData.length; i++) {
		ytPlayer[i] = new YT.Player(ytData[i]['area'], {
			width: 800,
			height: 450,
			videoId: ytData[i]['id'],
			playerVars: {
				rel: 0, //再生動画と同じチャンネルから関連動画を選択
				modestbranding: 1, //YouTubeロゴを表示しない
                mute: 1,
                
			},
            events:{
                'onReady': onPlayerReady,
                'onStateChange':onPlayerStateChange,
            }
		});
	}
}

function onPlayerReady(event){
    event.target.playVideo();
}



