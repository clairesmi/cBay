module.exports = {
  // options...
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
        secure: false,
        pathRewrite: { "^/api": "/api" },
        logLevel: "debug"
      }
    }
  },
  pages: {
    index: {
      entry: "frontend/src/main.js",
      template: "frontend/public/index.html"
    }
  }
};
