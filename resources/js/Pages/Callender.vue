<template>
    
    <div class="flex flex-col h-screen">
        <!-- <div class="flex flex-1"> -->
          <SideBar  :open="open" @update-open="toggleMenu" />
        <!-- </div> -->
          <div v-show="open" @click="toggleMenu" class="fixed inset-0 bg-black opacity-25 md:hidden z-10"></div>
        <div class="py-6">
          <div class="mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
              <!-- Replace with your content -->
              <CallenderView :practices = "practices" />
              <!-- /End replace -->
          </div>
        </div>
    </div>
</template>

<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import Welcome from '@/Components/Welcome.vue';
import CallenderView from '@/Components/Callender/Data.vue';
import Header from '@/Components/header.vue'
import SideBar from '@/Components/SideBar.vue'
import { ref, computed } from 'vue'
const open = ref(false)
const toggleMenu = () => {
  open.value = !open.value;
}
</script>
<script>

 export default {
    props: {
        practices:{
                type: Array,
        },
        data: {
            type: Array,
        },
        user: {
            type: Array,
        },
    },
    mounted() {
        this.user = window.Jetstream.inertia.user;
    },
    data(){
        return null
    },
}
</script>
