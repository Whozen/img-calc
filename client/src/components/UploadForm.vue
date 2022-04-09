<template>
    <form>
        <div class="form-group">
            <label for="filename"></label>
            <input type="file" id="myFile" name="filename" class="form-control">
        </div>
        <div class="form-group">
            <div class="radio">
                <label><input type="radio" name="optradio" checked>Add</label>
            </div>
            <div class="radio">
                <label><input type="radio" name="optradio">Multiply</label>
            </div>
        </div>
        <input type="submit" value="Submit">
    </form>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  
})
export default class UploadForm extends Vue {}
</script>