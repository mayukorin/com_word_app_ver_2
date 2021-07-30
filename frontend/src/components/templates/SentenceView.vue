<template>
  <div id="sentence-view">
    <v-container class="my-5">
      <v-row>
        <v-col cols="12">
          文章を下のフォームに入力すれば，頻出単語とその出現回数が棒グラフに最大10個まで表示されます!<br />
          また，棒グラフをクリックすれば，その単語に関連するwikipediaのページが表示されます!<br />
          論文を読む時に使えば，頻出単語がすぐ分かり，便利です！
        </v-col>
        <v-col cols="12" md="6">
          <SentenceCard />
        </v-col>
        <v-col cols="12" md="6">
          <WordGraphFrame />
        </v-col>
      </v-row>
    </v-container>
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
};
</script>