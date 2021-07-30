import Vue from "vue";
import Vuex from "vuex";


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
    print() {
      console.log("ok");
    }
  },
  actions: {
    execute(context, payload) {
      console.log(payload);
      context.commit("print");
    },
  },
};

const store = new Vuex.Store({
  modules: {
    analyze: analyzeModule,
  },
});

export default store;
