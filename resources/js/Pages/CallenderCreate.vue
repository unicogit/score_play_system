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
                        <PracticeCreate
                            :practice="practice"
                            @submitted="createPractice"
                        ></PracticeCreate>
                    </div>
                </div>
            </main>
        </div>
    </div>
</template>
<script setup>
import SideBar from '@/Components/SideBar.vue'
import PracticeCreate from '@/Components/Callender/Create.vue'
import { ref } from 'vue'


const createPractice = (formData) => {
    formData.post(route('callender.store'))
}

const sidebarOpen = ref(false)
</script>
<script>
export default {
    props: {
        practice: {
            type: Array
        }
    },
    methods: {
        createPractice(formData) {
            formData.post(route('callender.store'))
        }
    }
}
</script>
<style scope>
.sticky {
    position: -webkit-sticky;
    position: sticky;
    top: 1.5rem;
}
</style>
