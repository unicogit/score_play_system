<template>
    <div class="hidden md:fixed md:inset-y-0 md:flex md:w-64 md:flex-col">
        <!-- Sidebar component, swap this element with another sidebar if you like -->
        <div class="flex flex-grow flex-col overflow-y-auto bg-indigo-50 pt-5">
            <div class="flex flex-shrink-0 items-center px-4">
                <img
                    class="h-8 w-auto"
                    src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=300"
                    alt="SCPS"
                />
            </div>
            <div class="mt-5 flex flex-1 flex-col">
                <nav class="flex-1 space-y-1 bg-white px-2" aria-label="Sidebar">
                    <template v-for="item in navigation" :key="item.name">
                        <div v-if="!item.children">
                            <a
                                :href="item.href"
                                :class="[
                                    item.current
                                        ? 'bg-gray-100 text-gray-900'
                                        : 'bg-white text-gray-600 hover:bg-gray-50 hover:text-gray-900',
                                    'group w-full flex items-center pl-7 pr-2 py-2 text-sm font-medium rounded-md'
                                ]"
                                >{{ item.name }}</a
                            >
                        </div>
                        <Disclosure as="div" v-else class="space-y-1" v-slot="{ open }">
                            <DisclosureButton
                                :class="[
                                    item.current
                                        ? 'bg-gray-100 text-gray-900'
                                        : 'bg-white text-gray-600 hover:bg-gray-50 hover:text-gray-900',
                                    'group w-full flex items-center pr-2 py-2 text-left text-sm font-medium rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'
                                ]"
                            >
                                <svg
                                    :class="[
                                        open ? 'text-gray-400 rotate-90' : 'text-gray-300',
                                        'mr-2 h-5 w-5 flex-shrink-0 transform transition-colors duration-150 ease-in-out group-hover:text-gray-400'
                                    ]"
                                    viewBox="0 0 20 20"
                                    aria-hidden="true"
                                >
                                    <path d="M6 6L14 10L6 14V6Z" fill="currentColor" />
                                </svg>
                                {{ item.name }}
                            </DisclosureButton>
                            <DisclosurePanel class="space-y-1">
                                <DisclosureButton
                                    v-for="subItem in item.children"
                                    :key="subItem.name"
                                    as="a"
                                    :href="subItem.href"
                                    class="group flex w-full items-center rounded-md py-2 pl-10 pr-2 text-sm font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900"
                                    >{{ subItem.name }}</DisclosureButton
                                >
                            </DisclosurePanel>
                        </Disclosure>
                    </template>
                </nav>
            </div>
        </div>
    </div>
</template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue'
var currentpath = location.pathname;
let home,register,viewer = false;

if (currentpath=='/callender'){
  home = true
  register,viewer = false;
}
if (currentpath=='/practice_register'){
  register = true
  home,viewer = false;
}
if (currentpath=='/viewer'){
  viewer = true
  register,home = false;
}

const navigation = [
  { name: 'ホーム', href: '/callender', current: home },
  { name: '新規練習登録', href: '/callender.create', current: register },
  { name: '動画再生ビュアー', href: '/viewer', current: viewer },
]
</script>

<style lang="scss" scoped></style>
