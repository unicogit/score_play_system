<script setup>
import { Head, Link } from '@inertiajs/inertia-vue3';

defineProps({
    canLogin: Boolean,
    canRegister: Boolean,
    laravelVersion: String,
    phpVersion: String,
});
</script>

<template>
    <Head title="Home" meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <div class="container">
        <h1>MeloRecap♪</h1>
        <a :href="route('login')" class="text-sm text-white-700 dark:text-white-500 underline">ログイン</a>
        <a v-if="canRegister" :href="route('register')" class="ml-4 text-sm text-white-700 dark:text-white-500 underline">新規登録</a>
    </div>
</template>
<script>
import { onMounted } from 'vue';

export default {
    props: {
        canLogin: Boolean,
        canRegister: Boolean,
        laravelVersion: String,
        phpVersion: String,
    },
    setup() {
        let container;

        onMounted(() => {
            container = document.querySelector('.container');
            container.addEventListener('mouseenter', () => {
                container.style.transform = 'scale(1.05)';
                container.style.boxShadow = '0 8px 12px rgba(0, 0, 0, 0.1)';
            });
            container.addEventListener('mouseleave', () => {
                container.style.transform = 'scale(1)';
                container.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
            });
        });

        return {};
    },
};
</script>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    .container {
        text-align: center;
        padding: 2rem;
        background-color: white;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 50%;
        min-width: 320px;
    }

    h1 {
        font-size: 2rem;
        margin-bottom: 1rem;
        color: #333;
    }

    a {
        display: inline-block;
        text-decoration: none;
        padding: 0.5rem 1rem;
        background-color: #2d3748;
        color: white;
        font-size: 1rem;
        margin-top: 1rem;
        border-radius: 0.5rem;
        transition: all 0.3s ease;
    }

    a:hover {
        background-color: #4a5568;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>