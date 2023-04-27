<template>
    <div>
      <video ref="video" 
        autoplay muted playsinline 
        width="800"
        height="600"
        :style="{ objectFit: 'contain' }"></video>
      <button
        v-if="!isRecording"
        class="ml-6 rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        @click="startRecording"
      >
        録画開始
      </button>
      <button
        v-if="isRecording"
        class="ml-6 rounded-md border border-transparent bg-red-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
        @click="stopRecording"
      >
        録画終了
      </button>
      <button
        class="ml-6 rounded-md border border-transparent bg-yellow-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-yellow-700 focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:ring-offset-2"
        @click="toggleCamera"
        >
        カメラ切り替え
        </button>
      <a
            v-show="showDownloadLink"
            ref="downloadLink"
            download="recorded-video.mp4"
      >
        動画のダウンロード
      </a>
      <button
        class="ml-6 rounded-md border border-transparent bg-blue-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        @click="goBack"
        >
        戻る
    </button>
    </div>
  </template>
  
  <script>
  import { Inertia } from '@inertiajs/inertia'; // 追加: Inertia.js のインポート

  export default {
    data() {
      return {
        videoStream: null,
        mediaRecorder: null,
        chunks: [],
        isRecording: false,
        showDownloadLink: false,
        facingMode: "user", // 追加: カメラの向き (初期値は内向き)
      };
    },
    mounted() {
      this.initializeCamera();
    },
    methods: {
      async initializeCamera() {
        try {
          this.videoStream = await navigator.mediaDevices.getUserMedia({
            video: {
                facingMode: this.facingMode, // 追加: カメラの向きを指定
            },
            audio: true,
          });
  
          this.$refs.video.srcObject = this.videoStream;
        } catch (error) {
          console.error("Error accessing camera:", error);
        }
      },
      async toggleCamera() {
            this.facingMode = this.facingMode === "user" ? "environment" : "user";
            await this.initializeCamera();
        },
        goBack() {
            Inertia.visit(document.referrer);
        },
      startRecording() {
        this.isRecording = true;
        this.chunks = [];
        this.mediaRecorder = new MediaRecorder(this.videoStream);
  
        this.mediaRecorder.ondataavailable = (event) => {
          if (event.data.size > 0) {
            this.chunks.push(event.data);
          }
        };
  
        this.mediaRecorder.onstop = () => {
          this.saveVideo();
          this.isRecording = false;
          this.showDownloadLink = true;
        };
  
        this.mediaRecorder.start();
      },
      stopRecording() {
        if (this.mediaRecorder && this.mediaRecorder.state !== "inactive") {
          this.mediaRecorder.stop();
        }
      },
      saveVideo() {
        const blob = new Blob(this.chunks, { type: "video/mp4" });
        const url = URL.createObjectURL(blob);
  
        this.$refs.downloadLink.href = url;
      },
    },
  };
  </script>
  