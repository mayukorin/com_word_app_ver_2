<template>
  <div id="sentence-view">
    <v-container class="my-5">
      <v-row>
        <v-col cols="12">
          <v-list>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-play</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  頻出単語の出現回数
                </v-list-item-title>
                <v-list-item-subtitle>
                  頻出単語とその出現回数が棒グラフに最大10個まで表示
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-play</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  頻出単語を調べる
                </v-list-item-title>
                <v-list-item-subtitle>
                  棒グラフをクリックすれば，その単語に関連するwikipediaへ移動
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-play</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  こういう時に便利
                </v-list-item-title>
                <v-list-item-subtitle>
                  論文を読む，参考書を読む，...
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
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