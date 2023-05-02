<template>
    <div id="playbox">
        <div id="scorebox" class="reltive border-2">
            {{ currentImage }}
                <img
                @click="onClickScore"
                :src="currentImage || preview"
                alt="Image Preview"
                class="image-preview"
            />
            <canvas
                v-if="drawing"
                ref="canvas"
                :class="{ 'transparent-canvas': drawing }"
                @mousedown="startDrawing"
                @mousemove="draw"
                @mouseup="stopDrawing"
            ></canvas>
            <!-- <button type="submit">アップロード</button> -->
            <!-- <button @click="toggleDrawing" type="button" class="rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">描画</button> -->
        </div>
        <div id="videos-wrapper">
            <div class="videobox" v-for="practice in data" :key="practice.id">
                <video
                    :src="practice.video"
                    :id="practice.id"
                    width="30%"
                    controls
                    autobuffer
                >
                    <!-- <source v-if="videoview" :src="videoview" /> -->
                </video>
            </div>

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
            default: () => [],
        },
        src : {
            type: String,
        },
        data:{
            type: Array,
            default: () => [], // デフォルト値を設定する
        } 
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
            drawing: false,
            currentPageIndex: 0,
            imagePaths: [],
        };
    },
    computed: {
    // currentImage() {
    //   if (this.practices.length) {
    //     return this.practices[this.currentPageIndex].score.image_path;
    //   }
    //   return "";
    // },
    },
    mounted() {
        this.$watch("uploadedImage", (newImage) => {
            if (newImage) {
                this.initializeCanvas();
            }
        });
        console.log(this.data);
    },
    methods: {
        
        previewImage(event) {
        this.image = event.target.files[0];
        this.preview = URL.createObjectURL(this.image);
        console.log(this.preview);
        this.loadImageToCanvas();
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
        // nextPage() {
        // if (this.currentPageIndex < this.practices.length - 1) {
        //     this.currentPageIndex++;
        // }
        // },
        prevPage() {
        if (this.currentPageIndex > 0) {
            this.currentPageIndex--;
        }
        },

        loadImageToCanvas() {
            if (!this.preview) return;

            const img = new Image();
            img.src = this.preview;
            img.onload = () => {
            this.$refs.canvas.width = img.width;
            this.$refs.canvas.height = img.height;
            this.context = this.$refs.canvas.getContext("2d");
            this.context.drawImage(img, 0, 0);
            this.drawing = false;
            };
        },
        toggleDrawing() {
            this.drawing = !this.drawing;
        },
        startDrawing(event) {
            this.drawing = true;
            this.context.beginPath();
            this.context.moveTo(event.offsetX, event.offsetY);
        },
        draw(event) {
            if (!this.context || !this.drawing) return;
            this.context.lineTo(event.offsetX, event.offsetY);
            this.context.stroke();
        },
        stopDrawing() {
            this.drawing = false;
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
            // if (!this.timestamp.length) {
            //     console.log('Timestamp array is empty');
            //     return;
            // }
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
canvs,
.image-preview {
  max-width: 100%;
  max-height: 100%;
  display: block;
  object-fit: contain;
  z-index: 1;
}
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
.transparent-canvas {
    z-index: 2;
    opacity: 0.8;
}
</style>
