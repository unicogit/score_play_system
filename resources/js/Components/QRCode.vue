<template>
    <div>
      <canvas ref="canvas"></canvas>
    </div>
  </template>
  
  <script>
  import QRious from 'qrious'
  
  export default {
    props: {
      url: {
        type: String,
        required: true
      },
      size: {
        type: Number,
        default: 400
      }
    },
    mounted() {
      const qr = new QRious({
        element: this.$refs.canvas,
        value: this.url,
        size: this.size
      })
    }
  }
  </script>
  