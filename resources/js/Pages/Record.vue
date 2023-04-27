<script setup>
import { Head } from '@inertiajs/inertia-vue3';
import axios from 'axios';
</script>
<style>
.recording{
    border: 3px solid red;
}
</style>
<template>
    <Head>
        <title>撮影画面</title>
        <link rel="stylesheet" href='css/record.css'>
    </Head>
    <div id="app">
        <!-- <button @click="broadcast">{{ record_status }}</button> -->
        <div v-show="videoavailable">
            <button v-on:click="download">録画をダウンロード</button><br>
            <button @click="upload">録画をアップロード</button>
            <!-- <form :action="route('record.store')" method="post" enctype="multipart/form-data">
                <input type="text" name="title">
                <input type="file" name="video" accept="video/mp4"><br>
                <input type="submit" value="選択した動画をアップロード">
            </form> -->
        </div>

        <div id="video-container">
            <video id="video" v-bind:class="{recording: recording}"></video>
        </div>
    </div>
</template>
<script>
var constrains = { video: true, audio: true }// 映像・音声を取得するかの設定
var recorder = null;
var chunks = []
export default {
    name: 'app',
    props: {
        userID: String,
        lessonName: String,
    },
    data: function(){
        return {
            recording: false,
            videoavailable: false,
            record_status: '録画開始',
        }
    },
    mounted() {

        console.log(this.userID + '/' + this.lessonName);
        //カメラにアクセスする処理
        var video = document.getElementById('video');
        video.volume = 0;
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
        });
        window.Echo.channel('multi_record').listen('RecordingStart', (e)=>{
            console.log('RecordingStart');
            console.log(e);
            var status = e.message.status;
            this.recording = status == '開始' ? true : false;
        });
        window.Echo.channel('multi_record').listen('UploadBlob', (e)=>{
            console.log('UploadBlob');
            console.log(e);
        });
        window.Echo.channel('multi_record').listen('UploadBlob', (e)=>{
            console.log('UploadBlob');
            console.log(e);
            let blob = new Blob(chunks, {"type": 'video¥/mp4'})
            let formData = new FormData();
            let date = new Date();
            formData.append('video', blob);
            formData.append('title', this.lessonName);
            formData.append('practice_date', 
                date.getFullYear() + '-' 
                + (date.getMonth()+1) + '-' 
                + date.getDate()
            );

            axios.post(route('record.store'), formData)
            .then(res=>{
                console.log(res);
            })
            .catch(e=>{
                console.log(e);
            });
        })
    },
    methods: {
        // download: function(){
        //     var blob = new Blob(chunks, {"type": 'video¥/mp4'})
        //     var url = window.URL.createObjectURL(blob) // データにアクセスするためのURLを作成
        //     var rec_video = document.createElement('video')
        //     document.body.appendChild(rec_video)
        //     rec_video.src = url
        //     rec_video.controls = true
        //     rec_video.style = 'width: 100vw; height: 100vh'
        //     var a = document.createElement('a') // download属性を持ったaタグをクリックするとダウンロードができるので、それをシミュレートする
        //     document.body.appendChild(a)
        //     a.style = 'display:none'
        //     a.href = url;
        //     a.download = 'test.mp4'
        //     a.click()
        //     window.URL.revokeObjectURL(url)
        // },
        // toggle_record: function(){
        //     this.recording = !this.recording
        // },
        // broadcast: function(){
        //     //console.log('broadcast');
        //     this.recording = !this.recording;
        //     var params = {
        //         'status': this.recording,
        //     };
        //     axios.post(route('record.create'), params)
        //     .then(res=>{
        //         console.log('create');
        //         console.log(res);
        //     })
        //     .catch(e=>{
        //         console.log('broadcast error');
        //         console.log(e.response);
        //     });
        // },
        // upload: function(){
        //     axios.post(route('record.upload'))
        //     .then(res=>{
        //         console.log('uploaded: ');
        //         console.log(res);
        //     })
        //     .catch(e=>{
        //         console.log('upload error: ');
        //         console.log(e.response);
        //     });
        // },
    },
    watch: {
    //     recording: function(newVal){
    //         if(newVal){
    //             //record start
    //             recorder.start();
    //             this.record_status = '撮影終了';
    //         }else{
    //             //record stop
    //             recorder.stop();
    //             this.videoavailable = true;
    //             this.record_status = '撮影開始';
    //         }
    //     }
    }
}
</script>