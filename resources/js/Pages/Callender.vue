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
                        <CallenderView :practices = "practices" />
                        <!-- /End replace -->
                    </div>
                </div>
            </main>
        </div>
    </div>
</template>

<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import Welcome from '@/Components/Welcome.vue';
import CallenderView from '@/components/Callender/Data.vue';
import Header from '@/Components/Header.vue'
import SideBar from '@/Components/SideBar.vue'

</script>
<script>
 export default {
                props: {
                    practices:{
                        type: Array
                    }
                },
                data(){
                    return null
                }
            }
</script>