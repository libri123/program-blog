<template>
  <div class="articles">
    <div class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title is-size-1">Articles</h1>
        </div>
      </div>
    </div>
    <div class="container">
      <h2 class="subtitle is-3">Article List</h2>
        <div class="columns is-multiline">
          <div
            v-for="article in articles"
            :article="article"
            :key="article.id"
            class="column is-one-quarter"
          >
            <router-link :to="'/article/' + article.id">
              <ArticleCard :article="article" />
            </router-link>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
  import ArticleCard from '@/components/ArticleCard';
  export default {
    name: 'ArticlePage',
    components: {
      ArticleCard,
    },
    data() {
      return {
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
          }
        ]
      };
    },
  }
</script>


<style lang="scss" scoped>
  .org-description {
    margin-top: 50px;
  }
</style>