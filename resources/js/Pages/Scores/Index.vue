<template>
    <div class="flex flex-col h-screen">
    <div class="flex flex-1">
      <SideBar :open="open" @update-open="toggleMenu" />
      <div
        v-show="open"
        @click="toggleMenu"
        class="fixed inset-0 bg-black opacity-25 md:hidden z-10"
      ></div>
    <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5">
        <div class="space-y-6 sm:space-y-5">
            <div class="flex flex-1 flex-col md:pl-64">
                <div class="py-6">
                        <div class="container">
                            <h3 class="text-lg font-medium leading-6 text-gray-900">楽譜一覧</h3>
                            <form @submit.prevent="submitForm" enctype="multipart/form-data">
                                <div class="mt-1 sm:col-span-2 sm:mt-0">
                                <label for="title" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">楽譜のタイトル</label>
                                    <input type="text" class="block w-full max-w-lg rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:max-w-xs sm:text-sm" id="title" v-model="title" required />
                                </div>
                                <div class="col-span-full">
                                    <label for="cover-photo" class="block text-sm font-medium leading-6 text-gray-900">楽譜PDFアップロード</label>
                                <div class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
                                <div class="text-center">
                                    <PhotoIcon class="mx-auto h-12 w-12 text-gray-300" aria-hidden="true" />
                                <div class="mt-4 flex text-sm leading-6 text-gray-600">
                                    <label for="file-upload" class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500">
                                    <span>楽譜のアップロード</span>
                                    <input id="file-upload" name="file-upload" type="file" class="sr-only" @change="onFileChange" required/>
                                    </label>
                                    <p class="pl-1">ドラッグ&ドロップでもアップロードできます</p>
                                </div>
                                <p class="text-xs leading-5 text-gray-600">PDF up to 10MB</p>
                            </div>
                        </div>
                    </div>
                        <button type="submit" class="rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">アップロード</button>
                    </form>
                    <hr>
                    <div class="scores">
                    <div v-for="score in parsedScores" :key="score.id" class="score">
                        <h2 @click="showImages(score.id)">{{ score.title }}</h2>
                        <div v-for="(imagePath, index) in score.image_path" :key="index" class="score-image" v-show="activeScoreId === score.id">
                        <img :src="`/storage/${imagePath.substring(7)}`" alt="Score image" />
                        </div>
                    </div>
                    </div>
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
import { ref, computed} from "vue";
import { Inertia } from "@inertiajs/inertia";
import AppLayout from '@/Layouts/AppLayout.vue';
import Welcome from '@/Components/Welcome.vue';
import Header from '@/Components/header.vue';

export default {
    components: {
        Header,
        SideBar,
        // ScoreViewer,
    },
    computed: {
    parsedScores() {
        return this.scores.map(score => {
        let imagePath;
        try {
            imagePath = JSON.parse(score.image_path);
        } catch (error) {
            console.error(`Failed to parse image_path for score id ${score.id}: ${score.image_path}`);
            imagePath = [];
        }

        return {
            ...score,
            image_path: imagePath,
        };
        });
    },
  },
  props: {
    scores: Array,
  },
  setup() {
    const activeScoreId = ref(null);
    const title = ref("");
    const file = ref(null);

    function onFileChange(e) {
      file.value = e.target.files[0];
    }

    function submitForm() {
      if (!title.value || !file.value) return;

      const formData = new FormData();
      formData.append("title", title.value);
      formData.append("file", file.value);

      Inertia.post("/score", formData);
    }
    function showImages(scoreId) {
        activeScoreId.value = scoreId;
        }
    return {
        title,
        file,
        onFileChange,
        submitForm,
        activeScoreId,
        showImages
    };
  },
};
</script>