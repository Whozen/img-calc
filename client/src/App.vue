<template>
  <Header />
  <HomePage />
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Header from './components/Header.vue';
import HomePage from './views/HomePage.vue';

@Options({
  components: {
    Header,
    HomePage,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
@import '@/assets/css/global.scss';
@import '@/assets/css/helper/variable.scss';

</style>
