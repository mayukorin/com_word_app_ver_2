<template>
  <v-row justify="center">
    <v-btn
      text
      class="success mx-0 my-3 button"
      @click="handleClick"
      :loading="loading"
    >
      <slot />
    </v-btn>
  </v-row>
</template>
<script>
export default {
  name: "Button",
  props: {
    loading: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    handleClick() {
      this.$emit("click");
      this.load = true;
    },
  },
};
</script>
