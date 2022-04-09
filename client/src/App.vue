<template>
  <div class="container">
    <div class="title">
      <h1>Calculate Image Numbers</h1>
    </div>
    <UploadForm />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import UploadForm from './components/UploadForm.vue';

@Options({
  components: {
    UploadForm,
  },
})
export default class App extends Vue {}
</script>

<style>
</style>
