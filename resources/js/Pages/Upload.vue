<script setup>
import { Head } from '@inertiajs/inertia-vue3';
</script>
<template>
    <Head>
        <title>upload video</title>
    </Head>
    <div id="app">
        <button onclick="location.href='/record'">record</button><br>
        <!-- CSRF対策をオフにしたので注意！でもオンにするとうまくいかない... -->
        <form :action="route('upload.store')" method="post" enctype="multipart/form-data">
            <input type="text" name="title">
            <input type="file" name="video" accept="video/mp4"><br>
            <input type="submit" value="upload">
        </form>
    </div>
</template>
<script>
export default {
    el: '#app',
}
</script>