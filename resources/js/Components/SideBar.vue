<template>
    <!-- <div class="relative"> -->
    <div>
        <button @click="$emit('updateOpen', !open)" class="bg-white p-2 rounded-md text-gray-500 z-30">
  <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" xmlns="http://www.w3.org/2000/svg">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path>
  </svg>
</button>
    </div>
    <div :class="{'hidden': !props.open, 'fixed md:static top-0 bottom-0 right-0 md:flex md:w-64 md:flex-col': true}">
        <div class="flex-grow flex-col gap-y-5 overflow-y-auto border-r border-gray-200 bg-white px-6">
          <div class="flex h-16 shrink-0 items-center">
            <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company" />
          </div>
          <nav class="flex flex-1 flex-col">
            <ul role="list" class="flex flex-1 flex-col gap-y-7">
              <li>
                <ul role="list" class="-mx-2 space-y-1">
                  <li v-for="item in navigation" :key="item.name">
                    <a :href="item.href" :class="[item.current ? 'bg-gray-50 text-indigo-600' : 'text-gray-700 hover:text-indigo-600 hover:bg-gray-50', 'group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold']">
                      <component :is="item.icon" :class="[item.current ? 'text-indigo-600' : 'text-gray-400 group-hover:text-indigo-600', 'h-6 w-6 shrink-0']" aria-hidden="true" />
                      {{ item.name }}
                      <span v-if="item.count" class="ml-auto w-9 min-w-max whitespace-nowrap rounded-full bg-white px-2.5 py-0.5 text-center text-xs font-medium leading-5 text-gray-600 ring-1 ring-inset ring-gray-200" aria-hidden="true">{{ item.count }}</span>
                    </a>
                  </li>
                </ul>
              </li>
            </ul>
          </nav>
        </div>
    </div>
  <!-- </div> -->

  </template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue'
import { useWindowSize } from '../hooks/useWindowSize'
var currentpath = location.pathname;
let home,register,viewer, playview = false;
const props = defineProps({
  open: Boolean
});

const emit = defineEmits({
  updateOpen: (value) => true
});

if (currentpath=='/callender'){
  home = true
  register,viewer,playview = false;
}
if (currentpath=='/practice_register'){
  register = true
  home,viewer,playview = false;
}
if (currentpath=='/scores'){
  viewer = true
  register,home,playview = false;
}
if (currentpath=='playview'){
    home,register,viewer= false;
}

const navigation = [
  { name: 'ホーム', href: '/callender', current: home },
  { name: '楽譜登録', href: '/score', current: viewer },
  { name: '新規レッスン登録', href: '/callender/create', current: register },
  { name: 'レッスンを撮影', href: '/gather'},
  // { name: '録画データを視聴', href: '/playview', current: playview},
]
</script>

<style scoped>
 .hidden {
    display: none;
  }
</style>
