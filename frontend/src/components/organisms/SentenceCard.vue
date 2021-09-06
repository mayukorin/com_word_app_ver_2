<template>
  <v-card class="sentence-card px-3">
    <v-card-text>
      <div class="text-body-1">頻出単語を調べたい文章を入力してください</div>
      <SentenceForm :onanalyze="handleAnalyze" />
    </v-card-text>
  </v-card>
</template>

<script>
import SentenceForm from "@/components/molecules/SentenceForm";

export default {
  name: "SentenceCard",
  components: {
    SentenceForm,
  },
  methods: {
    handleAnalyze(sentenceInfo) {
      return this.$store.dispatch("analyze/execute", sentenceInfo);
    },
  },
};
</script>