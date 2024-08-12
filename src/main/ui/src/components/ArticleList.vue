<template>
  <div class="events container">
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
</template>
<script>
  import ArticleCard from '@/components/ArticleCard';
  import articleService from '@/services/articleService.js';
  export default {
    name: 'ArticleList',
    components: {
      ArticleCard,
    },
    created() {
      this.getArticlesData();
    },
    methods: {
      async getArticlesData() {
        articleService.getArticles()
        .then(
          (articles => {
            this["articles"] = articles;
          })
        );
      }
    }
  };
</script>
<style lang="scss" scoped>
  .events {
    margin-top: 100px;
    text-align: center;
  }
</style>