<template>
  <v-card class="sentence-card px-3">
    <v-card-title>
      <span class="headline">頻出単語を調べる</span>
    </v-card-title>
    <v-card-text>
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