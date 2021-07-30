<template>
  <v-app>
    <Appbar />
    <v-main class="mx-4 mb-5">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Appbar from "@/components/organisms/Appbar.vue";
export default {
  name: "App",
  components: { Appbar },
};
</script>
