<template>
    <div class ="playbox">
        <div class="scorebox">
            <img src="/scores/kirakira.png">
        </div>
        <div class="videobox">
            <video id="video" width="400" height="300">
            <source src="/videos/test.mp4">
        </video>
        </div>
    </div>
</template>
<script>
    const img_src = "/scores/kirakira.png";
    const video_src = "/videos/test.mp4";
    export default {
        img_src
}   
</script>