<template>
    <div id="playbox">
        <div id="scorebox" class="reltive border-2">
            <form @submit.prevent="submitForm">
            <input type="file" ref="image" @change="previewImage" />
            <img @click="onClickScore" v-if="preview" :src="preview" alt="Image Preview" />
            <!-- <button type="submit">アップロード</button> -->
            </form>
        </div>
        <div class="videobox">
            <form @submit.prevent="submitFormVideo">
            <input type="file" ref="video" @change="previewVideo" />
            <video
                id="video"
                width="400"
                height="300"
                controls
                autobuffer
            >
                <source v-if="videoview" :src="videoview" />
            </video>
            </form>
        </div>
    </div>
</template>
<script>
import axios from "axios";

export default {
    props: {
        points: {
            type: Array,
        },
        timestamp: {
            type: Array,
        },
        src : {
            type: String,
        },
        practices: [],
    },
    data() {
        return {
            imgSrc: "/scores/kirakira.png",
            // videoSrc: "/videos/MVI_25.mp4",
            videoSrc: this.src,
            isPlaying: false,
            image: null,
            imageLoaded: false,
            uploadedImage: "",
            preview: "",
            videoview: "",
            context: null,
            lineColor: "black",
            lineWidth: 5,
            initialized: false,
        };
    },
    mounted() {
        this.$watch("uploadedImage", (newImage) => {
            if (newImage) {
                this.initializeCanvas();
            }
        });
    },
    methods: {
        previewImage(event) {
        this.image = event.target.files[0];
        this.preview = URL.createObjectURL(this.image);
        console.log(this.preview);
        },
        async submitForm() {
        if (!this.image) return;

        const formData = new FormData();
        formData.append("image", this.image);

        try {
            const response = await axios.post("/upload-image", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
            });

            this.uploadedImage = response.data.path; // 追加
            console.log("アップロード成功", response.data);
        } catch (error) {
            console.error("アップロード失敗", error);
        }
        },

        previewVideo(event) {
        const video = event.target.files[0];
        this.videoview = URL.createObjectURL(video);
        console.log(this.videoview);
        },
        async submitFormVideo() {
        if (!this.video) return;

        const formData = new FormData();
        formData.append("video", this.video);
        try {
            const response = await axios.post("/upload-video", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
            });

            this.uploadedVideo = response.data.path; // 追加
            console.log("アップロード成功", response.data);
        } catch (error) {
            console.error("アップロード失敗", error);
        }
        },
        onClickScore(e) {
            const x = e.offsetX;
            const y = e.offsetY;
            console.log(x, y);

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
        togglePlayback(){
            this.isPlaying = !this.isPlaying
            this.$refs.video.forEach(video => {
                if (this.isPlaying) {
                video.play()
                } else {
                video.pause()
                }
            })
        }
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
canvas {
    width: 40%;
    padding: 20px 10px;
    border: 1px solid black;
}
</style>
