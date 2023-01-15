<template>
    <form class="space-y-6" @submit.prevent="$emit('submitted', form)">
        <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5">
            <div class="space-y-6 sm:space-y-5">
                <div>
                    <h3 class="text-lg font-medium leading-6 text-gray-900">新規練習登録</h3>
                </div>

                <div class="space-y-6 sm:space-y-5">
                    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
                        <label for="first-name" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"
                            >練習タイトル</label
                        >
                        <div class="mt-1 sm:col-span-2 sm:mt-0">
                            <input
                                type="text"
                                name="first-name"
                                id="first-name"
                                autocomplete="given-name"
                                class="block w-full max-w-lg rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:max-w-xs sm:text-sm"
                                v-model="form.title"
                            />
                        </div>
                    </div>
                    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
                        <label for="first-name" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"
                            >練習日</label
                        >
                        <div class="mt-1 sm:col-span-2 sm:mt-0">
                            <input
                                type="date"
                                name="first-name"
                                id="first-name"
                                autocomplete="given-name"
                                class="block w-full max-w-lg rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:max-w-xs sm:text-sm"
                                v-model="form.practice_date"
                            />
                        </div>
                    </div>
                    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
                        <label for="first-name" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"
                            >練習開始時刻</label
                        >
                        <div class="mt-1 sm:col-span-2 sm:mt-0">
                            <input
                                type="time"
                                name="first-name"
                                id="first-name"
                                autocomplete="given-name"
                                class="block w-full max-w-lg rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:max-w-xs sm:text-sm"
                                v-model="form.time"
                            />
                        </div>
                    </div>
                    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
                        <label for="first-name" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"
                            >解析用動画</label
                        >
                        <div class="mt-1 sm:col-span-2 sm:mt-0">
                            <input
                                type="text"
                                name="first-name"
                                id="first-name"
                                autocomplete="given-name"
                                class="block w-full max-w-lg rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:max-w-xs sm:text-sm"
                                v-model="form.video"
                            />
                        </div>
                    </div>
                    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
                        <label for="first-name" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                            解析用楽譜</label>
                        <div class="mt-1 sm:col-span-2 sm:mt-0">
                            <input
                                type="text"
                                name="title"
                                id="title"
                                autocomplete="given-name"
                                class="block w-full max-w-lg rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:max-w-xs sm:text-sm"
                                v-model="form.score"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <a :href="route('callender.python')">python実行</a>
        <div class="pt-5">
            <div class="flex justify-end">
                <a :href="route('callender.index')">
                    <button
                        type="button"
                        class="rounded-md border border-gray-300 bg-white py-2 px-4 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                    >
                        Cancel
                    </button>
                </a>
                <button
                    type="submit"
                    class="ml-3 inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                >
                    Save
                </button>
            </div>
        </div>
    </form>
</template>
<script setup>
import { Link } from '@inertiajs/inertia-vue3'
import { useForm } from '@inertiajs/inertia-vue3'
</script>
<script>
export default {
    props: [''],
    emits: ['submitted'],
    data() {
        return {
            form: useForm({
                title: '',
                practice_date: '',
                time: '',
                video: '',
                score: '',
            })
        }
    }
}
</script>
