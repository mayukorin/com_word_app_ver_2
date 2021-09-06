<template>
  <div>
    <!-- グラフを描画するのは，子供にして，wordGraphはdataをstoreから持ってくる．propsのメソッドをcomputedに入れられたら，変更検知できるため-->
    <WordGraph :chart-data="GetWordList" :options="GetCntList" ref="child" />
  </div>
</template>
<script>
import WordGraph from "@/components/molecules/WordGraph";
export default {
  name: "WordGraphFrame",
  components: {
    WordGraph,
  },
  data() {
    return {
      word_url_dict: null,
    };
  },
  computed: {
    GetWordList: function () {
      let result = this.$store.state.analyze.result;
      this.set_word_url_dict(result);
      let result_words = Object.keys(result);
      let result_cnt = [];
      for (let url_and_cnt of Object.values(result)) {
        result_cnt.push(url_and_cnt[1]);
      }

      const chartDataObject = {
        labels: result_words,
        datasets: [
          {
            label: "出現回数",
            data: result_cnt,
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(255, 160, 167, 0.2)",
              "rgba(157, 204, 224, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(115, 78, 48, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(255, 160, 167, 1)",
              "rgba(157, 204, 224, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
              "rgba(115, 78, 48, 1)",
            ],
            borderWidth: 1,
          },
        ],
      };
      return chartDataObject;
    },
    GetCntList: function () {
      const optionObject = {
        scales: {
          xAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: "頻出単語",
              },
            },
          ],
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
                stepSize: 10,
              },
            },
          ],
        },
        onClick: this.clickHandler,
      };
      return optionObject;
    },
  },
  methods: {
    clickHandler: function (event) {
      let elements = this.$refs.child._data._chart.getElementAtEvent(event);
      if (elements.length) {
        let click_word = elements[0]._model.label;
        if (this.word_url_dict[click_word] == "")
          window.alert(`${click_word}に関連するwikipediaのページがありません`);
        else window.open(this.word_url_dict[click_word], "_blank");
      }
    },
    set_word_url_dict: function (result) {
      let word_url_dict = {};
      for (const word of Object.keys(result)) {
        word_url_dict[word] = result[word][0];
      }
      this.word_url_dict = word_url_dict;
    },
  },
};
</script>
