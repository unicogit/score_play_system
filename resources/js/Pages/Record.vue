<script setup>
import { Head } from '@inertiajs/inertia-vue3'
</script>
<template>
    <Head>
        <title>撮影画面</title>
        <link rel="stylesheet" href='css/record.css'>
    </Head>
    <div id="app">
        <button v-on:click="recording = !recording">record</button>
        <div v-show="videoavailable">
            <button v-on:click="download">download</button>
        </div>
        <div id="video-container">
            <video id="video"></video>
        </div>
    </div>
</template>
<script>
var constrains = { video: true, audio: true }// 映像・音声を取得するかの設定
var recorder = null;
var chunks = []
export default {
    name: 'app',
    mounted() {
        //カメラにアクセスする処理
        var video = document.getElementById('video');
        navigator.mediaDevices.getUserMedia(constrains)
        .then(function(stream) {
            video.srcObject = stream // streamはユーザーのカメラとマイクの情報で、これをvideoの入力ソースにする
            video.play();
            recorder = new MediaRecorder(stream) // 映像の入力ソースをユーザーのデバイスから取得
            recorder.ondataavailable = function (e) {
                if(e.data.size > 0){
                    chunks.push(e.data);
                }
            }
        })
        .catch(function(err) {
            console.log("An error occured! " + err)
        })
    },
    data: function(){
        return {
            recording: false,
            videoavailable: false,
        }
    },
    methods: {
        download: function(){
            var blob = new Blob(chunks, {"type": 'video¥/mp4'})
            var url = window.URL.createObjectURL(blob) // データにアクセスするためのURLを作成
            var rec_video = document.createElement('video')
            document.body.appendChild(rec_video)
            rec_video.src = url
            rec_video.controls = true
            rec_video.style = 'width: 100vw; height: 100vh'
            var a = document.createElement('a') // download属性を持ったaタグをクリックするとダウンロードができるので、それをシミュレートする
            document.body.appendChild(a)
            a.style = 'display:none'
            a.href = url;
            a.download = 'test.mp4'
            a.click()
            window.URL.revokeObjectURL(url)
        },

    },
    watch: {
        recording: function(newVal){
            if(newVal){
                //record start
                recorder.start()
            }else{
                //record stop
                recorder.stop()
                this.videoavailable = true
            }
        }
    }
}
</script>