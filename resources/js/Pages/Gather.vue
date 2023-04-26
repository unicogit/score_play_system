<style>
#camera-controll-wrapper{
  border: 1px solid black;
}
</style>
<template>
    <div>
      <input type="text" name="lesson-name" id="lesson-name" v-model="lessonName">
      <button @click="createURL">QRコードを生成</button>
      <canvas id="qr-code-wrapper">
      </canvas>
      <button @click="showQRCode = true">Show QR Code</button>
    </div>
    <div v-if="isGenerated" id="camera-control-wrapper">
      <button @click="bcToggleRecording" >撮影ボタン</button><br>
      <button v-if="isRecorded" @click="bcUpload">アップロード</button>
      <br>
      <a href="/record">録画画面へ移動</a>
    </div>
  </template>
  
  <script>
  import { Head } from '@inertiajs/inertia-vue3';
  import QRious from 'qrious';
  import Qrcode from '@/Components/QRCode.vue';
  
  export default {
    components: { Qrcode },
    props: {
      user: {
        type: Array,
      },
      size: {
        type: Number,
        default: 400
      },
    },
    data() {
      return {
        showQRCode: false,
        lessonName: '',
        qrCodeUrl: '',
        isGenerated: false,
        isRecorded: false,
      }
    },
    mounted() {
    this.user = window.Jetstream.inertia.user;
    },
    methods: {
      createURL(){
        this.qrCodeUrl = 'https://scoreplaysystem.unico-unique.com/record/' + this.user.name + '/' + this.lessonName;
        var qrWrapper = document.getElementById('qr-code-wrapper');
        
        const qr = new QRious({
        element: qrWrapper,
        value: this.qrCodeUrl,
        size: this.size
      });
      console.log('generated');
      this.isGenerated = true;
      },
      bcToggleRecording(){
        //TODO 撮影中なら撮影を終了し、それ以外なら撮影を開始するbcメッセージを送信
        this.isRecorded = true;
      }
    }
  }
  </script>
  