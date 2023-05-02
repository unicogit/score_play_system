<template>
    <div>
      <h1>{{ practice.title }}</h1>
      <p>練習日: {{ practice.practice_date }}</p>
      <p>練習開始時刻: {{ practice.time }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      practice: Object,
    },
  };
  </script>