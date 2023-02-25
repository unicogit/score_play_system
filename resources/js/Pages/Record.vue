<script setup>
import { Head } from '@inertiajs/inertia-vue3'
</script>
<template>
    <Head>
        <title>撮影画面</title>
        <link rel="stylesheet" href='css/record.css'>
    </Head>
    <div id="app">
        <div id="video-container">
            <video id="video"></video>
        </div>
    </div>
</template>
<script>
export default {
    name: 'app',
    mounted() {
        //alert('loaded')
        //カメラにアクセスする処理
        var video = document.getElementById('video');
        var constrains = { video: true, audio: true }// 映像・音声を取得するかの設定
        navigator.mediaDevices.getUserMedia(constrains)
        .then(function(stream) {
            video.srcObject = stream // streamはユーザーのカメラとマイクの情報で、これをvideoの入力ソースにする
            video.play()
        })
        .catch(function(err) {
            console.log("An error occured! " + err)
        })
    },
    methods:{

    }
}
</script>