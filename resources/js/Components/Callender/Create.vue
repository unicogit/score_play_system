<template>
    <div>
      <h1>練習登録</h1>
      <video
        ref="video"
        autoplay
        muted
        playsinline
        width="800"
        height="600"
        :style="{ objectFit: 'contain' }"
      ></video>
      <button
        v-if="!isRecording"
        @click="startRecording"
      >
        録画開始
      </button>
      <button
        v-if="isRecording"
        @click="stopRecording"
      >
        録画終了
      </button>
      <button @click="toggleCamera">
        カメラ切り替え
      </button>
      <a
        v-show="showDownloadLink"
        ref="downloadLink"
        download="recorded-video.mp4"
      >
        動画のダウンロード
      </a>
      <!-- フォームのコードをここに追加 -->
      <form @submit.prevent="submitForm">
        <label>
          タイトル:
          <input type="text" v-model="title" required />
        </label>
        <label>
          練習日:
          <input type="date" v-model="practiceDate" required />
        </label>
        <label>
          楽譜:
          <select v-model="scoreId">
            <option disabled value="">選択してください</option>
            <option
              v-for="score in scores"
              :key="score.id"
              :value="score.id"
            >
              {{ score.name }}
            </option>
          </select>
        </label>
        <button type="submit">登録</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: {
      scores: Array,
    },
    data() {
      return {
        title: "",
        practiceDate: "",
        scoreId: "",
        videoStream: null,
        mediaRecorder: null,
        chunks: [],
        isRecording: false,
        showDownloadLink: false,
        facingMode: "user",
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
              facingMode: this.facingMode,
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
          this.saveVideo
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
async submitForm() {
  const videoBlob = new Blob(this.chunks, { type: "video/mp4" });
  const formData = new FormData();

  formData.append("title", this.title);
  formData.append("practice_date", this.practiceDate);
  formData.append("score_id", this.scoreId);
  formData.append("video", videoBlob, "recorded-video.mp4");

  try {
    const response = await axios.post("/practice/create", formData);
    console.log(response);
    alert("練習が登録されました");
  } catch (error) {
    console.error("Error submitting form:", error);
  }
},
},
};
</script>  