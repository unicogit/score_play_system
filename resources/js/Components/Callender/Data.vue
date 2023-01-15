<template>
    <div class="lg:flex lg:h-full lg:flex-col">
      <header class="flex items-center justify-between border-b border-gray-200 py-4 px-6 lg:flex-none">
        <h1 class="text-lg font-semibold text-gray-900">
          <time datetime="2022-01">{{year}}年 {{month}}月</time>
        </h1>
        <div class="flex items-center">
          <div class="flex items-center rounded-md shadow-sm md:items-stretch">
            <button type="button" class="flex items-center justify-center rounded-l-md border border-r-0 border-gray-300 bg-white py-2 pl-3 pr-4 text-gray-400 hover:text-gray-500 focus:relative md:w-9 md:px-2 md:hover:bg-gray-50">
              <span class="sr-only">先月</span>
              <ChevronLeftIcon class="h-5 w-5" aria-hidden="true" />
            </button>
            <button type="button" class="hidden border-t border-b border-gray-300 bg-white px-3.5 text-sm font-medium text-gray-700 hover:bg-gray-50 hover:text-gray-900 focus:relative md:block">本日</button>
            <span class="relative -mx-px h-5 w-px bg-gray-300 md:hidden" />
            <button type="button" class="flex items-center justify-center rounded-r-md border border-l-0 border-gray-300 bg-white py-2 pl-4 pr-3 text-gray-400 hover:text-gray-500 focus:relative md:w-9 md:px-2 md:hover:bg-gray-50">
              <span class="sr-only">次月</span>
              <ChevronRightIcon class="h-5 w-5" aria-hidden="true" />
            </button>
          </div>
          <div class="hidden md:ml-4 md:flex md:items-center">
            <Menu as="div" class="relative">
              <MenuButton type="button" class="flex items-center rounded-md border border-gray-300 bg-white py-2 pl-3 pr-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50">
                月表示
                <ChevronDownIcon class="ml-2 h-5 w-5 text-gray-400" aria-hidden="true" />
              </MenuButton>
  
              <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                <MenuItems class="absolute right-0 z-10 mt-3 w-36 origin-top-right overflow-hidden rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                  <div class="py-1">
                    <MenuItem v-slot="{ active }">
                      <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">日表示</a>
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                      <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">週表示</a>
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                      <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">月表示</a>
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                      <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">年表示</a>
                    </MenuItem>
                  </div>
                </MenuItems>
              </transition>
            </Menu>
            <div class="ml-6 h-6 w-px bg-gray-300" />
            <a :href="route('callender.create')">
            <button type="button" class="ml-6 rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">練習登録</button>
          </a>
          </div>
          <Menu as="div" class="relative ml-6 md:hidden">
            <MenuButton class="-mx-2 flex items-center rounded-full border border-transparent p-2 text-gray-400 hover:text-gray-500">
              <span class="sr-only">メニューを開く</span>
              <EllipsisHorizontalIcon class="h-5 w-5" aria-hidden="true" />
            </MenuButton>
  
            <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
              <MenuItems class="absolute right-0 z-10 mt-3 w-36 origin-top-right divide-y divide-gray-100 overflow-hidden rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <div class="py-1">
                 
                </div>
                <div class="py-1">
                  <MenuItem v-slot="{ active }">
                    <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">現在の日付へ</a>
                  </MenuItem>
                </div>
                <div class="py-1">
                  <MenuItem v-slot="{ active }">
                    <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">日表示</a>
                  </MenuItem>
                  <MenuItem v-slot="{ active }">
                    <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">週表示</a>
                  </MenuItem>
                  <MenuItem v-slot="{ active }">
                    <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">月表示</a>
                  </MenuItem>
                  <MenuItem v-slot="{ active }">
                    <a href="#" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">年表示</a>
                  </MenuItem>
                </div>
              </MenuItems>
            </transition>
          </Menu>
        </div>
      </header>
      <div class="shadow ring-1 ring-black ring-opacity-5 lg:flex lg:flex-auto lg:flex-col">
        <div class="grid grid-cols-7 gap-px border-b border-gray-300 bg-gray-200 text-center text-xs font-semibold leading-6 text-gray-700 lg:flex-none">
          <div class="bg-white py-2">M<span class="sr-only sm:not-sr-only">on</span></div>
          <div class="bg-white py-2">T<span class="sr-only sm:not-sr-only">ue</span></div>
          <div class="bg-white py-2">W<span class="sr-only sm:not-sr-only">ed</span></div>
          <div class="bg-white py-2">T<span class="sr-only sm:not-sr-only">hu</span></div>
          <div class="bg-white py-2">F<span class="sr-only sm:not-sr-only">ri</span></div>
          <div class="bg-white py-2">S<span class="sr-only sm:not-sr-only">at</span></div>
          <div class="bg-white py-2">S<span class="sr-only sm:not-sr-only">un</span></div>
        </div>
        <div class="flex bg-gray-200 text-xs leading-6 text-gray-700 lg:flex-auto">
          <div class="hidden w-full lg:grid lg:grid-cols-7 lg:grid-rows-6 lg:gap-px">
            <!-- :class="[day.isCurrentMonth ? 'bg-white' : 'bg-gray-50 text-gray-500', 'relative py-2 px-3']" -->
            <div v-for="day in days" :key="day.date" class="bg-white bg-gray-50 text-gray-500 relative py-2 px-3">
              <!-- :class="day.isToday ? 'flex h-6 w-6 items-center justify-center rounded-full bg-indigo-600 font-semibold text-white' : undefined" -->
              <time :datetime="day.date">{{ day.date }}</time>
              <ol class="mt-2">
                <li v-for="practice in practices" :key="practice.id">
                  <a v-if="practice.practice_date == year+'-'+('0'+month).slice(-2)+'-'+('0'+day.date).slice(-2)" :href="practice.title" class="group flex">
                    <p class="flex-auto truncate font-medium text-gray-900 group-hover:text-indigo-600">
                      {{ practice.title }}
                    </p>
                    <time :datetime="practice.time" class="ml-3 hidden flex-none text-gray-500 group-hover:text-indigo-600 xl:block">{{ practice.time }}</time>
                  </a>
                </li>
                <!-- <li v-if="day.events.length > 2" class="text-gray-500">+ {{ day.events.length - 2 }} 更に</li> -->
              </ol>
            </div>
          </div>
          <div class="isolate grid w-full grid-cols-7 grid-rows-6 gap-px lg:hidden">
            <!-- :class="[day.isCurrentMonth ? 'bg-white' : 'bg-gray-50', (day.isSelected || day.isToday) && 'font-semibold', day.isSelected && 'text-white', !day.isSelected && day.isToday && 'text-indigo-600', !day.isSelected && day.isCurrentMonth && !day.isToday && 'text-gray-900', !day.isSelected && !day.isCurrentMonth && !day.isToday && 'text-gray-500', 'flex h-14 flex-col py-2 px-3 hover:bg-gray-100 focus:z-10']" -->
            <button v-for="practice in practices" :key="practice.id" type="button" >
              <!-- :class="[day.isSelected && 'flex h-6 w-6 items-center justify-center rounded-full', day.isSelected && day.isToday && 'bg-indigo-600', day.isSelected && !day.isToday && 'bg-gray-900', 'ml-auto']" -->
              <time :datetime="practice.practice_date">{{ practice.practice_date.split('-').pop().replace(/^0/, '') }}</time>
              <span class="sr-only">{{ practice.title }}</span>
              <!-- <span v-if="day.events.length > 0" class="-mx-0.5 mt-auto flex flex-wrap-reverse">
                <span v-for="event in day.events" :key="event.id" class="mx-0.5 mb-1 h-1.5 w-1.5 rounded-full bg-gray-400" />
              </span> -->
            </button>
          </div>
        </div>
      </div>
      <div class="py-10 px-4 sm:px-6 lg:hidden">
        <ol class="divide-y divide-gray-100 overflow-hidden rounded-lg bg-white text-sm shadow ring-1 ring-black ring-opacity-5">
          <li v-for="practice in practices" :key="practice.id" class="group flex p-4 pr-6 focus-within:bg-gray-50 hover:bg-gray-50">
            <div class="flex-auto">
              <p class="font-semibold text-gray-900">{{ practice.title }}</p>
              <time :datetime="practice.practice_date" class="mt-2 flex items-center text-gray-700">
                <ClockIcon class="mr-2 h-5 w-5 text-gray-400" aria-hidden="true" />
                {{ practice.practice_date }}
              </time>
            </div>
            <a :href="practice.title" class="ml-6 flex-none self-center rounded-md border border-gray-300 bg-white py-2 px-3 font-semibold text-gray-700 opacity-0 shadow-sm hover:bg-gray-50 focus:opacity-100 group-hover:opacity-100"
              >Edit<span class="sr-only">, {{ practice.title }}</span></a
            >
          </li>
        </ol>
      </div>
    </div>
    {{ practices }}
  </template>
  
  <script setup>
  import {
    ChevronDownIcon,
    ChevronLeftIcon,
    ChevronRightIcon,
    ClockIcon,
    EllipsisHorizontalIcon,
  } from '@heroicons/vue/20/solid'
  import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
  
  const date = new Date()
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const startDate = new Date(year, month - 1, 1) // 月の最初の日を取得
  const endDate = new Date(year, month,  0) // 月の最後の日を取得
  const endDayCount = endDate.getDate() // 月の末日
  const startDay = startDate.getDay()
  const days = []
  console.log(endDayCount)
  const maxday = parseInt(endDayCount);
  for (let i= 1; i <= maxday; i++){
    days.push({date:i})
  }
  console.log(days)
  const day=[
      { date: year+'-'+month+'-'+startDay+1}
  ]

  function prev(){
    showDate.setMonth(showDate.getMonth() - 1);
    showProcess(showDate);
}
  // const days = [
  //   { date: '2021-12-27', events: [] },
  //   { date: '2021-12-28', events: [] },
  //   { date: '2021-12-29', events: [] },
  //   { date: '2021-12-30', events: [] },
  //   { date: '2021-12-31', events: [] },
  //   { date: '2022-01-01', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-02', isCurrentMonth: true, events: [] },
  //   {
  //     date: '2022-01-03',
  //     isCurrentMonth: true,
  //     events: [
  //       { id: 1, name: '練習', time: '10AM', datetime: '2022-01-03T10:00', href: '#' },
  //       { id: 2, name: '練習', time: '2PM', datetime: '2022-01-03T14:00', href: '#' },
  //     ],
  //   },
  //   { date: '2022-01-04', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-05', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-06', isCurrentMonth: true, events: [] },
  //   {
  //     date: '2022-01-07',
  //     isCurrentMonth: true,
  //     events: [{ id: 3, name: '練習', time: '6PM', datetime: '2022-01-08T18:00', href: '#' }],
  //   },
  //   { date: '2022-01-08', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-09', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-10', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-11', isCurrentMonth: true, events: [] },
  //   {
  //     date: '2022-01-12',
  //     isCurrentMonth: true,
  //     isToday: true,
  //     events: [{ id: 6, name: "練習", time: '2PM', datetime: '2022-01-25T14:00', href: '#' }],
  //   },
  //   { date: '2022-01-13', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-14', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-15', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-16', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-17', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-18', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-19', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-20', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-21', isCurrentMonth: true, events: [] },
  //   {
  //     date: '2022-01-22',
  //     isCurrentMonth: true,
  //     isSelected: true,
  //     events: [
  //       { id: 4, name: '練習', time: '3PM', datetime: '2022-01-22T15:00', href: '#' },
  //       { id: 5, name: '練習', time: '7PM', datetime: '2022-01-22T19:00', href: '#' },
  //     ],
  //   },
  //   { date: '2022-01-23', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-24', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-25', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-26', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-27', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-28', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-29', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-30', isCurrentMonth: true, events: [] },
  //   { date: '2022-01-31', isCurrentMonth: true, events: [] },
  //   { date: '2022-02-01', events: [] },
  //   { date: '2022-02-02', events: [] },
  //   {
  //     date: '2022-02-03',
  //     events: [{ id: 7, name: '練習', time: '9PM', datetime: '2022-02-04T21:00', href: '#' }],
  //   },
  //   { date: '2022-02-04', events: [] },
  //   { date: '2022-02-05', events: [] },
  //   { date: '2022-02-06', events: [] },
  // ]
  // const selectedDay = practices.find((practice) => practice.isSelected)
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