<script>
import { Bar, mixins } from "vue-chartjs";

export default {
  name: "WordGraph",
  extends: Bar,
  mixins: [mixins.reactiveProp],
  props: {
    wordList: {
      type: Array,
      required: false,
    },
    cntList: {
      type: Array,
      required: false,
    },
    chartData: {
      type: Object,
      required: false,
    },
    options: {
      type: Object,
      required: false,
    },
  },
  data() {
    return {
      chartObject: null,
    };
  },
  mounted() {
    this.chartObject = this.renderChart(this.chartData, this.options);
  },
};
</script>
