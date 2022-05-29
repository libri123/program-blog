<template>
  <div class="event-single">
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">{{ article.name }}</h1>
          <h2 class="subtitle ">Event date</h2>
        </div>
      </div>
    </section>
    <section class="event-content">
      <div class="container">
        <p class="is-size-4 description">Event description</p>
        <p class="is-size-4">Location:</p>
        <p class="is-size-4">Category:</p>
        <div class="event-images columns is-multiline has-text-centered">
          <div class="column is-one-third">IMAGE PLACEHOLDER</div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
  import articleService from '@/services/articleService.js';
  export default {
    name: 'SingleArticle',
    data() {
      // NEW - initialize the event object
      return {
        article: {}
      }
    },
    created() {
      this.getArticleData(); // NEW - call getEventData() when the instance is created
    },
    // NEW
    methods: {
      async getArticleData() {
        // Use the eventService to call the getEventSingle() method
        articleService.getArticleSingle(this.$route.params.id)
        .then(
          (article => {
            this.$set(this, "article", article);
          }).bind(this)
        );
      }
    }
  }
</script>
<style lang="scss" scoped>
  .event-single {
    margin: 0;
  }
  .hero {
    margin-bottom: 70px;
  }
  .event-images {
    margin-top: 50px;
  }
  .description {
    margin-bottom: 30px;
  }
</style>