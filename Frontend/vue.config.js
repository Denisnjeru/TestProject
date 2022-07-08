const path = require("path");

module.exports = {
  pluginOptions: {
    "style-resources-loader": {
      preProcessor: "scss",
      patterns: [path.resolve(__dirname, "./src/styles/main.scss")]
    }
  },
  devServer: {
    host: 'localhost',
  },
  pwa: {
    themeColor: '#f5f6f7'  
  },
  
};