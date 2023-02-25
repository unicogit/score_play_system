<template>
    <div id ="playbox">
        <div id="scorebox">
            <img src="/scores/kirakira.png">
        </div>
        <div class="videobox">
            video
            <video id="video" width="400" height="300">
            <source src="/videos/test.mp4">
        </video>
        </div>
    </div>
</template>
<script>
    const img_src = "/scores/kirakira.png";
    const video_src = "/videos/test.mp4";
        window.onload = function () {
        document.getElementById("playbox").addEventListener( "click", function( event ) { {
        var clickX = event.pageX ;
        var clickY = event.pageY ;

        // 要素の位置を取得
        var clientRect = this.getBoundingClientRect() ;
        var positionX = clientRect.left + window.pageXOffset ;
        var positionY = clientRect.top + window.pageYOffset ;

        // 要素内におけるクリック位置を計算
        var x = clickX - positionX ;
        var y = clickY - positionY ;
        console.log(x,y)
        }    
    }) 
    // if(x = 130 <= ){ 
    // video.currentTime= 30;
    // video.play()
    // }
    }
    export default {
        img_src
}

</script>