<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-form ref="form" class="mb-3">
          <v-textarea
            counter="1000"
            label="文章(1000文字まで)"
            :rules="rules.sentence"
            v-model="form.sentence"
          ></v-textarea>
          <Button @click="handleClick" :loading="myLoad">調べる</Button>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import Button from "@/components/atoms/Button";

export default {
  name: "SentenceForm",
  components: {
    Button,
  },
  props: {
    onanalyze: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
      form: {
        sentence: "",
      },
      rules: {
        sentence: [
          (v) => v.length <= 1000 || "一度に分析できるのは，1000文字までです",
        ],
      },
      myLoad: false,
    };
  },
  methods: {
    handleClick() {
      if (!this.$refs.form.validate()) return;
      this.myLoad = true;
      return this.onanalyze({ sentence: this.form.sentence }).then(() => {
        this.myLoad = false;
      });
    },
  },
};
</script>
