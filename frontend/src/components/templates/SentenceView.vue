<template>
  <div id="sentence-view">
    <div class="ma-5">
      <v-container class="my-5">
        <v-row v-for="ex in explain" :key="ex.heading">
          <v-col cols="12"> 
            <div>
              <v-icon>mdi-play</v-icon>
              {{ ex.heading }}
            </div>
            <v-subheader>
              {{ ex.detail }}
            </v-subheader>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="6">
            <SentenceCard />
          </v-col>
          <v-col cols="12" md="6">
            <WordGraphFrame />
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>
<script>
import SentenceCard from "@/components/organisms/SentenceCard";
import WordGraphFrame from "@/components/organisms/WordGraphFrame";
export default {
  name: "SentenceView",
  components: {
    SentenceCard,
    WordGraphFrame,
  },
  data() {
    return {
      explain: [
        {heading: "頻出単語が分かる", detail: "フォームに文章を入力すれば，頻出単語とその出現回数が棒グラフに最大10個まで表示"},
        {heading: "頻出単語を調べる", detail: "棒グラフをクリックすれば，その単語に関連するwikipediaへ移動"},
        {heading: "こういう時に便利", detail: "論文を読む，参考書を読む時など..."},
      ]
    }
  }
};
</script>