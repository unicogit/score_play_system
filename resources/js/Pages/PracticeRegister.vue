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
                        <!-- <CustomerCreate
                            :cutomers="cutomers"
                            @submitted="createCustomer"
                        ></CustomerCreate> -->
                        <!-- /End replace -->
                    </div>
                </div>
            </main>
        </div>
    </div>
</template>
<script setup>
import SideBar from '@/Components/SideBar.vue'
// import CustomerCreate from '@/Components/Customer/Create.vue'
import { ref } from 'vue'
import {
    Dialog,
    DialogPanel,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
    TransitionChild,
    TransitionRoot
} from '@headlessui/vue'

import { MagnifyingGlassIcon } from '@heroicons/vue/20/solid'
const userNavigation = [
    { name: 'Your Profile', href: '#' },
    { name: 'Settings', href: '#' },
    { name: 'Sign out', href: '#' }
]

const createCustomer = (formData) => {
    formData.post(route('customer.store'))
}

const sidebarOpen = ref(false)
</script>
<script>
export default {
    // props: {
    //     cutomers: {
    //         type: Array
    //     }
    // },
    // methods: {
    //     createCustomer(formData) {
    //         formData.post(route('customer.store'))
    //     }
    // }
}
</script>
<style scope>
.sticky {
    position: -webkit-sticky;
    position: sticky;
    top: 1.5rem;
}
</style>
