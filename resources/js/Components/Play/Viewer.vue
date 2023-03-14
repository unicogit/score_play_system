<template>
    <div id="playbox">
        <div @click="onClickScore" id="scorebox" class="reltive border-2">
            <img :src="imgSrc" />
        </div>
        <div class="videobox">
            <video
                ref="video"
                id="video"
                width="400"
                height="300"
                controls
                autobuffer
            >
                <source :src="videoSrc" />
            </video>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        points: {
            type: Array,
        },
        timestamp: {
            type: Array,
        },
    },
    data() {
        return {
            imgSrc: "/scores/chart.png",
            videoSrc: "/videos/MVI_24.mp4",
        };
    },
    computed: {},
    methods: {
        onClickScore(e) {
            const x = e.offsetX;
            const y = e.offsetY;
            // console.log(x, y);

            const points = [];
            const timestamp = this.timestamp;

            for (let i = 0; i < this.points.length; i++) {
                const point = this.points[i];
                points.push(point.map((x) => x / 10));
            }

            // console.log("points:", points);
            // console.log("timestamp:", timestamp);

            /*----------------------------------------------------
                1列目
            -----------------------------------------------------*/
            if (32 <= x && x < 100 && 60 <= y && y <= 90) {
                this.onClickMeasure(0);
            }
            if (100 <= x && x < 150 && 60 <= y && y <= 90) {
                this.onClickMeasure(1);
            }
            if (150 <= x && x < 200 && 60 <= y && y <= 90) {
                this.onClickMeasure(2);
            }
            if (200 <= x && x < 250 && 60 <= y && y <= 90) {
                this.onClickMeasure(3);
            }
            /*----------------------------------------------------
                2列目
            -----------------------------------------------------*/
            if (20 <= x && x < 80 && 120 <= y && y <= 150) {
                this.onClickMeasure(4);
            }
            if (80 <= x && x < 140 && 120 <= y && y <= 150) {
                this.onClickMeasure(5);
            }
            if (140 <= x && x < 200 && 120 <= y && y <= 150) {
                this.onClickMeasure(6);
            }
            if (200 <= x && x < 260 && 120 <= y && y <= 150) {
                this.onClickMeasure(7);
            }
            /*----------------------------------------------------
                3列目
            -----------------------------------------------------*/
            if (20 <= x && x < 80 && 180 <= y && y <= 210) {
                this.onClickMeasure(8);
            }
            if (80 <= x && x < 140 && 180 <= y && y <= 210) {
                this.onClickMeasure(9);
            }
            if (140 <= x && x < 200 && 180 <= y && y <= 210) {
                this.onClickMeasure(10);
            }
            if (200 <= x && x < 260 && 180 <= y && y <= 210) {
                this.onClickMeasure(11);
            }
        },
        onClickMeasure(index) {
            const media = this.$refs.video;
            console.log(this.timestamp[index][1]+7.5)
            media.currentTime = this.timestamp[index][1] + 7.5;
            media.play();
        },
    },
};
</script>

<style>
/* viewer用css */
#playbox {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    color: blue;
}
#scorebox {
    width: 40%;
    padding: 20px 10px;
}
.videobox {
    width: 60%;
    padding: 20px 10px;
}
</style>
