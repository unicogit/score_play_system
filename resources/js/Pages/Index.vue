<style>
#menu{
    display: flex;
    flex-direction: row;
}
.button_menu_index{
    margin: auto;
    width: 50vw;
    height: 30vh;
    background-color: black;
    color: white;
}
.button_menu_index:hover{
    background-color: lightgray;
    color: black;
}

</style>
<template>
    <div id="app">
        <nav id="menu">
            <button id="playview" class="button_menu_index" @click="jumpPlayview">振り返る</button>
            <button id="record" class="button_menu_index" @click="jumpRecord">撮影する</button>
        </nav>
    </div>
</template>
<script>
export default{
    name: 'app',
    methods: {
        jumpPlayview: function(){
            window.location.href = '/playview';
        },
        jumpRecord: function(){
            window.location.href = '/record';
        },
    },

}
</script>