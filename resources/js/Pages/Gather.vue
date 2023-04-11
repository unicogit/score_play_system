<template>
    <div>
      <div v-if="showQRCode">
        <qrcode url=https://scoreplaysystem.unico-unique.com/record />
      </div>
      <button v-else @click="showQRCode = true">Show QR Code</button>
    </div>
    <div>
        <a href="/record">録画画面へ移動</a>
    </div>
  </template>
  
  <script>
  import Qrcode from '@/Components/QRCode.vue'
  
  export default {
    components: { Qrcode },
    data() {
      return {
        showQRCode: false,
        qrCodeUrl: '',
      }
    },
    mounted() {
      // ログイン済みのユーザーのトークンを取得
    //   const token = this.$store.state.auth.token
      
    //   // QRコードの生成に必要なURL
    //   const baseUrl = 'https://example.com/record'
    //   const query = `token=${token}`
    //   const qrCodeUrl = `${baseUrl}?${query}`
  
    //   // QRコードを表示
    //   this.qrCodeUrl = qrCodeUrl
      this.showQRCode = true
    },
  }
  </script>
  