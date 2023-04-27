<template>
    <div class="flex flex-col h-screen">
    <div class="flex flex-1">
      <SideBar  :open="open" @update-open="toggleMenu" />
    </div>
      <div v-show="open" @click="toggleMenu" class="fixed inset-0 bg-black opacity-25 md:hidden z-10"></div>
     <div class="flex flex-1 flex-col md:pl-64">
   
        <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5">
            <div class="space-y-6 sm:space-y-5">
                <div class="py-6">
                <div>
                    <h3 class="text-lg font-medium leading-6 text-gray-900">練習詳細</h3>
                </div>

                <div class="space-y-6 sm:space-y-5">
                    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
                        <label class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">楽曲のタイトル</label>
                        <div class="mt-1 sm:col-span-2 sm:mt-0">
                            <span class="text-gray-600">{{ data.title }}</span>
                        </div>
                    </div>
                    <!-- <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
                        <label class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">練習日</label>
                        <div class="mt-1 sm:col-span-2 sm:mt-0">
                            <span class="text-gray-600">{{ data.practice_date }}</span>
                        </div>
                    </div> -->
                </div>
                <div class="py-6">
                    <div class="mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
                        <PlayView
                            :practices="practices"
                            :points="points"
                            :timestamp="timestamp"
                            :data="data"
                        />
                    </div>
                </div>
            </div>
        </div>
        </div>
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
}
</script>