<template>
    <div class="flex flex-col h-screen">
    <div class="flex flex-1">
        <SideBar  :open="open" @update-open="toggleMenu" />
      <div v-show="open" @click="toggleMenu" class="fixed inset-0 bg-black opacity-25 md:hidden z-10"></div>
        <div class="flex flex-1 flex-col md:pl-64">
            <main>
                <div class="py-6">
                    <div class="mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
                        <PracticeCreate
                            :scores="scores"
                            @submitted="createPractice"
                        ></PracticeCreate>
                    </div>
                </div>
            </main>
        </div>
    </div>
    </div>
</template>
<script setup>
import SideBar from '@/Components/SideBar.vue'
import PracticeCreate from '@/Components/Callender/Create.vue'
import { ref, computed } from 'vue'
const open = ref(false)
const toggleMenu = () => {
  open.value = !open.value;
}
const createPractice = (formData) => {
    formData.post(route('callender.store'))
}

</script>
<script>
export default {
    props: {
        scores: {
            type: Array,
            default: () => [],
        },
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
