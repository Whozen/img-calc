<template>
    <header>
        <div class="container">
            <nav class="flex">
                <div class="logo">
                    <h1><a href="/">Img Calculator</a></h1>
                </div>
                <ul class="header-menu flex">
                    <li><a href="#">How to use</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
                <div class="header-cta flex">
                    <button class="btn btn-cta">One</button>
                    <button class="btn btn-cta">Two</button>
                </div>
            </nav>
        </div>
    </header>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
    data() {
        return {
            msg: 'Hlloe',
        }
    }
})

export default class Header extends Vue {}
</script>


<style lang="scss">
@import '../assets/css/helper/variable.scss';

body {
    header {
        padding: 0.5rem 0;
        -webkit-box-shadow: 0 0 40px rgb(0 0 0 / 10%);
        box-shadow: 0 0 40px rgb(0 0 0 / 10%);

        nav {
            .header-menu {
                li {
                    padding: 0 1.25rem;
                    transition: all .1s;

                    &:hover {
                        font-weight: $bold;
                    }
                }
            }
        }
    }
}
</style>