<template>
    <div class="py-6">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
            <PlayView
                :practices="data"
                :points="points"
                :timestamp="timestamp"
                :data="data"
            />
        </div>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import SideBar from '@/Components/SideBar.vue';
const title = ref("");
const activeScoreId = ref(null);
const open = ref(false);
const toggleMenu = () => {
  open.value = !open.value;
};
</script>
<script>
import { ref } from 'vue';
import PlayView from '@/Components/Play/Viewer.vue';
import AppLayout from '@/Layouts/AppLayout.vue';
import Welcome from '@/Components/Welcome.vue';
import Header from '@/Components/header.vue';
export default {
    components: {
        AppLayout,
        Welcome,
        Header,
        SideBar,
        PlayView,
    },
    props: ['data'],
    mounted(){
        console.log(this.data);
    }
}
</script>