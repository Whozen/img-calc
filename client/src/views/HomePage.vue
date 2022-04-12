<template>
    <div class="main-content">
        <div class="container">
            <div class="title">
                <h1>Calculate Numbers in the image</h1>
            </div>
            <UploadForm />
        </div>
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import UploadForm from '../components/UploadForm.vue';

@Options({
  components: {
    UploadForm,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
    .main-content {
        margin: 3.125rem 0;
    }
</style>