<template>
    <div class="flexbox">
        <div id="score-wrapper">
            <form @submit.prevent="submitForm">
                <input type="file" ref="image" @change="previewImage" />
                <button type="submit">アップロード</button>
            </form>
            <button @click="togglePlayback">{{ isPlaying ? '一時停止' : '再生'}}</button>
            <div
            @click="onClickScore"
            id="scorebox"
            class="relative border-2"
            style="position: relative;"
            >
                <!-- :src="preview" -->
                <img
                    v-if="preview"
                    :src="displayImage"
                    alt="Image Preview"
                    style="position: absolute;"
                />
                <img :src="uploadedImage" style="position: absolute;" />
                <!-- <canvas
                    ref="canvas"
                    @mousedown="startPaint"
                    @mousemove="paint"
                    @mouseup="stopPaint"
                    @mouseleave="stopPaint"
                    style="position: absolute;"
                ></canvas> -->
            </div>
        </div>
        <div id="videos-wrapper">
            <div class="videobox" v-for="practice in practices" :key="practice.id">
                <video
                    ref="video"
                    class="video"
                    autobuffer
                >
                    <source :src="practice.video" />
                </video>
            </div>
        </div>
    </div>

    
        <!-- <div id="playbox">
            
            <div id="playbox">
                <canvas
                ref="canvas"
                @mousedown="startPaint"
                @mousemove="paint"
                @mouseup="stopPaint"
                @mouseleave="stopPaint"
                ></canvas>
                <div @click="onClickScore" id="scorebox" class="reltive border-2">
                <img v-if="preview" :src="preview" alt="Image Preview" />
                <img :src="uploadedImage" />
                </div>
                <canvas ref="canvas" @click="onClick"></canvas>
                <div @click="onClickScore" id="scorebox" class="reltive border-2">
                    <img v-if="preview" :src="preview" alt="Image Preview" />
                    <img :src="uploadedImage" />
                </div>
            </div>
            

            <div class="videobox">
                <form method="POST" action="/upload" enctype="multipart/form-data">
                @csrf
                <input type="file" name="video" @change="setVideo" />
                <button type="submit">Upload</button>
                </form>
                <div v-if="videoPath">
                <video :src="videoPath" ref="video" controls></video>
            </div> -->
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
        console.log(this.practices);
    },
    watch: {
    uploadedImage(newImage) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
            this.uploadedImage = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    },
    },
    computed: {
        displayImage() {
        if (this.uploadedImage) {
            this.initializeCanvas();
        }
        return this.uploadedImage;
        },
    },
    methods: {
        
        previewImage(event) {
            this.image = event.target.files[0];
            this.preview = URL.createObjectURL(this.image);
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

            // this.$inertia.reload();
            this.uploadedImage = response.data.path;
            console.log("アップロード成功", response.data);
        } catch (error) {
            console.error("アップロード失敗", error);
        }
        },
        initializeCanvas() {
            const canvas = this.$refs.canvas;
            const context = canvas.getContext("2d");
            this.context = context;

            const img = new Image();
            img.src = this.uploadedImage;
            img.onload = () => {
                canvas.width = img.width;
                canvas.height = img.height;
                context.drawImage(img, 0, 0);
                context.strokeStyle = this.lineColor;
                context.lineWidth = this.lineWidth;

                this.initialized = true;
            };
        },
        startPaint(event) {
            if (!this.initialized) return;

            this.context.beginPath();
            this.context.moveTo(event.clientX, event.clientY);
                },
        paint(event) {
            if (!this.initialized) return;

            this.context.lineTo(event.clientX, event.clientY);
            this.context.stroke();
        },
        stopPaint() {
            if (!this.initialized) return;

            this.context.closePath();
        },
        onClick(event) {
            this.context.fillStyle = "red";
            this.context.beginPath();
            this.context.arc(
                event.clientX -
                this.$refs.canvas.getBoundingClientRect().left -
                window.pageXOffset,
                event.clientY -
                this.$refs.canvas.getBoundingClientRect().top -
                window.pageYOffset,
                5, // 半径（サイズを調整）
                0,
                2 * Math.PI
            );
            this.context.fill();
            this.context.closePath();
        },
        startPaint(event) {
            this.painting = true;
            this.context.beginPath();
            this.context.moveTo(event.clientX - this.$refs.canvas.offsetLeft, event.clientY - this.$refs.canvas.offsetTop);
        },
        paint(event) {
            if (!this.painting) return;
            this.context.lineTo(event.clientX - this.$refs.canvas.offsetLeft, event.clientY - this.$refs.canvas.offsetTop);
            this.context.stroke();
        },
        stopPaint() {
            if (!this.painting) return;
            this.painting = false;
            this.context.closePath();
        },
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
.flexbox{
    display: flex;
}
#score-wrapper{
    height: 100vh;
    width: 50vw;
}
#playbox {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    color: blue;
}
#scorebox {
    width: 40%;
}
#videos-wrapper{
    width: 50vw;
    background-color: gray;
}
.videobox {
    height: fit-content;
}
canvas {
    width: 40%;
    padding: 20px 10px;
    border: 1px solid black;
}
</style>
