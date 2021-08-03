<template>
  <div id="app">
    <v-app>
      <Appbar />
      <v-main class="mx-4 mb-5">
        <router-view />
      </v-main>
    </v-app>
  </div>
</template>

<script>
import Appbar from "@/components/organisms/Appbar.vue";
export default {
  name: "App",
  components: { Appbar },
};
</script>
<style>
  #app {
    font-family: -apple-system, BlinkMacSystemFont, Roboto, "Segoe UI", "Helvetica Neue", HelveticaNeue, YuGothic, "Yu Gothic Medium", "Yu Gothic", Verdana, Meiryo, sans-serif;
  }
</style>
