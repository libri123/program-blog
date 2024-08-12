// client/src/services/articleService.js

import axios from "axios"

export default {
  async getArticles() {
    let res = await axios.get("http://localhost:8080/articles/");
    return res.data;
  },
  async getArticleSingle(articleId) {
    let res = await axios.get("http://localhost:8080/articles/" + articleId);
    return res.data;
  },
  async createNewArticle() {
    console.log("hello");
  }
}