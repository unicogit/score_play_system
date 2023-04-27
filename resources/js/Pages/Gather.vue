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
    </div>
    <div v-if="isGenerated" id="camera-control-wrapper">
      <button @click="bcToggleRecording" >撮影{{ ctlrButton }}</button><br>
      <button v-if="isRecorded" @click="bcUpload">アップロード</button>
      <br>
      <a :href="qrCodeUrl">録画画面へ移動</a>
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
        status: '開始',
        onRec: false,
        ctlrButton: '開始',
      }
    },
    mounted() {
    this.user = window.Jetstream.inertia.user;
    },
    methods: {
      createURL(){
        // this.qrCodeUrl = 'https://scoreplaysystem.unico-unique.com/record/' + this.user.id + '/' + this.lessonName;
        this.qrCodeUrl = '/record/' + this.user.id + '/' + this.lessonName;

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
        this.onRec = !this.onRec;
        this.status = this.onRec? '開始' : '終了';
        this.ctlrButton = this.onRec ? '終了' : '開始';
        var params = {
            'status': this.status,
        };
        axios.post(route('record.create'), params)
        .then(res=>{
            console.log('create' + params);
            console.log(res);
        })
        .catch(e=>{
            console.log('broadcast error');
            console.log(e.response);
        });
      },
      bcUpload: function(){
        axios.post(route('record.upload'))
        .then(res=>{
            console.log('uploaded: ');
            console.log(res);
        })
        .catch(e=>{
            console.log('upload error: ');
            console.log(e.response);
        });
      },
    }
  }
  </script>
  