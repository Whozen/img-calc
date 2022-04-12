<template>
    <form @submit.prevent="formSubmit()">
        <div class="form-group">
            <label>
                <input type="file" ref="file" @change="readFile()" id="image" name="imgName" class="form-control" />
                Upload Image
            </label>
            <div v-if="imgPreview !== null">
               <img :src="imgPreview" />
            </div>
        </div>
        <div class="form-group">
            <label>Select Operaton</label>
            <label>
                <input type="radio" value="add" v-model="operation">
                Add
            </label>
            <label>
                <input type="radio" value="multiply" v-model="operation">
                Multiply
            </label>
        </div>
        <input type="submit" value="Submit">
    </form>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Service from '../services/index';

@Options({
    data: function() {
        return {
            operation: 'add',
            file: null,
            imgPreview: null
        };
    },

     methods: {
        formSubmit() {
            console.log("File:");
            console.log(this.file);
            console.log("Operation: " + this.operation);

            console.log(Service.uploadImg(this.file));
        },
        readFile() {
            this.file = this.$refs.file.files[0];
            if (
                this.file.name.includes(".png") ||
                this.file.name.includes(".jpg")
            ) {
                this.imgPreview = URL.createObjectURL(this.file);
            }
        }
    }
})
export default class UploadForm extends Vue {}
</script>