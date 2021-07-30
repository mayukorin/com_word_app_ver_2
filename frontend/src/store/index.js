import Vue from "vue";
import Vuex from "vuex";
import api from "../services/api";

Vue.use(Vuex);

const analyzeModule = {
  namespaced: true,
  state: {
    result: {},
  },
  mutations: {
    set(state, payload) {
      state.result = payload.result;
    },
    clear(state) {
      state.result = {};
    },
  },
  actions: {
    execute(context, payload) {
      console.log(payload.sentence);
      return api({
        method: "post",
        url: "/analyze/execute",
        data: {
          sentence: payload.sentence,
        },
      }).then((response) => {
        console.log(response.data.result);
        context.commit("set", { result: response.data.result });
      });
    },
  },
};

const store = new Vuex.Store({
  modules: {
    analyze: analyzeModule,
  },
});

export default store;
