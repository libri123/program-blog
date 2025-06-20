import { createStore } from 'vuex'

// Create a new store instance.
const store = createStore({
    state () {
      return {
        count: 1,
        articles: [
            {
              id      : 1,
              name: "test1",
              date: "2023.1.1",
              category: "python"
            },
            {
              id      : 2,
              name: "test2",
              date: "2023.1.2",
              category: "java"
            },
            {
                id      : 3,
                name: "test3",
                date: "2023.1.3",
                category: "css"
              }
          ]
      }
    },
    mutations: {
        increment (state) {
            state.count++
        },
        initialize_data (state) {
            state.count = 1
        }
    }
})

export default store