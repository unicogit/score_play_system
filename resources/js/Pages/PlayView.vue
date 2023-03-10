<template>
<div>
    <SideBar />
    <div class="flex flex-1 flex-col md:pl-64">
        <div class="sticky top-0 z-10 flex h-16 flex-shrink-0 bg-white shadow">
            <div class="flex flex-1 justify-between px-4">
                <div class="flex flex-1">
                    <Header />
                </div>
            </div>
        </div>
    </div>
    <div class="flex flex-1 flex-col md:pl-64">
        <main>
            <div class="py-6">
                <div class="mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
                    <!-- Replace with your content -->
                    <PlayView :points="points" :timestamp="timestamp" />
                    <!-- /End replace -->
                </div>
            </div>
        </main>
    </div>
</div>
</template>
<script>
import AppLayout from '@/Layouts/AppLayout.vue';
import Welcome from '@/Components/Welcome.vue';
import Header from '@/Components/header.vue'
import SideBar from '@/Components/SideBar.vue'
import { Head, Link } from '@inertiajs/inertia-vue3';
import PlayView from '@/Components/Play/Viewer.vue';
import axios from 'axios'

export default {
    components: {
        AppLayout,
        Welcome,
        Header,
        SideBar,
        PlayView,
    },
    data() {
        return {
            timestamp: [],
            points: [],
        }
    },
    mounted () {
        axios.get(route('fetch.positions'))
            .then(res => {
                console.log('res: ', res.data)
                this.timestamp = res.data.timestamp
                this.points = res.data.points
            })
            .catch(err => {
                console.log('err: ', err)
            });
    },
}
</script>
