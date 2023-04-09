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
        <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5">
            <div class="space-y-6 sm:space-y-5">
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
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { ref } from 'vue';
import PlayView from '@/Components/Play/Viewer.vue';
import SideBar from '@/Components/SideBar.vue'
import AppLayout from '@/Layouts/AppLayout.vue';
import Welcome from '@/Components/Welcome.vue';
import Header from '@/Components/header.vue'
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