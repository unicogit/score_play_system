<template>
    <div id="playbox">
        <div @click="onClickScore" id="scorebox" class="reltive border-2">
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
const video_src = "/videos/MVI25.mp4";
export default {
    props: {
        points: {
            type: Array,
        },
        timestamp: {
            type: Array,
        },
    },
    computed: {
    },
    methods: {
        onClickScore(e) {
            console.log('offset:', e.offsetX, e.offsetY)
            console.log('pos:', e.x, e.y)

            const points = []
            const timestamp = this.timestamp

            for (let i = 0; i < this.points.length; i++) {
                const point = this.points[i];
                points.push(point.map(x => x / 10))
            }
            
            console.log('points:', points)
            console.log('timestamp:', timestamp)
        }
    },
}

</script>

<style>
    /* viewer用css */
    #playbox{
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        color: blue;
    }
    #scorebox{
        width: 40%;
        padding: 20px 10px;
    }
    .videobox{
        width: 60%;
        padding: 20px 10px;
    }
</style>