// client/src/services/EventService.js

import axios from "axios"

export default {
  async getArticles() {
    let res = await axios.get("http://localhost:8000/articles");
    return res.data;
  },
  async getArticleSingle(articleId) {
    let res = await axios.get("http://localhost:8000/articles/" + articleId);
    return res.data;
  }
}