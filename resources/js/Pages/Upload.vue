<script setup>
import { Head } from '@inertiajs/inertia-vue3';
</script>
<template>
    <head>
        <!--参考: https://tech.amefure.com/js-vue-laravel-csrf -->
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <!--参考の通りにやるとcontentがnullになる(csrf_token()が走っていない)-->
    </head>
    <Head>
        <title>upload video</title>
    </Head>
    <div id="app">
        <form v-bind:action="store" method="post" enctype="multipart/form-data">
            <!--bladeでは @csrf とここに記述すれば良い-->
            <input type="hidden" name="_token" v-bind:value="csrf">
            <input type="file" name="video"><br>
            <input type="submit" value="upload">
        </form>
    </div>
</template>
<script>
export default {
    el: '#app',
    computed: {
        store: route('upload.store'),
        csrf: document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
    }
}
</script>